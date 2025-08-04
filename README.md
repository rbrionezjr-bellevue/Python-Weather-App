# 🌤️ Weather App – Final Project

This is a Python command-line weather application created for the final project of Week 12 in the DSC 510 course. The app allows users to retrieve current weather conditions using either a ZIP code or city/state combination via the OpenWeatherMap API.

---

## 📦 Features

- Search weather by:
  - ZIP code
  - City and State
- Supports temperatures in both:
  - Fahrenheit (℉)
  - Celsius (℃)
- Displays:
  - Current temperature
  - Feels like temperature
  - High and low temperatures
  - Pressure (mb)
  - Humidity (%)
  - Weather description

---

## 🚀 How It Works

The script retrieves latitude and longitude based on user input, then queries OpenWeatherMap's current weather endpoint to display formatted weather data.

Users can choose to view the output in Celsius or Fahrenheit and can run multiple queries in a single session.

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install required libraries with:

```bash
pip install requests
```

---

## 🔑 API Key

This project uses the OpenWeatherMap API. You must supply a valid API key to use it.

Replace the placeholder value in the script with your own key:

```python
api_key = "YOUR_API_KEY_HERE"
```

You can get a free API key from: [https://openweathermap.org/api](https://openweathermap.org/api)

---

## 🖥️ Usage

Run the script from the terminal:

```bash
python weather_app.py
```

Follow the prompts to enter either a ZIP code or city/state. Then choose Fahrenheit or Celsius display.

Example session:

```
***Welcome to the Weather App***
Do you want to search by 'city' or 'zip'? Enter 'quit' to exit: city
Please enter your city: Austin
Please enter the two letter abbreviation for state: TX
Would you like to see the temperatures in Celsius or Fahrenheit, Enter 'C' or 'F': F
-----------------------------------------------------------------------------------------
The current temperature is 91°F
The 'feel like' temperature is 94°F
The low temperature is 86°F
The high temperature is 97°F
The pressure is 1015mb
The humidity is 44%
The weather description is: Scattered Clouds
-----------------------------------------------------------------------------------------
```

---

## 📂 File Overview

- `weather_app.py` – Main Python script

---

## 👨‍💻 Author

**Ruben Brionez Jr**  
Final Project – Week 12  
DSC 510 – Bellevue University

📅 **Date**: November 19, 2023

---

## 📃 License

This project is for educational purposes only.

