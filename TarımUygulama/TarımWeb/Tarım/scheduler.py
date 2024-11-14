from apscheduler.schedulers.background import BackgroundScheduler
from .utils import get_weather, get_agriculture_news
from .models import Weather, AgricultureNews  
import logging

logger = logging.getLogger(__name__)

def fetch_weather_data():
    cities = [
        "Istanbul", "Ankara", "Izmir", "Bursa", "Antalya", 
        "Adana", "Gaziantep", "Konya", "Kayseri", "Mersin",
        "Diyarbakir", "Sakarya", "Trabzon", "Manisa", "Eskişehir",
        "Aydın", "Balıkesir", "Samsun", "Denizli", "Kahramanmaraş",
        "Elazığ", "Zonguldak", "Tekirdağ", "Bolu", "Sakarya",
        "Amasya", "Kastamonu", "Kırıkkale", "Nevşehir", "Karaman",
        "Niğde", "Bartın", "Yozgat", "Burdur", "Uşak",
        "Ordu", "Rize", "Artvin", "Giresun", "Aksaray",
        "Bilecik", "Çankırı", "Düzce", "Kırklareli", "Tekirdağ",
        "Çorum", "Tokat", "Sivas", "Bayburt", "Kars", 
        "Ağrı", "Ardahan", "Hakkari", "Van", "Batman", 
        "Mardin", "Şırnak", "Siirt", "Bitlis", "Diyarbakır"
    ]
    weather_data = get_all_cities_weather(cities)
    for weather in weather_data:
        Weather.objects.update_or_create(
            city=weather['city'],
            defaults={
                'temperature': weather['temperature'],
                'description': weather['description'],
                'icon': weather['icon']
            }
        )
        logger.info(f"{weather['city']} için güncel hava durumu: {weather}")

def fetch_agriculture_news_data():
    news_articles = get_agriculture_news()
    if news_articles:
        for article in news_articles:
            AgricultureNews.objects.update_or_create(
                title=article['title'],
                defaults={
                    'description': article.get('description', ''),
                    'url': article.get('url', ''),
                    'published_at': article.get('published_at', ''),
                    'image_url': article.get('image')  
                }
            )
            logger.info(f"{article['title']} kaydedildi.")
    else:
        logger.error("Tarım haberleri alınamadı.")



def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_weather_data, 'interval', minutes=5)  
    scheduler.add_job(fetch_agriculture_news_data, 'interval', minutes=5)  
    scheduler.start()
