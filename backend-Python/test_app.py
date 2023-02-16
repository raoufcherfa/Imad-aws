import json
import unittest
from PJ_api_backend import app, employees


class TestAPI(unittest.TestCase):
    # Test GET /api/v1/employees
    def test_get_employees(self):
        with app.test_client() as client:
            response = client.get('/api/v1/employees')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), len(employees))

    # Test POST /api/v1/employees
    def test_add_employee(self):
        new_employee = {
            "firstName": "PJ",
            "lastName": "DACOSTA",
            "emailId": "PJ.DACOSTA@gmail.com"
        }
        with app.test_client() as client:
            response = client.post('/api/v1/employees', json=new_employee)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['firstName'], new_employee['firstName'])
            self.assertEqual(response.json['lastName'], new_employee['lastName'])
            self.assertEqual(response.json['emailId'], new_employee['emailId'])

    # Test PUT /api/v1/employees/:employee_id
    def test_update_employee(self):
        employee_id = 1
        updated_employee = {
            "firstName": "Mathieu",
            "lastName": "Perotti",
            "emailId": "Mathieu.Perotti@icloud.com"
        }
        with app.test_client() as client:
            response = client.put(f'/api/v1/employees/{employee_id}', json=updated_employee)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['firstName'], updated_employee['firstName'])
            self.assertEqual(response.json['lastName'], updated_employee['lastName'])
            self.assertEqual(response.json['emailId'], updated_employee['emailId'])

    # Test DELETE /api/v1/employees/:employee_id
    def test_delete_employee(self):
        employee_id = 2
        with app.test_client() as client:
            response = client.delete(f'/api/v1/employees/{employee_id}')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['message'], 'Employee has been deleted')
            self.assertIsNone(next((employee for employee in employees if employee['id'] == employee_id), None))

if __name__ == '__main__':
    unittest.main()