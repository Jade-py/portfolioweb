# Generated by Django 4.2.6 on 2023-12-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_projects_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='icon',
            field=models.ImageField(null=True, upload_to='portfolio/uploads'),
        ),
    ]
