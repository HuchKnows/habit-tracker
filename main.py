"""
    This is the follow along from '100 Days of Code - The Complete Python Pro Bootcamp for 2021'
    By: Angela Yu

    Student: Jason Smith
    Date/Time: 6/6/2021 10:55 AM
"""

import requests
from datetime import datetime

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

today = datetime.now()
headers = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    """create new Pixela user"""
    print("Create User Selected...")
    user_params = {
        "token": input("Token: "),
        "username": input("Username: "),
        "agreeTermsOfService": input("Agree to terms of service?(Yes or No) "),  # yes
        "notMinor": input("Do you agree that you're not a minor?(Yes or No) "),  # yes
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    return response.text


def create_graph():
    """create new Pixela graph"""
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai",
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    return response.text


def create_pixel():
    """create a new pixel"""
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": "20210605",
        "quantity": "9.74",
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    return response.text


def edit_pixel():
    """edits pixel based on date supplied by user input"""
    date = input("Enter the date that you would like to edit(yyyyMMdd): ")
    quantity = input("Enter the updated quantity: ")
    pixel_edit_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    pixel_edit_data = {"quantity": quantity}
    response = requests.put(url=pixel_edit_endpoint, json=pixel_edit_data, headers=headers)
    return response.text


def delete_pixel():
    """deletes a pixel based on date supplied by user input"""
    date = input("Enter the date that you would like to delete(yyyyMMdd): ")
    pixel_deletion_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    response = requests.delete(url=pixel_deletion_endpoint, headers=headers)
    return response.text


def menu():
    """main menu"""
    sel = input("Jason's Pixel console. Please make a selection\n"
                "\t1. Create a user.\n"
                "\t2. Create a graph.\n"
                "\t3. Create a pixel.\n"
                "\t4. Update a pixel.\n"
                "\t5. Delete a pixel.\n"
                "\t6. Quit\n")
    sel = int(sel)
    if sel == 1:
        print(f"Sel: {sel}")
        return create_user()
    elif sel == 2:
        return f"Sel: {sel}", create_graph()
    elif sel == 3:
        return f"Sel: {sel}", create_pixel()
    elif sel == 4:
        return f"Sel: {sel}", edit_pixel()
    elif sel == 5:
        return f"Sel: {sel}", delete_pixel()
    elif sel == 6:
        return f"Sel: {sel}", quit()


menu()
