# 🌱 PlantSync: Plant Care Recommendation System 🌱

Welcome to **PlantSync**, a comprehensive system designed to help you care for your plants by providing recommendations based on real-time weather data and plant-specific needs! This project integrates machine learning, APIs, and user-friendly web interfaces to deliver actionable advice. 🌍💧🌞

---

## 📖 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Datasets and Training](#datasets-and-training)
5. [Workflow](#workflow)
6. [Google Colab Notebook](#google-colab-notebook)
7. [Flask Web Application](#flask-web-application)
8. [How to Run](#how-to-run)
9. [Project Structure](#project-structure)
10. [Demo](#demo)
11. [API Endpoints](#api-endpoints)
12. [Contributing](#contributing)
13. [Acknowledgments](#acknowledgments)

---

## 🌟 Overview

**PlantSync** provides plant care recommendations by:
- Predicting watering frequency using machine learning.
- Fetching real-time weather data for your location.
- Combining plant-specific care details and environmental factors.

Whether you're caring for an Aloe Vera in London or a Cactus in Arizona, PlantSync has you covered!

---

## ✨ Features

1. **🌤️ Real-Time Weather Insights**:
   - Fetch live weather data from [WeatherAPI](https://www.weatherapi.com/).
2. **🌱 Plant Care Recommendations**:
   - Receive tailored advice for your specific plant and location.
3. **🖥️ Interactive User Interface**:
   - Input your plant name and location to get immediate advice.
4. **🤖 Machine Learning Integration**:
   - Predict watering frequency using a Random Forest model.
5. **🌐 RESTful API**:
   - Easy-to-use API endpoints for programmatic access.

---

## 🛠️ Technologies Used

- **Google Colab**: For training and evaluating the machine learning model.
- **Flask**: Backend for APIs and the web interface.
- **WeatherAPI**: For real-time weather data.
- **HTML/CSS/JavaScript**: For the front-end interface.
- **Python (joblib)**: For saving and loading the trained model.

---

## 📂 Datasets and Training

### Dataset
The model was trained using synthetic environmental data:
- **Features**:
  - Brightness
  - Temperature
  - Soil Humidity
- **Target**:
  - Watering Frequency (days between watering)

### Model Training
The training process was conducted in the Google Colab notebook:
- **Model Used**: Random Forest Regressor.
- **Metrics**: Root Mean Square Error (RMSE).

The dataset and model are saved as `plant_care_model.pkl` and included in this repository.

---

## 🧩 Workflow

1. **User Input**:
   - The user provides the plant name and location via the web interface.
2. **Weather Fetching**:
   - The system retrieves real-time weather data using WeatherAPI.
3. **Model Prediction**:
   - Using brightness, temperature, and soil humidity, the system predicts watering frequency.
4. **Plant-Specific Recommendations**:
   - The system combines weather data, model predictions, and plant care specifics to generate actionable advice.
5. **User Output**:
   - Recommendations are displayed on the web interface.

---

## 📘 Google Colab Notebook

The project began with the **PlantSync.ipynb** notebook, where the machine learning model was trained. It contains:
1. **Data Preprocessing**: Normalization and feature engineering.
2. **Model Training**: Training a Random Forest model.
3. **Model Evaluation**: Computing RMSE and visualizing predictions.

📂 **Notebook Name**: `PlantSync.ipynb`  
📎 [Open in Google Colab](https://colab.research.google.com/github/your-username/plantsync/blob/main/PlantSync.ipynb)

---

## 🌐 Flask Web Application

The Flask app provides:
1. **Interactive Front-End**:
   - A user-friendly interface to enter plant names and locations.
2. **REST API Endpoints**:
   - `/predict`: Predict watering frequency based on environmental data.
   - `/get_weather`: Retrieve live weather data.
   - `/recommend`: Provide plant care recommendations by combining weather and plant-specific data.

---

## 🚀 How to Run

### Prerequisites
- Python 3.7+
- Flask and Python libraries (see `requirements.txt`).
- WeatherAPI Key ([Get Yours](https://www.weatherapi.com/)).

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/plantsync.git
   cd plantsync
Install Dependencies:

bash
Copier le code
pip install -r requirements.txt
Run the Application:

bash
Copier le code
python app.py
Access the Web Interface: Visit http://127.0.0.1:5000/ui in your browser.
### Complete README.md Content for **PlantSync** Project

```markdown


2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Web Interface**:
   Visit `http://127.0.0.1:5000/ui` in your browser.

---

## 📂 Project Structure

```
plantsync/
│
├── app.py                # Flask application
├── index.html            # Front-end interface
├── plant_care_model.pkl  # Trained machine learning model
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── PlantSync.ipynb       # Google Colab notebook
```

---

## 🎥 Demo

### Example: Aloe Vera in London
1. Enter `Aloe Vera` and `London` into the web interface.
2. Click **Get Recommendation**.
3. Output:
   - Weather: 7.5°C, 74% humidity.
   - Recommendation: "Reduce watering. Plants need less water in cooler weather."

---

## 📊 API Endpoints

1. **`/predict`**:
   - **Method**: `POST`
   - **Input**:
     ```json
     {
         "brightness": 0.5,
         "temperature": -1.2,
         "solHumidity": 0.8
     }
     ```
   - **Response**:
     ```json
     {
         "watering_frequency": 3
     }
     ```

2. **`/get_weather`**:
   - **Method**: `GET`
   - **Input**:
     ```
     ?location=London
     ```
   - **Response**:
     ```json
     {
         "temperature": 7.5,
         "humidity": 74
     }
     ```

3. **`/recommend`**:
   - **Method**: `POST`
   - **Input**:
     ```json
     {
         "plant_name": "Aloe Vera",
         "location": "London"
     }
     ```
   - **Response**:
     ```json
     {
         "recommendation": "Reduce watering. Plants need less water in cooler weather.",
         "weather": {
             "temperature": 7.5,
             "humidity": 74
         },
         "plant_care_details": {
             "light": "partial shade",
             "optimal_humidity": 40,
             "optimal_temperature": 25,
             "watering_frequency": 3
         }
     }
     ```

---

## 🤝 Contributing

Feel free to fork the repository, submit a pull request, or open issues. Contributions are always welcome! 🌟

---

## ⚡ Acknowledgments

- **Google Colab** for machine learning experimentation.
- **WeatherAPI** for real-time weather data.
- **Flask** for enabling a seamless web application.

🌱 **Happy Gardening!** 🌿
```

This README.md file is fully comprehensive, combining details from Google Colab, Flask API, and the user interface. Copy-paste it directly into your repository's README.md file!
