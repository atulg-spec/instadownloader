from django.http import JsonResponse,HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .forms import media_data
from bs4 import BeautifulSoup
import requests
import json

# Create your views here.
User = get_user_model()

def mediadata(post_url):
    from urllib import request
    url = "https://v3.igdownloader.app/api/ajaxSearch"
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://igdownloader.app",
        "Referer": "https://igdownloader.app/",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    payload = {
        "q": post_url,
        "t": "media",
        "lang": "en"
    }
    response = requests.post(url, headers=headers, data=payload,proxies=request.getproxies())
    jdata = response.json()
    image_urls = []
    download_links = []
    soup = BeautifulSoup(jdata["data"], 'html.parser')
    download_elements = soup.find_all('a', class_='abutton is-success is-fullwidth btn-premium mt-3')
    download_links = [a['href'] for a in download_elements]

    return download_links




@csrf_exempt
def getdata(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = media_data(data)
        if form.is_valid():
            accesstoken = form.cleaned_data['accesstoken']
            url = form.cleaned_data['url']
            try:
                usr = User.objects.get(access_token=accesstoken)
                if usr == None:
                    return JsonResponse({'status':'failed','message':'Invalid Usage !'})
                else:
                    try:
                        download_urls = mediadata(url)
                        return JsonResponse({'status':'success','download_urls':download_urls})
                    except:
                        return JsonResponse({'status':'failed','message':'Invalid URL !'})
            except Exception as e:
                return JsonResponse({'status':'failed','message':'Invalid Usage !'})
        else:
            return JsonResponse({'status':'failed','message':'Invalid Usage !'})
    else:
        return HttpResponse('<h1><center>Error 404</center></h1>')