from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MemoryForm
from .models import Current_coord


@login_required
def new_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)

        if form.is_valid():
            memory = form.save(commit=False)
            memory.author = request.user

            coord = Current_coord.objects.first()
            if coord != None:
                memory.lat = coord.lat
                memory.lon = coord.lon

            memory.save()
            Current_coord.objects.all().delete()
            return redirect('profile')

        return render(request, 'memory/new_memory.html', {'form': form})

    form = MemoryForm
    return render(request, 'memory/new_memory.html', {'form': form})


def get_coord(request):
    if request.method == 'GET':
        if 'lat' in request.GET and 'lon' in request.GET:
            Current_coord.objects.all().delete()
            lat = request.GET['lat']
            lon = request.GET['lon']
            Current_coord.objects.create(lat=lat, lon=lon)
            return HttpResponse('success')
