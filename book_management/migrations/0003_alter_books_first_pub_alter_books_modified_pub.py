# Generated by Django 4.2.4 on 2023-09-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0002_books_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='first_pub',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='modified_pub',
            field=models.DateField(auto_now=True),
        ),
    ]