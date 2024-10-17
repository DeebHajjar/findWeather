from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api_key = "5e664efb947890a23125b3a453c4c503"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form['city']
        complete_url = base_url + "q=" + city_name + "&units=metric" + "&appid=" + api_key
        response = requests.get(complete_url)
        x = json.loads(response.text)

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            
            return render_template('weather.html', 
                                   city=city_name,
                                   temperature=current_temperature,
                                   pressure=current_pressure,
                                   humidity=current_humidity,
                                   description=weather_description)
        else:
            return render_template('weather.html', error="City not found")
    
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)