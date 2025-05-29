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
