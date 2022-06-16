# Generated by Django 2.2.4 on 2022-06-13 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='Enrollment_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='First_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Gender',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Phone_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Regional_Centre_Code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Regional_Centre_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Session',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Study_Centre_Code',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='Study_Centre_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='permanent_block',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='temporary_block',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='timout',
            field=models.DateTimeField(blank=True),
        ),
    ]