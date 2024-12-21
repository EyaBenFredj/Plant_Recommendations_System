from flask import Flask, request, jsonify, send_from_directory
import joblib
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
model_path = 'model/plant_care_model.pkl'
try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"Error loading model: {e}")

# Weather API configuration
WEATHER_API_KEY = "db01645cc60b4f989be205041242112"  # Replace with your actual API key
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

# Plant care details (mock data)
def get_plant_data(plant_name):
    plant_dataset = {
        "Aloe Vera": {"watering_frequency": 3, "light": "partial shade", "optimal_humidity": 40, "optimal_temperature": 25},
        "Fern": {"watering_frequency": 2, "light": "indirect sunlight", "optimal_humidity": 60, "optimal_temperature": 20},
        "Cactus": {"watering_frequency": 7, "light": "full sun", "optimal_humidity": 20, "optimal_temperature": 30},
    }
    return plant_dataset.get(plant_name)

@app.route('/')
def home():
    return '''
        <h1>Welcome to the Plant Care Recommendation API!</h1>
        <p>Use the following endpoints:</p>
        <ul>
            <li>/ui - Access the frontend user interface</li>
            <li>/predict - POST method to predict watering frequency</li>
            <li>/get_weather - GET method to fetch weather data by location</li>
            <li>/recommend - POST method to get plant care recommendations</li>
        </ul>
    '''

@app.route('/ui')
def serve_ui():
    return send_from_directory('.', 'index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        plant_name = data.get('plant_name')
        location = data.get('location')

        if not plant_name or not location:
            raise ValueError("Plant name and location are required.")

        plant_data = get_plant_data(plant_name)
        if not plant_data:
            return jsonify({"error": f"No care details found for plant: {plant_name}"})

        # Fetch weather data
        response = requests.get(
            WEATHER_API_URL,
            params={"key": WEATHER_API_KEY, "q": location}
        )
        weather_data = response.json()
        print("Weather API Response:", weather_data)  # Debugging line

        temperature = weather_data['current']['temp_c']
        humidity = weather_data['current']['humidity']

        # Generate recommendation
        watering_frequency = plant_data['watering_frequency']
        recommendation = f"Water every {watering_frequency} days."
        if temperature > 30 and humidity < 40:
            recommendation = "Due to hot and dry conditions, water more frequently."
        elif temperature < 10:
            recommendation = "Reduce watering. Plants need less water in cooler weather."

        return jsonify({
            "plant_name": plant_name,
            "location": location,
            "current_weather": {"temperature": temperature, "humidity": humidity},
            "plant_care_details": plant_data,
            "recommendation": recommendation,
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
