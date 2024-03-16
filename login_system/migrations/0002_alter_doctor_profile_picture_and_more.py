# Generated by Django 4.2.3 on 2024-03-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='profile_picture',
            field=models.ImageField(upload_to='static/imades/Doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='profile_picture',
            field=models.ImageField(upload_to='static/images/Patient'),
        ),
    ]