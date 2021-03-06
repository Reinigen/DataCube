# Generated by Django 3.0.5 on 2020-04-10 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DataCubeApp', '0002_wine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alg_Name', models.CharField(max_length=300)),
                ('Alg_Type', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Alg_solution', models.CharField(max_length=300)),
                ('Alg_problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DataCubeApp.Algorithm')),
            ],
        ),
        migrations.DeleteModel(
            name='Wine',
        ),
        migrations.DeleteModel(
            name='WineProducer',
        ),
    ]
