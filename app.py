from flask import Flask, render_template, request
import requests
from datetime import datetime
import pytz

app = Flask(__name__)
import os
API_KEY = os.getenv("WEATHER_API_KEY")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")

    try:
        weather_data = response.json()
        print("API Response JSON:", weather_data)
    except Exception as e:
        print("Error parsing JSON:", e)
        error_msg = 'Error parsing weather data. Please try again.'
        return render_template('index.html', error=error_msg)

    # Check if API returned success code inside JSON
    if weather_data.get('cod') == 200:
        return render_template('weather.html', weather=weather_data)
    else:
        error_msg = weather_data.get('message', 'City not found or error retrieving data. Please try again.')
        return render_template('index.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
