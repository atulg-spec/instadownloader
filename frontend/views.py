from django.shortcuts import render
from django.http import HttpResponse
from .forms import media_data
import json
import requests
from django.http import HttpResponse
from urllib.request import urlopen
from django.core.files.temp import NamedTemporaryFile
from django.core.files import File
from django.shortcuts import render

def download_image(request, image_url):
    try:
        # Fetch the image from the URL
        response = requests.get(image_url)
        response.raise_for_status()

        # Create a temporary file to store the image
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(response.content)
        img_temp.flush()

        # Create a Django File object from the temporary file
        image_file = File(img_temp)

        # Set the appropriate content type for the response
        content_type = response.headers['Content-Type']

        # Create an HttpResponse with the image file and content type
        response = HttpResponse(image_file.read(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename=image.jpg'

        return response

    except Exception as e:
        # Handle any errors that may occur (e.g., invalid URL, network error)
        return render(request, 'error_page.html', {'error_message': str(e)})



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
            url = 'http://192.168.92.1:8000/api-v1/getdata'
            data = {
                'url':form.cleaned_data['url'],
                'accesstoken':'5966f16e-cfbf-4a3d-8431-118c2ba32393'
            }
            data = json.dumps(data)
            response = requests.post(url,data)
            mdata = response.json()
            context = {
                'media_data':mdata,
            }
            return render(request,'index.html',context)
    return render(request,'index.html')