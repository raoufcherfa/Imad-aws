import json
import unittest
from app import app, employees


class TestApp(unittest.TestCase):

    def test_get_employees(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(json.loads(response.data), employees)

    def test_add_employee(self):
        tester = app.test_client(self)
        new_employee = {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'}
        response = tester.post('/api/v1/employees', json=new_employee)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(json.loads(response.data), new_employee)

    def test_get_employee_by_id(self):
        tester = app.test_client(self)
        employee_id = 0
        response = tester.get(f'/api/v1/employees/{employee_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(json.loads(response.data), [])

    def test_delete_employee(self):
        tester = app.test_client(self)
        employee_id = 1
        response = tester.delete(f'/api/v1/employees/{employee_id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(json.loads(response.data), {'message': f'Employee with ID {employee_id} deleted'})
        self.assertNotIn(employees[1], employees)

    def test_update_employee(self):
        tester = app.test_client(self)
        employee_id = 1
        updated_employee = {'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'}
        response = tester.put(f'/api/v1/employees/{employee_id}', json=updated_employee)
        self.assertEqual(response.status_code, 200) 
      
if __name__ == '__main__':
    unittest.main()