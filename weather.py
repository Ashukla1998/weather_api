import requests

API_KEY = 'f5857f5577a6fa59271adbef5ecf7b10'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city, date):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        if date == "today":
            return data['main']['temp'], data['wind']['speed'], data['main']['pressure']
        else:
            return None
    else:
        print(f"Error: {data['message']}")
        return None

def get_user_option():
    print("1. Get weather")
    print("2. Get Wind Speed")
    print("3. Get Pressure")
    print("0. Exit")
    return int(input("Enter your choice: "))

def main():
    while True:
        option = get_user_option()

        if option == 0:
            print("Terminating the program.")
            break

        elif option in [1, 2, 3]:
            city = input("Enter the city name: ")
            date = input("Enter the date (today): ").lower()

            if date != "today":
                print("Invalid date input. Please enter 'today' as the date.")
                continue

            weather_data = get_weather_data(city, date)
            if weather_data is not None:
                if option == 1:
                    temp, _, _ = weather_data
                    print(f"The temperature in {city} today is {temp}°C.")
                elif option == 2:
                    _, wind_speed, _ = weather_data
                    print(f"The wind speed in {city} today is {wind_speed} m/s.")
                elif option == 3:
                    _, _, pressure = weather_data
                    print(f"The pressure in {city} today is {pressure} hPa.")
        else:
            print("Invalid option. Please choose a valid option (1, 2, 3, or 0).")

if __name__ == "__main__":
    main()
