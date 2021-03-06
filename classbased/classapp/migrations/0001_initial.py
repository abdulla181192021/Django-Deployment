# Generated by Django 4.0.2 on 2022-03-19 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField(choices=[(1, 'worst'), (2, 'bad'), (3, 'not bad'), (4, 'good'), (5, 'Excellent')])),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classapp.musician')),
            ],
        ),
    ]
