# Generated by Django 2.1.5 on 2019-10-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_signin_signout_signup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignIn',
        ),
        migrations.DeleteModel(
            name='SignOut',
        ),
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
