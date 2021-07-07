from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0001_initial_300_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customlink',
            name='button_class',
            field=models.CharField(default='outline-dark', max_length=30),
        ),
    ]
