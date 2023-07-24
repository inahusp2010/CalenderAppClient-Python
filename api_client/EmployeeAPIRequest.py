import requests
from model import Employee

def add_employee(employee):
    employee_json=employee.object_to_json()
    headers = {'Content-type': 'application/json'}
    response=requests.post("http://localhost:8080/employee", headers=headers, data=employee_json)
    print(response.json())
def remove_employee(id):
    response=requests.delete("http://localhost:8080/employee/"+str(id))
    print(response.json())
def get_all_employees():
    response=requests.get("http://localhost:8080/employee")
    print(response.json())
def get_employee_by_email(email):
    response=requests.get("http://localhost:8080/employee/"+email)
    print(response.json())
def update_employee_details(id,employee):
    employee_json = employee.object_to_json()
    headers = {'Content-type': 'application/json'}
    response = requests.put("http://localhost:8080/employee/"+str(id), headers=headers, data=employee_json)
    print(response.json())
def employee_api(operation):
    if(operation == 1):
        name=input("Name : ")
        email=input("Email : ")
        officeId=int(input("Office Id : "))
        dob=input("DOB : ")
        emp= Employee.Employee(name=name, email=email, officeId=officeId, dob=dob)
        add_employee(emp)
    elif(operation == 2):
        id=int(input("Employee Id : "))
        remove_employee(id)
    elif(operation == 3):
        get_all_employees()
    elif(operation == 4):
        email = int(input("Employee email : "))
        get_employee_by_email(email)
    elif(operation == 5):
        id=int(input("Employee Id : "))
        name = input("Name : ")
        email = input("Email : ")
        officeId = int(input("Office Id : "))
        dob = input("DOB : ")
        emp = Employee.Employee(name=name, email=email, officeId=officeId, dob=dob)
        update_employee_details(id, emp)