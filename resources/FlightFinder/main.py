 #! API Broken going to remake it once a new API is available
 
# import pprint


# from flight_search import FlightSearch
# from data_manager import DataManager
# from flight_data import FlightData
# from notification_manager import NotificationManager


# #This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# data_manager = DataManager()
# flight_search = FlightSearch()
# flight_data = FlightData()
# notification_manager = NotificationManager()

# # Get google sheet data
# sheet_data = data_manager.get_destination_data_mock()

# if sheet_data[0]["iataCode"] == "":
#     for destination in sheet_data:
#         destination["iataCode"] = flight_search.get_iata_code(destination["city"])
    
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_code()
