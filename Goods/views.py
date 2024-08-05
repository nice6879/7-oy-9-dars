from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Loan

def lending_page(request):
    loans = Loan.objects.all()
    return render(request, 'lending.html', {'loans': loans})

def paginator_page(data, num, request):
    paginator = Paginator(data.order_by('-id'), num)
    pages = request.GET.get('page')
    try:
        paginated_list = paginator.page(pages)
    except PageNotAnInteger:
        paginated_list = paginator.page(1)
    except EmptyPage:
        paginated_list = paginator.page(paginator.num_pages)
    return paginated_list

def main(request):
    banners = models.Banner.objects.filter(is_active = True)[:5]
    
    context = {}
    context['banners'] = paginator_page(banners, 8, request)

    return render(request, 'index.html')