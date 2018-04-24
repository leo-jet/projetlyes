from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .extract_data import ExtractData, TOKEN

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_graph_data(request):
    if request.method == "POST":
        extractor = ExtractData(token=TOKEN)
        my_id = request.POST.get('id', None)
        data = None
        if id:
            data = extractor.get_graph_likes(my_id)
        else:
            data = extractor.get_graph_likes("661094353948044")
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        content = {
            'error': True
        }
        return HttpResponse(json.dumps(content), content_type='application/json')

