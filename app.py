from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz


# Load environment variables
load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("WEATHER_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        return render_template('weather.html', weather=weather_data)
    else:
        error_msg = 'City not found. Please try again.'
        return render_template('index.html', error=error_msg)

if __name__ == '__main__':
    app.run(debug=True)
