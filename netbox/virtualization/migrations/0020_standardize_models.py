# Generated by Django 3.2b1 on 2021-02-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0019_standardize_name_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='clustergroup',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='clustertype',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='virtualmachine',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vminterface',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]