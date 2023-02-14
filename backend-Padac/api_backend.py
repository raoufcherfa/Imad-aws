from flask import Flask, jsonify
import uuid

app = Flask(__name__)

employees = [
        {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
        {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
        {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
    ]

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

@app.route('/api/v1/employees', methods=['POST'])
def create_employee():
    new_employee = request.get_json()
    new_employee['id'] = str(uuid.uuid4())
    employees.append(new_employee)
    return jsonify(new_employee), 201
    
@app.route('/api/v1/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    global employe
    employe = [employee for employee in employees if employee.get('id') == id]
    return jsonify(employe), 200

        

if __name__ == '__main__':
    app.run(debug=True, port=8080)
