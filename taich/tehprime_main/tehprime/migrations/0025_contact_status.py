# Generated by Django 3.2.9 on 2022-04-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tehprime', '0024_contact_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('Рассмотрена', 'Рассмотрена'), ('В ожидании', 'В ожидании'), ('Отклонена', 'Отклонена')], default='Доставлена', max_length=30),
        ),
    ]
