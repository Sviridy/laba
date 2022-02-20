"""Tests REST"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from department_app.models import Department, Positions, Specialization, Employee
from department_app.rest.serializers import DepartmentListSerializer, EmployeeListSerializer, \
    SpecializationListSerializer, PositionsListSerializer


class CreateTests(APITestCase):
    """Class test create"""
    def test_can_create_department(self):
        """Test create department"""
        url = reverse('department-list')
        data = {'department': 'One'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_create_positions(self):
        """Test create positions"""
        url = reverse('positions-list')
        data = {'name': 'One'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_create_specialization(self):
        """Test create specialization"""
        url = reverse('specialization-list')
        data = {'name': 'One'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_create_employee(self):
        """Test create employee"""
        url = reverse('employee-list')
        data = {'name': 'Kostya', 'date_of_birth': '1998-05-05', 'experience': 1, 'wages': 10, 'department': 1,
                'positions': 1, 'specialization': 1}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTests(APITestCase):
    """Class test read"""
    def setUp(self):
        self.department = Department.objects.create(department='One')
        self.specialization = Specialization.objects.create(name='Py')
        self.positions = Positions.objects.create(name='Stud')
        self.employee = Employee.objects.create(name='Svirydzetski', date_of_birth='1995-05-05',
                                                department=self.department, positions=self.positions,
                                                specialization=self.specialization,
                                                experience=5, wages=20)

    def test_can_read_department_list(self):
        """Test read department list"""
        url = reverse('department-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_department_detail(self):
        """Test read department detail"""
        url = reverse('department-list')
        response = self.client.get(url, args=[self.department.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_positions_list(self):
        """Test read positions list"""
        url = reverse('positions-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_positions_detail(self):
        """Test read positions detail"""
        url = reverse('positions-list')
        response = self.client.get(url, args=[self.positions.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_specialization_list(self):
        """Test read specialization list"""
        url = reverse('specialization-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_specialization_detail(self):
        """Test read specialization detail"""
        url = reverse('specialization-list')
        response = self.client.get(url, args=[self.specialization.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_employee_list(self):
        """Test read employee list"""
        url = reverse('employee-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_employee_detail(self):
        """Test read employee detail"""
        url = reverse('employee-list')
        response = self.client.get(url, args=[self.employee.id])
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTests(APITestCase):
    """Class test update"""
    def setUp(self):
        self.department = Department.objects.create(department='One')
        self.specialization = Specialization.objects.create(name='Py')
        self.positions = Positions.objects.create(name='Stud')
        self.employee = Employee.objects.create(name='Svirydzetski', date_of_birth='1995-05-05',
                                                department=self.department, positions=self.positions,
                                                specialization=self.specialization,
                                                experience=5, wages=20)
        self.data1 = DepartmentListSerializer(self.department).data
        self.data1.update({'department': 'Two'})
        self.data2 = PositionsListSerializer(self.positions).data
        self.data2.update({'name': 'C'})
        self.data3 = SpecializationListSerializer(self.specialization).data
        self.data3.update({'name': 'Sen'})
        self.data4 = EmployeeListSerializer(self.employee).data
        self.data4.update({'name': 'Ivanov'})

    def test_can_update_department(self):
        """Test update department"""
        response = self.client.put(reverse('department-detail', args=[self.department.id]), self.data1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_positions(self):
        """Test update positions"""
        response = self.client.put(reverse('positions-detail', args=[self.positions.id]), self.data2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_specialization(self):
        """Test update specialization"""
        response = self.client.put(reverse('specialization-detail', args=[self.specialization.id]), self.data3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_employee(self):
        """Test update employee"""
        response = self.client.put(reverse('employee-detail', args=[self.employee.id]), self.data4)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTests(APITestCase):
    """Class test delete"""
    def setUp(self):
        self.department = Department.objects.create(department='One')
        self.specialization = Specialization.objects.create(name='Py')
        self.positions = Positions.objects.create(name='Stud')
        self.employee = Employee.objects.create(name='Svirydzetski', date_of_birth='1995-05-05',
                                                department=self.department, positions=self.positions,
                                                specialization=self.specialization,
                                                experience=5, wages=20)

    def test_can_delete_department(self):
        """Test delete department"""
        response = self.client.delete(reverse('department-detail', args=[self.department.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_delete_positions(self):
        """Test delete positions"""
        response = self.client.delete(reverse('positions-detail', args=[self.positions.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_delete_specialization(self):
        """Test delete specialization"""
        response = self.client.delete(reverse('specialization-detail', args=[self.specialization.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_can_delete_employee(self):
        """Test delete employee"""
        response = self.client.delete(reverse('employee-detail', args=[self.employee.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
