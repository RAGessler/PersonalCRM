# Generated by Django 4.0.4 on 2022-05-26 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('text', models.CharField(max_length=255)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.contact')),
            ],
        ),
    ]