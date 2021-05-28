# Generated by Django 3.2.3 on 2021-05-28 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default=None, max_length=100)),
                ('job_position', models.CharField(default=None, max_length=100)),
                ('img', models.ImageField(default=None, upload_to='testimonials')),
                ('desc', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
