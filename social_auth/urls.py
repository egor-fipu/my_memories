from django.contrib import admin
from django.urls import path, include

from memory.views import new_memory, get_coord
from .views import Home, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile, name='profile'),
    path('profile/new/', new_memory, name='new_memory'),
    path('get_coord/', get_coord, name='get_coord'),
    path('', Home.as_view(), name='home'),
]
