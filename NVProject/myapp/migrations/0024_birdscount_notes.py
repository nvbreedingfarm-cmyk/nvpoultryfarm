# Generated migration to add notes field to BirdsCount

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_merge_20251206_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdscount',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
