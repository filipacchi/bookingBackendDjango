# Generated by Django 4.1.7 on 2023-04-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('washbooking', '0003_remove_person_association_remove_person_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='inAssociation',
        ),
        migrations.AddField(
            model_name='person',
            name='associations',
            field=models.ManyToManyField(to='washbooking.association'),
        ),
    ]
