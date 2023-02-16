from flask import Flask, jsonify, request
import json
import pytest

from app import app, employees

app = Flask(__name__)

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

employees = [
    {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
    {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
    {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
]

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/api/v1/employees', methods=['POST'])
def add_employee():
    new_employee = request.json
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201

@app.route('/api/v1/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employees.remove(employee)
            return jsonify({'message': 'Employee has been deleted'}), 200
    return jsonify({'error': 'Employee not found'}), 404

@app.route('/api/v1/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            employee.update(request.json)
            return jsonify(employee), 200
    return jsonify({'error': 'Employee not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8080)