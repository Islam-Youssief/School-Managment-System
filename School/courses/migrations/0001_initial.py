# Generated by Django 2.2.1 on 2019-05-17 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('days_needed', models.IntegerField(default=0)),
                ('hours_needed', models.IntegerField(default=0)),
                ('start_hour', models.TimeField(blank=True)),
                ('end_hour', models.TimeField(blank=True)),
                ('content', models.CharField(max_length=250)),
                ('vacation', models.CharField(max_length=25)),
                ('instructor_name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=True, related_name='courses', to='students.Student')),
                ('subject', models.ForeignKey(on_delete=True, related_name='students', to='courses.Course')),
            ],
        ),
    ]
