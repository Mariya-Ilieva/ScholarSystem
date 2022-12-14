# Generated by Django 4.1.3 on 2022-11-30 13:48

from django.db import migrations, models
import scholar_system.seminars.validators


class Migration(migrations.Migration):

    dependencies = [
        ('seminars', '0003_alter_seminar_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='theme',
            field=models.CharField(max_length=100, validators=[scholar_system.seminars.validators.validate_theme]),
        ),
    ]
