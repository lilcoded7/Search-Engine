from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchRank
from .models import WebPage

def search(request):
    query = request.GET.get('q', '')
    if query:
        search_query = SearchQuery(query)
        results = WebPage.objects.annotate(
            rank=SearchRank('search_vector', search_query)
        ).filter(search_vector=search_query).order_by('-rank')
    else:
        results = WebPage.objects.none()
    return render(request, 'search_results.html', {'results': results, 'query': query})
