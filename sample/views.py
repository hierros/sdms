from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template import RequestContext
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from sample.forms import SampleForm, TreatmentForm, FeedstockForm, FractionForm, StatusForm, LocationForm
from sample.models import Sample, Treatment, Feedstock, Fraction, Status, Location
from attachment.forms import AttachmentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re


# Create your views here.

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

def paging(request, query):
    paginator = Paginator(query, 30)
    page = request.GET.get('page')
    try:
        sample = paginator.page(page)
    except PageNotAnInteger:
        sample = paginator.page(1)
    except EmptyPage:
        sample = paginator.page(paginator.num_pages)

    return sample

@login_required
def enter(request):
    form = SampleForm(request.POST or None)
    attach = AttachmentForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
        attach.save(commit=False)
        attach.sdms=form
        attach.save()
        return HttpResponseRedirect('/sdms/success/')
    print request.user
    return render_to_response('enter.html', {'form': form, 'attach': attach}, context_instance= RequestContext(request))

def success(request):
    return render_to_response('success.html')

@login_required
def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['id', 'sample_name', 'comment', 'location__building', 'feedstock__feedstock_name'])

        found_entries = Sample.objects.filter(entry_query).exclude(status_id=3).order_by('id')
    queries = request.GET.copy()
    sample = paging(request, found_entries)
    return render_to_response('search_results.html', {'sample': sample, 'queries': queries},
                              context_instance=RequestContext(request))
@login_required
def range_search(request):
    found_entries = None
    if ('begin' in request.GET and 'end' in request.GET):
        begin = request.GET['begin']
        end = request.GET['end']
        found_entries = Sample.objects.filter(id__range=(begin, end)).exclude(status_id=3).order_by('id')
    else:
        return render_to_response('search.html', context_instance=RequestContext(request))

    queries = request.GET.copy()
    sample = paging(request, found_entries)

    return render_to_response('search_results.html', {'sample': sample, 'queries': queries},
                              context_instance=RequestContext(request))

def update(request, id):
    sample = Sample.objects.get(id=id)
    form = SampleForm(request.POST or None, instance=sample)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/sdms/success/')
    return render_to_response('update.html', {'form': form}, context_instance=RequestContext(request))

def delete(request, id):
    sample = Sample.objects.get(id=id)
    sample.status_id = 3
    sample.save()
    return render_to_response('success.html')