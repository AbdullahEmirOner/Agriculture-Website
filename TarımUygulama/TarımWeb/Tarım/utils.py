import requests

def get_weather(city):
    api_key = 'c45966f73686cf713980007192a3b8aa'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"  

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": city,  
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "icon": data["weather"][0]["icon"]
        }
        return weather

    except requests.exceptions.HTTPError as err:
        print(f"Hava durumu API hatası: {err}")
        return None

def get_all_cities_weather(cities):
    weather_data = []
    for city in cities:
        weather = get_weather(city)
        if weather:
            weather_data.append(weather)
    return weather_data


def get_agriculture_news():
    api_key = '73078443d44f4fc9b292370fe3a0f98b'
    url = f'https://newsapi.org/v2/everything?q=tarım OR tarımsal&language=tr&sortBy=publishedAt&apiKey={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        articles = data.get('articles', [])

        news_list = []
        for article in articles:
            image_url = article.get("urlToImage", "")

            if 'tarım' in article['title'].lower() or 'tarım' in (article.get('description') or '').lower():
                news_item = {
                    "title": article["title"],
                    "description": article.get("description", ""),
                    "published_at": article["publishedAt"],
                    "url": article["url"],
                    "image": image_url if image_url else "https://example.com/default_image.jpg"  # Varsayılan resim ekle
                }
                news_list.append(news_item)
        return news_list

    except requests.exceptions.HTTPError as err:
        print(f"NewsAPI hatası: {err}")
        return None
