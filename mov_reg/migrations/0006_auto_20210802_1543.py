# Generated by Django 3.2.5 on 2021-08-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mov_reg', '0005_auto_20210730_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='TripSheetDate',
            field=models.CharField(blank=True, default='02-08-2021', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle_detail',
            name='Date',
            field=models.CharField(default='02-08-2021', max_length=10),
        ),
    ]
