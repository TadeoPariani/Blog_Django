# Generated by Django 4.2.1 on 2023-07-03 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_post_categories'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categories',
            new_name='category',
        ),
    ]