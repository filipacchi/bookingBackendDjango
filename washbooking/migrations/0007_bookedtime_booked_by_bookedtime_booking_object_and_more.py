# Generated by Django 4.1.7 on 2023-04-08 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('washbooking', '0006_remove_person_assocation_person_associations'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedtime',
            name='booked_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='washbooking.person'),
        ),
        migrations.AddField(
            model_name='bookedtime',
            name='booking_object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='washbooking.bookableobject'),
        ),
        migrations.AddField(
            model_name='bookedtime',
            name='date',
            field=models.DateField(help_text='YYYY-MM-DD', null=True),
        ),
        migrations.AddField(
            model_name='bookedtime',
            name='timeslot',
            field=models.IntegerField(choices=[(0, '06:00 - 10:00'), (1, '10:00 - 14:00'), (2, '14:00 - 18:00'), (3, '18:00 - 22:00')], null=True),
        ),
        migrations.AlterUniqueTogether(
            name='bookedtime',
            unique_together={('timeslot', 'date')},
        ),
        migrations.RemoveField(
            model_name='bookedtime',
            name='endTime',
        ),
        migrations.RemoveField(
            model_name='bookedtime',
            name='startTime',
        ),
    ]
