import requests


def get_weather(city_name):
    url = f"https://wttr.in/{city_name}?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        description = current["weatherDesc"][0]["value"]
        humidity = current["humidity"]

        print(f"\n--- Weather in {city_name.title()} ---")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%\n")

    except requests.exceptions.RequestException:
        print("\nError: Network issue or invalid city name.\n")
    except (KeyError, IndexError, ValueError):
        print("\nError: Unable to read weather data.\n")


if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
