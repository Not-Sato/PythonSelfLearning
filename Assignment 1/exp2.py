import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 19.0760,
    "longitude": 72.8777,
    "current_weather": "true",
    "timezone": "auto",
}

try:
    response = requests.get(url, params=params, timeout=10)
    if response.status_code != 200:
        print("Error: HTTP status code", response.status_code)
    else:
        data = response.json()
        weather = data["current_weather"]
        temperature = weather["temperature"]
        windspeed = weather["windspeed"]
        weathercode = weather["weathercode"]
        timezone = data["timezone"]

        summary = (
            "Weather Report\n"
            f"Temperature: {temperature} C\n"
            f"Windspeed: {windspeed} km/h\n"
            f"Weather Code: {weathercode}\n"
            f"Timezone: {timezone}\n"
        )

        print(summary)
        with open(r".\Assignment 1\weather_report.txt", "w") as file:
            file.write(summary)

except requests.exceptions.Timeout:
    print("Error: The request timed out")
except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the network")
except requests.exceptions.RequestException as e:
    print("Error:", e)