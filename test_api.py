import requests

BASE_URL = "http://127.0.0.1:5000"

# Test /predict endpoint (POST request)
def test_predict():
    print("\nTesting /predict endpoint...")
    payload = {"brightness": 0.5, "temperature": -1.2, "solHumidity": 0.8}
    response = requests.post(f"{BASE_URL}/predict", json=payload)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Test /get_weather endpoint (GET request)
def test_get_weather():
    print("\nTesting /get_weather endpoint...")
    location = "London"
    response = requests.get(f"{BASE_URL}/get_weather", params={"location": location})
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

# Test /recommend endpoint (POST request)
def test_recommend():
    print("\nTesting /recommend endpoint...")
    payload = {"plant_name": "Aloe Vera", "location": "London"}
    response = requests.post(f"{BASE_URL}/recommend", json=payload)
    if response.status_code == 200:
        print("Response:", response.json())
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    test_predict()
    test_get_weather()
    test_recommend()
