# Generated by Django 2.2.4 on 2019-09-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('empid', models.IntegerField(max_length=8)),
                ('email', models.EmailField(max_length=25)),
                ('location', models.CharField(max_length=10)),
                ('salery', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]