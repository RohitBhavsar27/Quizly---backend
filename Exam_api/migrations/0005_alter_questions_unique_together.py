# Generated by Django 5.1.4 on 2025-01-10 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_api', '0004_admin'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='questions',
            unique_together={('qno', 'subject')},
        ),
    ]
