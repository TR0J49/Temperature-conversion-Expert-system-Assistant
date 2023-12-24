import pyttsx3
import requests

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["cod"] != "404":
        main_data = data["main"]
        temperature = main_data["temp"]
        return temperature
    else:
        return None

def temperature_converter():
    speak("Welcome to Hack Tech World Technologies Private Limited , Temperature Converter Expert System.")
    speak("Do you want to convert from Celsius to Fahrenheit, from Fahrenheit to Celsius, or check the weather?")

    choice = input("Enter your choice (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius, 3 for weather check): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        speak(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        speak(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
    elif choice == '3':
        city = input("Enter the city for weather check: ")
        api_key = "f496f4c9efc08706626a74e3ceb89186"  
        temperature = get_weather(city, api_key)
        
        if temperature is not None:
            speak(f"The current temperature in {city} is {temperature:.2f} Celsius.")
        else:
            speak(f"Unable to fetch weather information for {city}. Please check the city name and try again.")
    else:
        speak("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    temperature_converter()
