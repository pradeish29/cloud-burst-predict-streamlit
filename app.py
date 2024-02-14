# Import necessary libraries
import streamlit as st
import requests
import pandas as pd
import joblib
import bz2file as bz2
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define a function to fetch weather data from OpenWeather API
def fetch_weather_data(api_key, city_name):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    return data

# Define a function to preprocess weather data
def preprocess_weather_data(data):
    # Extract relevant features
    # You can extract more features as per your requirements
    weather = {
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'humidity': data['main']['humidity'],
        'pressure': data['main']['pressure'],
        'wind_speed': data['wind']['speed'],
        'clouds': (data['clouds']['all'])/10
    }

    temp_min = weather['temp_min']
    temp_max = weather['temp_max']
    humidity = weather['humidity']
    pressure = weather['pressure']
    wind_speed = weather['wind_speed']
    clouds = weather['clouds']

    input_data = pd.DataFrame({
    'temp_min': [temp_min],
    'temp_max': [temp_max],
    'wind_speed': [wind_speed],
    'humidity': [humidity],
    'pressure': [pressure],
    'clouds': [clouds]
})
    return input_data

# Main function to run the Streamlit app
def main():
    # Streamlit UI
    st.title('Cloudburst Prediction App')

    # Get user input for city name
    city_name = st.text_input('Enter City Name')

    # Check if user input is not empty
    if city_name:
        # Fetch weather data
        weather_data = fetch_weather_data('06f89bace216464eef97c0c210a1bc90', city_name)
        
        # Preprocess weather data
        processed_data = preprocess_weather_data(weather_data)

        # Show the fetched data
        st.write('**Fetched Weather Data:**')
        st.write(processed_data)

        # Load ML model
        # Assuming you have a trained model saved
        # Initialize your model
        # Load your trained model using joblib or pickle
        model = joblib.load(r'C:\Users\KAVIYA\OneDrive\Desktop\cloud\model.joblib')

        # Make predictions
        prediction = model.predict(processed_data)  # Pass processed data to the model

        # Display prediction
        st.write('**Prediction:**')
        st.write(prediction)

        if(prediction):
            st.write('**cloudburst**')
        else:
            st.write('**No cloudburst**')

# Run the main function
if __name__ == '__main__':
    main()

