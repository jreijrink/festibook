from django.shortcuts import get_object_or_404, render

from querying.spelchecker import checkSpelling
from querying.decomposition import decompose
from querying.searchhistory import applySearchHistory
from querying.indexer import retrieveFromIndex
from querying.suggestor import createSuggestions

from common.models import Document

def index(request):
    documents = createSuggestions()
    context = {'suggestions': documents}
    return render(request, 'querying/index.html')

def search(request):
    query = request.GET.get('q', '')
    
    query = checkSpelling(query)
    query = decompose(query)
    query = applySearchHistory(query)
    
    documents = retrieveFromIndex(query)
    
    context = {'documents': documents, 'query': query}
    return render(request, 'querying/search.html', context)

def detail(request, document_id):
    document = get_object_or_404(Document, pk=document_id)
    return render(request, 'querying/detail.html', {'document': document})