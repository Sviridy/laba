from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from department_app.models import Department, Positions, Specialization, Employee


class DepartmentTests(APITestCase):
    def setUp(self):
        self.department = Department.objects.create(department='Developer')
        self.specialization = Specialization.objects.create(name='Python')
        self.positions1 = Positions.objects.create(name='Student')
        self.positions2 = Positions.objects.create(name='Senior')
        self.employee1 = Employee.objects.create(name='Svirydzetski Kanstantsin', date_of_birth='1998-05-05',
                                                 department=self.department, positions=self.positions1,
                                                 specialization=self.specialization,
                                                 experience=1, wages=10)
        self.employee2 = Employee.objects.create(name='Ihar Nauros', date_of_birth='1990-01-01',
                                                 department=self.department, positions=self.positions2,
                                                 specialization=self.specialization,
                                                 experience=15, wages=1500)

    def test_list_department(self):
        response = self.client.get(reverse('department-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[-1].get('department'), 'Developer')

    def test_create_department(self):
        url = reverse('department-list')
        data = {'department': 'hi'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json().get('department'), 'hi')

    def test_number_of_employees(self):
        """Test method"""
        self.assertEqual(self.department.number_of_employees, 2)

    def test_the_average_salary(self):
        """Test method"""
        self.assertEqual(self.department.the_average_salary, 755)
