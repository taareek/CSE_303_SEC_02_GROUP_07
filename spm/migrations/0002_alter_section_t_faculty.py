# Generated by Django 3.2.6 on 2021-09-12 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section_t',
            name='faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spm.faculty_t'),
        ),
    ]
