import requests
import datetime
from twilio.rest import Client

# Mock data for testing (api limit can be exceeded quickly) uncomment return of MOCK_STOCK_DATA in get_stock_data method to use it.
MOCK_STOCK_DATA = {
    "Time Series (Daily)": {
        "2025-02-21": {
            "4. close": "800.00"
        },
        "2025-02-20": {
            "4. close": "750.00"
        }
    }
}

# ! Constants and API keys
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


class StockAPI:
    '''Class to fetch stock data from Alpha Vantage and check price change.'''

    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = STOCK_ENDPOINT

    def get_stock_data(self):
        """Fetch stock data from Alpha Vantage."""
        stock_params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": COMPANY_NAME,
            "apikey": self.api_key
        }
        response = requests.get(url=self.endpoint, params=stock_params)
        response.raise_for_status()
        print("Full response (STOCKS): " + response.url)
        # return MOCK_STOCK_DATA
        return response.json()

    def check_price_change(self):
        """Return percentage difference between yesterday's and day before yesterday's closing price."""
        data = self.get_stock_data()

        # Check if the required data is present
        if "Time Series (Daily)" not in data:
            print("API call limit reached or data not available. Using mock data.")
            data = MOCK_STOCK_DATA

        # Get yesterday's and day before yesterday's data
        data_list = [value for (key, value) in data["Time Series (Daily)"].items()]
        yesterday_data = data_list[0]
        day_before_yesterday_data = data_list[1]

        # Get yesterday's and day before yesterday's closing price
        yesterday_closing_price = float(yesterday_data["4. close"])
        day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

        # Subtract the closing prices and return the difference in percentage
        difference = yesterday_closing_price - day_before_yesterday_closing_price
        diff_percent = round((difference / yesterday_closing_price) * 100)

        print(diff_percent, "%")
        return diff_percent


class NewsAPI:
    '''Class to fetch news.'''
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = NEWS_ENDPOINT

    def get_news_data(self):
        """Fetch news data from NewsAPI."""
        news_params = {
            "apiKey": self.api_key,
            "q": COMPANY_NAME,
        }
        response = requests.get(url=self.endpoint, params=news_params)
        response.raise_for_status()
        print("Full response (NEWS): " + response.url)
        return response.json()

    def get_news_articles(self):
        """Return the first 3 news articles."""
        data = self.get_news_data()
        articles = data["articles"]

        return articles[:3]

    def send_sms(self, stock_change):
        """Send SMS with the articles to the user using TWILIO."""
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        articles = self.get_news_articles()

        # Variables for formatting the message
        up_down = "🔺" if stock_change > 0 else "🔻"

        for article in articles:
            message = client.messages.create(
                body=f"{STOCK_NAME}: {up_down}{stock_change}%\nHeadline: {article['title']}. \nBrief: {article['description']}",
                from_=f"{VIRTUAL_TWILIO_NUMBER}",
                to=f"{VERIFIED_NUMBER}"
            )
            print(message.status)


def main():
    # Initialize API clients
    stock_api = StockAPI(api_key=STOCK_API_KEY)
    news_api = NewsAPI(api_key=NEWS_API_KEY)
    stock_change = stock_api.check_price_change()

    # Check if the stock price has changed by 5%
    if abs(stock_change) >= 5:
        news_api.send_sms(stock_change=stock_change)
    else:
        print("No significant price change.")


if __name__ == "__main__":
    main()
