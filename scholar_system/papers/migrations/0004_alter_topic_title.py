# Generated by Django 4.1.3 on 2022-11-30 13:54

from django.db import migrations, models
import scholar_system.seminars.validators


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0003_alter_paper_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=25, unique=True, validators=[scholar_system.seminars.validators.validate_theme]),
        ),
    ]