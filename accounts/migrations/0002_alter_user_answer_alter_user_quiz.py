# Generated by Django 4.1 on 2022-08-03 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='answer',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='quiz',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='qz', to='accounts.quiz'),
        ),
    ]
