# Generated by Django 2.2.1 on 2019-05-17 19:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45, validators=[django.core.validators.RegexValidator(message='Please enter a valid name', regex='^([A-Za-z])+$')])),
                ('email', models.EmailField(max_length=45, validators=[django.core.validators.RegexValidator(message='Please enter a valid email address', regex='^([a-zA-Z0-9_\\.\\-])+\\@(([a-zA-Z0-9\\-])+\\.)+([a-zA-Z0-9]{2,4})+$')])),
                ('password', models.CharField(max_length=45)),
                ('birthdate', models.DateTimeField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message='Please enter a valid phone number', regex='^01[5|1|2|0][0-9]{8}$')])),
            ],
        ),
    ]
