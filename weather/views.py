from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == "POST":
        city = request.POST.get("city") # Use request.POST.get() to avoid KeyError if 'city' is not in POST data
        api_key = '6351029f1ceba5d6baa83c880e57b7ee'  # Replace with your API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        try:
            response = urllib.request.urlopen(url).read()
            json_data = json.loads(response)
            print(json_data)
            temperature = json_data['main']['temp']
            humidity = json_data['main']['humidity']
            cordinate = json_data['coord']['lon']
            pressure = json_data['main']['pressure']
            code = json_data['cod']
            # You can extract more data from json_data as needed
        except Exception as e:
            # Handle exceptions, e.g., city not found, API request failed
            error_message = f"Error: {str(e)}"
            return render(request, 'index.html', {'city': city, 'error_message': error_message})
    else:
        code = ''
        city = '' 
        temperature = '' 
        humidity = '' 
        cordinate = ''
        pressure = ''
    return render(request, 'index.html', {'city': city, 'temperature': temperature,"humidity":humidity,'cordinate':cordinate,'pressure':pressure,'code':code})

