# import requests

# SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f2b4e430735a0e15c01f45cdb64ef9a5/tableFlightDeals/prices"

# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     def __init__(self):
#         self.destination_data = {}
        
#     def get_destination_data(self):
#         """Gets the data from the Google Sheet"""
#         response = requests.get(url=SHEETY_PRICES_ENDPOINT)
#         data = response.json()
#         self.destination_data = data["prices"]
#         return self.destination_data
    
#     def get_destination_data_mock(self):
#         data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Frankfurt', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Hong Kong', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Dublin', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]
#         return data
    
#     def update_destination_code(self):
#         """Updates the IATA code in the Google Sheet"""
#         for city in self.destination_data:
#             new_data = {
#                 "price": {
#                     "iataCode": city["iataCode"]
#                 }
#             }
#             response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
#             print(response.text)