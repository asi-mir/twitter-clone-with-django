# Generated by Django 3.1.7 on 2021-02-27 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210226_2032'),
        ('posts', '0003_auto_20210227_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='liked', to='accounts.Profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=type, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='posts.post'),
        ),
    ]
