# Generated by Django 2.2.4 on 2019-08-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
