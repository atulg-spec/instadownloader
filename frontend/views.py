from django.shortcuts import render
from django.http import HttpResponse
from .forms import media_data
import requests
from django.http import HttpResponse,JsonResponse
from urllib.request import urlopen
from django.shortcuts import render

def download_image(request):
    if request.method == 'GET':
        media_url = request.GET.get('url')

        if not media_url:
            return HttpResponse("Please provide a valid 'url' parameter in the query string.", status=400)

        try:
            # Fetch the media file from the URL
            response = requests.get(media_url, stream=True)
            response.raise_for_status()

            # Set the appropriate content type for the response
            content_type = response.headers.get('content-type', 'application/octet-stream')
            file_extension = content_type.split('/')[-1]
            response_headers = {'Content-Type': content_type, 'Content-Disposition': f'attachment; filename=media.{file_extension}'}

            # Return the media content as the response
            return HttpResponse(response.content, headers=response_headers)

        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error fetching the media file: {e}", status=500)

    return HttpResponse("Invalid request method. Use the HTTP GET method.", status=405)


# Create your views here.
def show_image(request, image_url):
    try:
        image_content = urlopen(image_url).read()
        image_format = "image/jpeg" if image_url.lower().endswith(".jpg") or image_url.lower().endswith(".jpeg") else "image/png"
        return HttpResponse(image_content, content_type=image_format)
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}", status=404)

def home(request):
    if request.method == 'POST':
        form = media_data(request.POST)
        if form.is_valid():
            mdata = []
            try:
                url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post_v2.php"
                posturl=form.cleaned_data['url']
                querystring = {"url":posturl}
                headers = {
                	"X-RapidAPI-Key": "be20525d20mshb68d723e44569dfp143f7cjsnf80ed42d78b9",
                	"X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
                }
                response = requests.get(url, headers=headers, params=querystring)
                jsonresponse = response.json()
                print(jsonresponse)
                if jsonresponse['items'][0]['media_type'] == 1:
                    mdata.append(jsonresponse['items'][0]['image_versions2']['candidates'][0]['url']) #MEDIA TYPE 1
                elif jsonresponse['items'][0]['media_type'] == 2:
                    mdata.append(jsonresponse['items'][0]['video_versions'][0]['url']) #MEDIA TYPE 2
                elif jsonresponse['items'][0]['media_type'] == 8:
                # MEDIA TYPE 8
                    for x in jsonresponse['items'][0]['carousel_media']:
                        print('-=-=-=-=-=-=-=-=-=x-=-=-=-=-=')
                        mdata.append(x['image_versions2']['candidates'][0]['url'])
                print(mdata)
            except Exception as e:
                print(f'Error: {e}')
            context = {
                'mdata':mdata
            }
            return render(request,'index.html',context)
    return render(request,'index.html')

