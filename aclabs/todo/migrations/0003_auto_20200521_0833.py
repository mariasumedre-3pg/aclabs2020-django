# Generated by Django 2.2.12 on 2020-05-21 08:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_add_due_date_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
