# Generated by Django 5.1.4 on 2025-01-10 16:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_payment_reviewers2_remove_reviewrating_doc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewers',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
