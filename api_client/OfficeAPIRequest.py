import requests
from model import Office

def add_office(office):
    office_json=office.object_to_json()
    headers = {'Content-type': 'application/json'}
    response=requests.post("http://localhost:8080/office",headers=headers,data=office_json)
    print(response.json())
def remove_office(id):
    response=requests.delete("http://localhost:8080/office/"+str(id))
    print(response.json())
def get_all_offices():
    response=requests.get("http://localhost:8080/office")
    print(response.json())
def get_office_by_id(id):
    response=requests.get("http://localhost:8080/office/"+str(id))
    print(response.json())
def update_office_details(id,office):
    office_json = office.object_to_json()
    headers = {'Content-type': 'application/json'}
    response = requests.put("http://localhost:8080/office/"+str(id), headers=headers, data=office_json)
    print(response.json())
def office_api(operation):
    if(operation == 1):
        name=input("Office Name : ")
        location=input("Office Location : ")
        total_rooms=int(input("Total Rooms : "))
        of1= Office.Office(name, location, total_rooms)
        add_office(of1)
    elif(operation == 2):
        id=int(input("Office Id : "))
        remove_office(id)
    elif(operation == 3):
        get_all_offices()
    elif(operation == 4):
        id = int(input("Office Id : "))
        get_office_by_id(id)
    elif(operation == 5):
        id=int(input("Office Id : "))
        name = input("Office Name : ")
        location = input("Office Location : ")
        total_rooms = int(input("Total Rooms : "))
        of1 = Office.Office(name, location, total_rooms)
        update_office_details(id,of1)