#!/usr/bin/env python3

import requests
import json
import time

# Координаты Москвы (можно поменять на свои)
LATITUDE = 55.7558
LONGITUDE = 37.6176

def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m"],
        "timezone": "Europe/Moscow"
    }
    
    # Пробуем 3 раза с задержкой
    for attempt in range(3):
        try:
            response = requests.get(url, params=params, timeout=10)
            if response.status_code == 200:
                data = response.json()
                current = data.get("current", {})
                
                temp = current.get("temperature_2m", 0)
                humidity = current.get("relative_humidity_2m", 0)
                wind = current.get("wind_speed_10m", 0)
                
                # Иконка погоды (примитивная, но работает)
                icon = "☀️" if temp > 20 else "⛅" if temp > 10 else "❄️" if temp < 0 else "🌤️"
                
                return {
                    "text": f"{icon} {temp:.0f}°C",
                    "alt": "Weather",
                    "tooltip": f"🌡️ Temperature: {temp:.0f}°C\n💧 Humidity: {humidity:.0f}%\n💨 Wind: {wind:.1f} km/h"
                }
            else:
                print(f"⚠️ API error: {response.status_code}", file=sys.stderr)
        except requests.exceptions.Timeout:
            print(f"⏱️ Timeout attempt {attempt + 1}/3", file=sys.stderr)
            time.sleep(2)
        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            time.sleep(2)
    
    # Если ничего не получилось - показываем заглушку
    return {
        "text": "🌐",
        "alt": "offline",
        "tooltip": "Weather unavailable"
    }

if __name__ == "__main__":
    import sys
    try:
        weather_data = get_weather()
        print(json.dumps(weather_data))
    except Exception as e:
        print(f"❌ Fatal error: {e}", file=sys.stderr)
        print(json.dumps({"text": "⚠️", "alt": "error", "tooltip": "Weather error"}))