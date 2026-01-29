# Generated migration: Add batch foreign key to mortality models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_dailyrecordsiaf_ai_birds_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='malebirdsmortality',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mortality_records', to='myapp.MaleBirdsStock'),
        ),
        migrations.AddField(
            model_name='femalebirdsmortality',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mortality_records', to='myapp.FemaleBirdsStock'),
        ),
    ]
