from flask import Flask, jsonify

app = Flask(__name__)


employees = [
        {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
        {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
        {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
    ]

@app.route('/api/v1/employees', methods=['GET'])
def get_employees():
    
    return jsonify(employees)

if __name__ == '__main__':
    app.run(debug=True, port=8080)


# Définition de la route pour créer un nouvel employé
@app.route('/api/v1/employees', methods=['POST'])
def create_employee():
    # Extraction des données du corps de la requête
    employee_data = request.get_json()
    new_employee = {
        'id': employee_data['id'],
        'firstname': employee_data['firstname'],
        'lastname': employee_data['lastname'],
        'email': employee_data['email']
    }

    # Ajout du nouvel employé à la liste des employés
    employees.append(new_employee)

    # Envoi de la réponse HTTP
    return jsonify({'success': True, 'message': 'Employee created successfully', 'data': new_employee}), 201