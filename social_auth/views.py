from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView

from memory.models import Memory
from .settings import PAGE_SIZE


class Home(TemplateView):
    template_name = 'home.html'


@login_required
def profile(request):
    user = request.user
    memory_list = Memory.objects.filter(author=user)
    paginator = Paginator(memory_list, PAGE_SIZE)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render(request, 'profile.html', context)
