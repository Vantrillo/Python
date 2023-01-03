from django.shortcuts import render
from django.http import Http404

from .models import Pet

def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {
        'pets':pets,
    })
    #return HttpResponse('<p>home view</p>')

def pet_detail(request, pet_id):
    try:
        pet=Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet Not Found')
    return render(request, 'pet_detail.html', {
        'pet': pet,
    })
    #return HttpResponse(f'<p>pet_detail view with id {pet_id}</p>')
