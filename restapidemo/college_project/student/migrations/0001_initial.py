# Generated by Django 5.1.4 on 2025-03-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_number', models.CharField(max_length=20, unique=True)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science'), ('IT', 'Information Technology'), ('ECE', 'Electronics & Communication'), ('EEE', 'Electrical & Electronics'), ('ME', 'Mechanical'), ('CE', 'Civil'), ('AI', 'Artificial Intelligence'), ('DS', 'Data Science'), ('BIO', 'BioTech'), ('AUTO', 'Automobile')], max_length=10)),
                ('year', models.CharField(choices=[('FY', 'First Year'), ('SY', 'Second Year'), ('TY', 'Third Year'), ('BTech', 'B.Tech Final Year')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_number', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]
