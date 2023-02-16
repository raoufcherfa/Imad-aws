import json
import pytest

from app import app, employees


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_employees(client):
    response = client.get('/api/v1/employees')
    assert response.status_code == 200
    assert len(response.json) == len(employees)


def test_add_employee(client):
    new_employee = {'firstName': 'Mark', 'lastName': 'Johnson', 'emailId': 'markjohnson@example.com'}
    response = client.post('/api/v1/employees', json=new_employee)
    assert response.status_code == 201
    assert response.json['id'] == len(employees) + 1
    assert response.json['firstName'] == new_employee['firstName']


def test_delete_employee(client):
    employee_id = 1
    response = client.delete(f'/api/v1/employees/{employee_id}')
    assert response.status_code == 200
    assert len(employees) == 2
    assert all(employee['id'] != employee_id for employee in employees)


def test_update_employee(client):
    employee_id = 1
    updated_employee = {'firstName': 'Mark', 'lastName': 'Johnson', 'emailId': 'markjohnson@example.com'}
    response = client.put(f'/api/v1/employees/{employee_id}', json=updated_employee)
    assert response.status_code == 200
    assert response.json['id'] == employee_id
    assert response.json['firstName'] == updated_employee['firstName']