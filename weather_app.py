# DSC 510
# Week 12
# Final Project Week 12
# Author Ruben Brionez Jr
# 11/19/2023


import requests
from urllib.error import HTTPError

api_key = "1aa4ba963fc3d2784de2be6a2065c2d3"
degree_sign = u'\N{DEGREE SIGN}'  # Creates the degree symbol


def get_lat_long_zip(zip_code, api_key, country_code="us"):
    api_call = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"  # Calls the
    # api based on the zip code entered. Country defaulted to US.
    response = requests.get(api_call)  # Sets the JSON response to a variable
    api_data = response.json()  # Converts the JSON response to a dictionary
    lat = api_data["lat"]
    lon = api_data["lon"]
    return lat, lon


def get_lat_lon_city(city_name, state_code, country_code="us"):
    api_call = (f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}"  # Calls the
                f"&limit={5}&appid={api_key}")  # Calls the
    # api based on the city and state entered. Country defaulted to US.
    response = requests.get(api_call)
    api_data = response.json()
    lat = api_data[0]["lat"]
    lon = api_data[0]["lon"]
    return lat, lon


def get_current_weather(lat, lon):
    current_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"  # Makes a
    # call to the api to retrieve the current weather data
    response = requests.get(current_call)
    current_data = response.json()
    weather_description = current_data["weather"][0]["description"].title()  # Sets the weather description to a
    # variable and applies the title attribute
    forecast = current_data['main']  # Sets the dictionary 'main' to a variable in order to access the values
    temperature_f = round((((forecast['temp'] - 273.15) * 1.8) + 32), 0)  # This first lines starts several lines of
    # code that convert the Kelvin temperate to either Fahrenheit or Celsius
    # and stores them in a variable to access later
    temperature_c = round((forecast['temp'] - 273.15), 1)
    feels_like_f = round((((forecast['feels_like'] - 273.15) * 1.8) + 32), 1)
    feels_like_c = round((forecast['feels_like'] - 273.15), 1)
    low_temp_f = round((((forecast['temp_min'] - 273.15) * 1.8) + 32), 1)
    low_temp_c = round((forecast['temp_min'] - 273.15), 1)
    high_temp_f = round((((forecast['temp_max'] - 273.15) * 1.8) + 32), 1)
    high_temp_c = round((forecast['temp_max'] - 273.15), 1)
    pressure = forecast['pressure']  # No conversion was necessary for pressure or humidity
    humidity = forecast['humidity']
    value_tuple = (temperature_f, temperature_c, feels_like_f, feels_like_c, low_temp_f, low_temp_c, high_temp_f,
                   high_temp_c, pressure, humidity, weather_description)  # a tuple of all variables to be returned
    return value_tuple


def show_fahrenheit(lat, lon):  # This function shows the user all temperatures in Fahrenheit
    value_tuple = get_current_weather(lat, lon)  # Retrieves the returned tuple
    print("-----------------------------------------------------------------------------------------")
    print(f"The current temperature is {value_tuple[0]}{degree_sign}\nThe 'feel like' temperature is {value_tuple[2]}"
          f"{degree_sign}\nThe low temperature is {value_tuple[4]}{degree_sign}\nThe high temperature is "
          f"{value_tuple[6]}{degree_sign}\nThe pressure is {value_tuple[8]}mb\nThe humidity is {value_tuple[9]}%\nThe "
          f"weather description is: {value_tuple[10]}")
    print("-----------------------------------------------------------------------------------------")


def show_celsius(lat, lon):  # This function shows the user all temperatures in Celsius
    value_tuple = get_current_weather(lat, lon) # Retrieves the returned tuple
    print("-----------------------------------------------------------------------------------------")
    print(f"The current temperature is {value_tuple[1]}{degree_sign}\nThe 'feel like' temperature is {value_tuple[3]}"
          f"{degree_sign}\nThe low temperature is {value_tuple[5]}{degree_sign}\nThe high temperature is "
          f"{value_tuple[7]}{degree_sign}\nThe pressure is {value_tuple[8]}mb\nThe humidity is {value_tuple[9]}%\nThe "
          f"weather description is: {value_tuple[10]}")
    print("-----------------------------------------------------------------------------------------")


def show_forecast(lat, lon):  # This function allows the user to pick which temperature type they would like
    # to see in the output
    degree = input("Would you like to see the temperatures in Celsius or Fahrenheit, Enter 'C' or 'F': ")
    degree = degree.lower()
    if degree == "c":
        show_celsius(lat, lon)  # Calls the show Celsius function
    elif degree == "f":
        show_fahrenheit(lat, lon)  # Calls the show Fahrenheit function
    else:
        print("Be sure you entered 'C' or 'F'")


def main():  # This is the main function of the program
    print("***Welcome to the Weather App***")  # Prints the welcome message
    while True:
        choice = input("Do you want to search by 'city' or 'zip'? Enter 'quit' to exit:  ")  # Requests user input to
        # start the forecast search by city or zip
        choice = choice.lower()
        try:
            if choice == 'city':
                city_name = input("Please enter your city: ")
                state_code = input("Please enter the two letter abbreviation for state:  ")
                get_lat_lon_city(city_name, state_code)  # Calls the function to get lat and lon by city and state
                lat = get_lat_lon_city(city_name, state_code)[0]  # Sets lat to a variable
                lon = get_lat_lon_city(city_name, state_code)[1]  # Sets lon to a variable
                get_current_weather(lat, lon)  # Calls function to get forecast from API
                show_forecast(lat, lon)  # Calls function to show the output in desired format
            elif choice == 'zip':
                zip_code = int(input("Please enter your zip code: "))
                lat = get_lat_long_zip(zip_code, api_key)[0]
                lon = get_lat_long_zip(zip_code, api_key)[1]
                get_current_weather(lat, lon)  # Calls function to get forecast from API
                show_forecast(lat, lon)  # Calls function to show the output in desired format
            elif choice == "quit":
                print("Thanks for stopping by!")
                break  # Exits the program when requested
            else:
                print("Please be sure to enter 'city' or 'zip'")
        except ValueError:
            print("Make sure you entered correct values for 'zip' this should be 5 digits.")  # This will catch invalid
            # input at the zip code where an integer value is required
        except HTTPError as err:
            print("The site may be down or has moved, please verify with a browser")  # This HTTP exception is meant to
            # catch error generated from a down site or unreachable site.
        except IndexError:
            print("Please be sure a valid city and state were entered. Try Again.")  # This exception is meant to catch
            # any invalid input that would generate an error when passed to the API
        except KeyError:
            print("Make sure you entered correct values for 'zip' this should be 5 digits.")  # This exception should
            # also catch invalid input that would generate an error from the API


if __name__ == "__main__":
    main()
