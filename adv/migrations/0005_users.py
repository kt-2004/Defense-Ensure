# Generated by Django 4.2.5 on 2023-09-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adv', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uName', models.CharField(max_length=255)),
                ('uEmail', models.EmailField(max_length=254)),
                ('uPass', models.CharField(max_length=255)),
            ],
        ),
    ]
