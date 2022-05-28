# Generated by Django 4.0.4 on 2022-05-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0002_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done'), ('Deleted', 'Deleted')], default='Pending', max_length=20),
        ),
    ]
