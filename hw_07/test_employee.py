from pprint import pprint

from employee import EmployeeApi


base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)
def test_create_employee():
    employee_json = {
            "first_name": "Albert",
            "last_name": "last_name",
            "middle_name": "string",
            "company_id": 29,
            "email": "user@example.com",
            "phone": "string",
            "birthdate": "2026-03-18",
            "is_active": True
    }

    # api = EmployeeApi(base_url)  # Инициализация API-клиента
    # 1.
    new_emp= api.create_employ(data_json=employee_json)

    # print(emp_before.get("id"))
    pprint(new_emp)
    assert new_emp.get("first_name") == "Albert"
    # assert new_emp.get("last_name") == "last_name"

    # assert

    # 2. Создаём новую компанию

def test_get_employee():

    employee_info = api.get_employee_by_id(1)

    assert employee_info["first_name"] == "Иван"


def test_edit_employee():
    employee_info = api.edit_employee(
        user="harrypotter",
        password="expelliarmus",
        employee_id=17,
        new_last_name="Albert_edit",
        new_email="Albert_edit",
        new_phone="asdf",
        new_is_active="true"
    )

    assert employee_info["last_name"] == "Albert_edit"