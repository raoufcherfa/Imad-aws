from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    employees = [
        {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
        {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
        {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
    ]
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
@app.route('/api/v1/employees', methods=['POST'])

def add_employee():
    new_employee = request.json
    new_employee['id'] = len(employees) + 1
    employees.append(new_employee)
    return jsonify(new_employee), 201


