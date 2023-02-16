from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

employees = [
        {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
        {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
        {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'},
        {'id': 4, 'firstName': 'raouf', 'lastName': 'pa', 'emailId': 'raoufpa@example.com'}
    ]

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)


@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"name": "John", "age": 30, "city": "New York"}
    return jsonify(data)

@app.route('/api/v1/employees', methods=['POST'])
def add_employee():
    new_employee = request.get_json()
    employees.append(new_employee)
    return jsonify(new_employee)
    
    
@app.route('/api/v1/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    global employe
    employe = [employee for employee in employees if employee.get('id') == id]
    return jsonify(employe), 200

@app.route('/api/v1/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    for employee in employees:
        if employee['id'] == id:
            employees.remove(employee)
            return jsonify({'message': f'Employee with ID {id} deleted'}), 200
    return jsonify({'message': f'No employee with ID {id} found'}), 404


@app.route('/api/v1/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    for employee in employees:
        if employee['id'] == employee_id:
            updated_employee = request.get_json()
            employee.update(updated_employee)
            return jsonify(employee)
    return jsonify({'error': 'Employé non trouvé'}), 404



if __name__ == '__main__':
    app.run(debug=True)
