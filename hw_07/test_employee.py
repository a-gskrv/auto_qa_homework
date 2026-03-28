from pprint import pprint

from employee import EmployeeApi


base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

def test_create_employee():
    employee_json = {
            "first_name": "Albert",
            "last_name": "last_name",
            "middle_name": "middle_name",
            "company_id": 5,
            "email": "albert@example.com",
            "phone": "string",
            "birthdate": "1984-04-17",
            "is_active": True
    }

    new_emp= api.create_employ(data_json=employee_json)

    pprint(new_emp)
    assert new_emp.get("first_name") == "Albert"



def test_get_employee():

    employee_info = api.get_employee_by_id(2)

    assert employee_info["first_name"] == "Сергей"


def test_edit_employee():
    employee_info = api.edit_employee(
        user="harrypotter",
        password="expelliarmus",
        employee_id=2,
        new_last_name="Albert_edit",
        new_email="albert_edit@albert.com",
        new_phone="asdf"
    )

    assert employee_info["last_name"] == "Albert_edit"