from fastapi import FastAPI
from typing import Union
from routes.user import user
from modelss import Employee

from mongoengine import connect
import json



app = FastAPI()
connect(db="hrms", host="localhost", port=27017)



@app.get("/")
def home():
    return {"message":"Hello World!"}


@app.get("/get_all_employees")
def get_all_employees():
    employees= json.loads(Employee.objects().to_json())
    return {"employees": employees}
from fastapi import Path

@app.get("/get_employee/{emp_id}")
def get_employee(emp_id: int = Path(...,gt=0)):
    employee = Employee.objects.get(emp_id=emp_id)
    employee_dic= {
        "emp_id": employee.emp_id,
        "name": employee.name,
        "age": employee.age,
        "teams": employee.teams
    }
    print(employee_dic)
    return employee_dic
