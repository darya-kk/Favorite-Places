from django.shortcuts import render
import random
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PlaceForm


def get_places(request):

    return request.session.get('places', [])


def save_places(request, places):
    """Зберегти список місць у сесію"""
    request.session['places'] = places
    request.session.modified = True


def index(request):
    places = get_places(request)
    random_place = None

    if request.method == 'POST' and 'random' in request.POST and places:
        weights = [p['rating'] for p in places]
        random_place = random.choices(places, weights=weights, k=1)[0]

    return render(request, 'places/index.html', {
        'places': places,
        'random_place': random_place,
    })


def places_list(request):
    places = get_places(request)
    return render(request, 'places/places_list.html', {'places': places})


def place_detail(request, index):
    places = get_places(request)
    try:
        place = places[index]
    except IndexError:
        return redirect('places_list')
    return render(request, 'places/place_detail.html', {'place': place})


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = get_places(request)
            new_place = {
                'name': form.cleaned_data['name'],
                'description': form.cleaned_data['description'] or '',
                'place_type': form.cleaned_data['place_type'] or 'невідомо',
                'location': form.cleaned_data['location'] or '',
                'rating': form.cleaned_data['rating'],
                'created_at': datetime.now().strftime('%d.%m.%Y %H:%M'),
            }
            places.append(new_place)
            save_places(request, places)
            return redirect('places:places_list')
    else:
        form = PlaceForm()

    return render(request, 'places/add_place.html', {'form': form})
