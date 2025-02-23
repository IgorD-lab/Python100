import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

# Load environment variables
load_dotenv()

# API Configuration
class WeatherNotifier:
    def __init__(self):
        # OpenWeatherMap configuration
        self.WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
        self.OMW_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
        
        # Twilio configuration
        self.TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
        self.TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
        
        # Location coordinates (Novi Sad, Serbia)
        self.LAT = 45.240372
        self.LONG = 19.711800

    def get_weather_data(self):
        """
        Fetch weather data from OpenWeatherMap API
        
        Returns:
            dict: Weather data JSON response
        """
        weather_params = {
            "lat": self.LAT,
            "lon": self.LONG,
            "appid": self.WEATHER_API_KEY,
        }
        
        try:
            response = requests.get(self.OMW_ENDPOINT, params=weather_params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None

    def check_rain(self, weather_data):
        """
        Check if it's raining
        
        Args:
            weather_data (dict): Weather data from API
        
        Returns:
            bool: True if it's raining, False otherwise
        """
        if not weather_data or 'weather' not in weather_data:
            return False
        
        current_weather = weather_data['current']['weather'][0]['main']
        return current_weather == "Rain"

    def send_rain_sms(self, from_number, to_number):
        """
        Send SMS if it's raining
        
        Args:
            from_number (str): Twilio phone number
            to_number (str): Recipient phone number
        """
        weather_data = self.get_weather_data()
        
        if self.check_rain(weather_data):
            try:
                client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)
                message = client.messages.create(
                    body="The hail of heavens tears is attempting to flood the world today. Be prepared. Bring an umbrella ☔️. - 34Weather Forecast",
                    from_=from_number,
                    to=to_number,
                )
                print("Rain SMS sent successfully!")
            except Exception as e:
                print(f"Error sending SMS: {e}")

def main():
    # TODO: Replace with actual Twilio and recipient phone numbers
    notifier = WeatherNotifier()
    notifier.send_rain_sms(
        from_number="YOUR TWILIO PHONE NUMBER", 
        to_number="RECIPIENT PHONE NUMBER"
    )

if __name__ == "__main__":
    main()