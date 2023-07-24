import requests
from api_client import OfficeAPIRequest,EmployeeAPIRequest

def main():
    choice=int(input("Enter Choice :\n1-Employee\n2-Office\n3-Meeting-Room\n4-Meeting\n"))
    if(choice==1):
        operation=int(input("Select Operation :\n1-Add Employee\n2-Remove Employee\n3-Get All Employees\n4-Get Employee By Email\n5-Update Employee Details\n"))
        EmployeeAPIRequest.employee_api(operation)
    elif(choice==2):
        operation = int(input(
            "Select Operation :\n1-Add Office\n2-Remove Office\n3-Get All Offices\n4-Get Office By ID\n5-Update Office Details\n"))
        OfficeAPIRequest.office_api(operation)
    elif(choice==3):
        operation = int(input(
            "Select Operation :\n1-Add Meeting-Room\n2-Remove Meeting-Room\n3-Get All Meeting-Room\n4-Get Meeting-Room By ID\n5-Update Meeting-Room Details\n"))
    elif(choice==4):
        operation = int(input(
            "Select Operation :\n1-Schedule Meeting\n2-Cancel Meeting\n3-Get All Meetings By Host\n4-Get Meeting Details\n"))
    else:
        print("You might have entered Incorrect Choice")

if __name__ == "__main__":
    main()