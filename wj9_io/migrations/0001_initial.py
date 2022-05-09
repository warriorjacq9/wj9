# Generated by Django 4.0.4 on 2022-05-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('file', models.FileField(upload_to='products/')),
            ],
            options={
                'verbose_name_plural': 'Digital Products',
            },
        ),
    ]
