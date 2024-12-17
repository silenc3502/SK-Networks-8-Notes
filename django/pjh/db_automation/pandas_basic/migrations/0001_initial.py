# Generated by Django 5.1.4 on 2024-12-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PandasBasicPerson',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'pandas_basic_person',
            },
        ),
    ]