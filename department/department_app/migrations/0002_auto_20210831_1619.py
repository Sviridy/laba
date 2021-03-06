# Generated by Django 3.2.6 on 2021-08-31 13:19

from django.db import migrations
def forwards_func(apps, schema_editor):
    Department = apps.get_model("department_app", "Department")
    Specialization = apps.get_model("department_app", "Specialization")
    Positions = apps.get_model("department_app", "Positions")
    Employee = apps.get_model("department_app", "Employee")
    Department.objects.bulk_create([
        Department(department="Finance"),
        Department(department="Marketing"),
        Department(department="Developer"),
    ])
    Specialization.objects.bulk_create([
        Specialization(name='Python'),
        Specialization(name='C#'),
        Specialization(name='Java'),
        Specialization(name='C++'),
    ])
    Positions.objects.bulk_create([
        Positions(name='Senior'),
        Positions(name='Middle'),
        Positions(name='Junior'),
        Positions(name='Student'),
    ])
    Employee.objects.bulk_create([
        Employee(name='Ihar Nauros', date_of_birth='1990-01-01',
                 department=Department.objects.get(department='Developer'),
                 positions=Positions.objects.get(name='Senior'),
                 specialization=Specialization.objects.get(name='Python'), experience=15, wages=1500),
        Employee(name='Svirydzetski Kanstantsin', date_of_birth='1998-05-05',
                 department=Department.objects.get(department='Developer'),
                 positions=Positions.objects.get(name='Student'),
                 specialization=Specialization.objects.get(name='Python'), experience=1, wages=10),
    ])

def reverse_func(apps, schema_editor):
    Department = apps.get_model("department_app", "Department")
    Specialization = apps.get_model("department_app", "Specialization")
    Positions = apps.get_model("department_app", "Positions")
    Employee = apps.get_model("department_app", "Employee")
    Department.objects.filter(department="Finance").delete()
    Department.objects.filter(department="Marketing").delete()
    Department.objects.filter(department="Developer").delete()
    Specialization.objects.filter(name='Python').delete()
    Specialization.objects.filter(name='C#').delete()
    Specialization.objects.filter(name='Java').delete()
    Specialization.objects.filter(name='C++').delete()
    Positions.objects.filter(name='Senior').delete()
    Positions.objects.filter(name='Middle').delete()
    Positions.objects.filter(name='Junior').delete()
    Positions.objects.filter(name='Student').delete()
    Employee.objects.filter(name='Ihar Nauros', date_of_birth='1990-01-01', experience=15, wages=1500).delete()
    Employee.objects.filter(name='Svirydzetski Kanstantsin', date_of_birth='1998-05-05', experience=1,
                            wages=10).delete()

class Migration(migrations.Migration):

    dependencies = [
        ('department_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
