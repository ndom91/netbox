from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0001_initial_300_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cable',
            name='length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
