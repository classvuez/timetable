# Generated by Django 3.2.6 on 2021-08-26 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='subject_sub_code',
            field=models.OneToOneField(db_column='subject_subCode', on_delete=django.db.models.deletion.CASCADE, to='accounts.subject'),
        ),
    ]
