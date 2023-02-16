import unittest
import json
from mp import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.employees = [
            {'id': 1, 'firstName': 'John', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'},
            {'id': 2, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'},
            {'id': 3, 'firstName': 'Bob', 'lastName': 'Johnson', 'emailId': 'bobjohnson@example.com'}
        ]

    def test_get_employees(self):
        response = self.client.get('/api/v1/employees')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), self.employees)

    def test_add_employee(self):
        new_employee = {'firstName': 'Alice', 'lastName': 'Smith', 'emailId': 'alicesmith@example.com'}
        response = self.client.post('/api/v1/employees', json=new_employee)
        self.assertEqual(response.status_code, 201)
        self.assertIn(new_employee, self.employees)

    def test_delete_employee(self):
        employee_id = 2
        response = self.client.delete(f'/api/v1/employees/{employee_id}')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn({'id': employee_id, 'firstName': 'Jane', 'lastName': 'Smith', 'emailId': 'janesmith@example.com'}, self.employees)

    def test_update_employee(self):
        employee_id = 1
        updated_employee = {'firstName': 'Johnny', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'}
        response = self.client.put(f'/api/v1/employees/{employee_id}', json=updated_employee)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'id': employee_id, 'firstName': 'Johnny', 'lastName': 'Doe', 'emailId': 'johndoe@example.com'})

if __name__ == '__main__':
    unittest.main()