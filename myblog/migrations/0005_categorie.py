# Generated by Django 2.1.5 on 2019-01-24 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=100, unique=True)),
            ],
        ),
    ]
