# Generated by Django 4.2.4 on 2025-02-13 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_remove_usermodel_is_employee_of_restaurant_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="Phone Number"
            ),
        ),
    ]
