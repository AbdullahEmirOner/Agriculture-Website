from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Weather, AgricultureNews
from .utils import get_weather

def home(request):
    # Varsayılan şehir
    default_city = 'Ankara'
    city = request.GET.get('city', default_city)  # Kullanıcıdan şehir al, yoksa varsayılanı kullan
    weather_data = get_weather(city)  # Girilen şehir için hava durumu verisini al
    agriculture_news_list = AgricultureNews.objects.all()  # Tüm tarım haberleri

    # Sayfalama ayarları
    paginator = Paginator(agriculture_news_list, 12)  # Sayfa başına 12 haber
    page_number = request.GET.get('page')  # URL'den sayfa numarasını al
    page_obj = paginator.get_page(page_number)  # İlgili sayfayı al

    context = {
        'weather_data': weather_data,
        'agriculture_news': page_obj,  # Sayfaya özel haberler
    }
    return render(request, 'index.html', context)