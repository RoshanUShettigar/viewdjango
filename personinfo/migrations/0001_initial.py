# Generated by Django 2.1.5 on 2019-01-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
