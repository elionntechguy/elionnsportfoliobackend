# Generated by Django 3.1.3 on 2020-12-10 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('link', models.CharField(max_length=120)),
                ('workimg', models.ImageField(max_length=255, upload_to='img/')),
            ],
        ),
    ]
