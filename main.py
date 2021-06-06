"""
    This is the follow along from '100 Days of Code - The Complete Python Pro Bootcamp for 2021'
    By: Angela Yu

    Student: Jason Smith
    Date/Time: 6/6/2021 10:55 AM
"""

import requests
from datetime import datetime

USERNAME = "huchknows"
TOKEN = "d80sdk329d14"
GRAPH_ID = "graph1"

today = datetime.now()

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

"""CREATE A PIXELA USER"""
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

"""CREATE A NEW GRAPH FOR THE NEWLY CREATED USER"""
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74",
}

"""CREATE A PIXEL"""
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


def edit_pixel():
    """edits pixel based on date supplied by user input"""
    date = input("Enter the date that you would like to edit(yyyyMMdd): ")
    quantity = input("Enter the updated quantity: ")
    pixel_edit_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

    pixel_edit_data = {
        "quantity": quantity
    }

    return requests.put(url=pixel_edit_endpoint, json=pixel_edit_data, headers=headers)


print(edit_pixel())
