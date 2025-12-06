# Generated migration for MaleBirdsStock status tracking

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_rename_dailyrecordcross_dailyrecordsiaf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='malebirdsstock',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('ended', 'Ended')], default='active', max_length=10),
        ),
        migrations.AddField(
            model_name='malebirdsstock',
            name='final_mortality',
            field=models.IntegerField(default=0),
        ),
    ]
