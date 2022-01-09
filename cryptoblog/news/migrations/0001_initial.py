# Generated by Django 4.0.1 on 2022-01-08 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('body', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['-date_added'],
                'get_latest_by': 'date_added',
            },
        ),
    ]
