# Cloud Burst Prediction using Random Forest Model

## Overview
This project aims to predict cloud burst occurrences using a Random Forest model deployed via a Streamlit web application. The model utilizes real-time weather data from OpenWeather.org, allowing users to input a city name to retrieve relevant weather information and receive a prediction output.

## Deployment
this project has been deployed using streamlit cloud.

https://cloud-burst-prediction.streamlit.app/

## Page view
![Streamlit Page](https://github.com/pradeish29/cloud-burst-predict/blob/main/Streamlit_page.jpg)

## Features
- **Real-time Weather Data**: Integration with OpenWeather.org provides up-to-date weather information.
- **User-Friendly Interface**: Streamlit app allows users to easily input city names and view prediction outputs.
- **Random Forest Model**: Utilizes a trained Random Forest model to predict cloud burst occurrences based on weather data.

## Usage
To use the application:
1. Clone the repository to your local machine.
2. Install the necessary dependencies using `pip install streamlit joblib requests bz2file`.
3. Check and modify the path for certain files in the code
4. Run the `model.ipynb` file 
5. Run the Streamlit app by executing `streamlit run app.py` in your terminal.
6. Access the app via the provided local URL in your browser.
7. Enter a city name to retrieve weather data and receive the cloud burst prediction output.

## File Structure
- `app.py`: Streamlit application script.
- `model.ipynb`: Pre-trained Random Forest model for cloud burst prediction.

## Data Sources
- [OpenWeather.org](https://openweathermap.org/): Provides real-time weather data.

## Credits
- **Developed by**: Pradeish Misara 


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.



Feel free to customize this template further according to your project's needs!
