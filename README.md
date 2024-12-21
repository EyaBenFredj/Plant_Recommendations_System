# 🌱 Plant Care Recommendation System 🌱

Welcome to the **Plant Care Recommendation System**! This project provides actionable plant care advice by combining machine learning predictions, real-time weather data, and plant-specific care details. 🌍💧🌞

---

## 📖 Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Google Colab Notebook](#google-colab-notebook)
5. [Flask Web Application](#flask-web-application)
6. [How to Run](#how-to-run)
7. [Demo](#demo)
8. [Project Structure](#project-structure)
9. [Contributing](#contributing)

---

## 🌟 Overview

This system integrates:
- A machine learning model predicting watering frequency.
- WeatherAPI to fetch real-time weather data.
- A web-based interface for user interaction.

The goal is to help plant enthusiasts take better care of their plants by combining data science and environmental context.

---

## ✨ Features

1. **Real-Time Weather Insights**:
   - Fetch live weather data for any location using WeatherAPI.
2. **Plant Care Recommendations**:
   - Suggest watering schedules and care advice tailored to specific plants.
3. **Interactive User Interface**:
   - Built with Flask, HTML, CSS, and JavaScript for simplicity and ease of use.
4. **Machine Learning Integration**:
   - Predict watering frequency based on environmental inputs.

---

## 🛠️ Technologies Used

- **Google Colab**: For model training and experimentation.
- **Flask**: Backend for serving APIs and the web interface.
- **WeatherAPI**: For real-time weather data.
- **HTML/CSS/JavaScript**: For the front-end interface.
- **Python (joblib)**: For saving and loading the trained model.

---

## 📘 Google Colab Notebook

The project started with a Google Colab notebook to:
1. **Preprocess Data**: Clean, transform, and prepare plant and weather data.
2. **Train the Model**: Develop and save a Random Forest model.
3. **Evaluate Results**: Validate the model using RMSE and other metrics.

📂 **Notebook Name**: `plant_care_system.ipynb`  
📎 [Open in Google Colab](https://colab.research.google.com/github/your-username/plant-care-recommendation-system/blob/main/PlantSync.ipynb)

---

## 🌐 Flask Web Application

The Flask app serves as the core of the system:
1. **Endpoints**:
   - `/predict`: Predicts watering frequency.
   - `/get_weather`: Retrieves real-time weather data for a location.
   - `/recommend`: Combines plant data and weather info to provide care recommendations.
2. **Web Interface**:
   - Allows users to input plant names and locations to get tailored advice.

---

## 🚀 How to Run

### Prerequisites

- Python 3.7 or higher.
- Flask and Python libraries (see `requirements.txt`).
- WeatherAPI Key ([Get Yours](https://www.weatherapi.com/)).

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/plant-care-recommendation-system.git
   cd plant-care-recommendation-system
