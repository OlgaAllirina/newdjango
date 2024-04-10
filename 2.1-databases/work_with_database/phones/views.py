from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    # отображение основной (главной) страницы
    return redirect('catalog')


def show_catalog(request):
    """
    При запросе <имя_сайта>/catalog/iphone-x должна открываться страница с отображением информации по телефону.
    iphone-x — это для примера, это значние берётся из slug.
    В каталоге необходимо добавить возможность менять порядок отображения товаров:
    по названию в алфавитном порядке и по цене по убыванию и по возрастанию.
    """
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    phones_objects = Phone.objects.all()

    if sort_pages == 'max_price':
        phones_objects = phones_objects.order_by('price').reverse()
    elif sort_pages == 'min_price':
        phones_objects = phones_objects.order_by('price')
    elif sort_pages == 'name':
        phones_objects = phones_objects.order_by('name')

    context = {'phones': phones_objects,}
    return render(request, template, context)


def show_product(request, slug):
    # При запросе <имя_сайта>/catalog должна открываться страница с отображением всех телефонов
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
