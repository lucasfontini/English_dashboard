# Generated by Django 4.1.5 on 2023-01-16 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishdashboardAPP', '0003_expressao_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expressao',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]
