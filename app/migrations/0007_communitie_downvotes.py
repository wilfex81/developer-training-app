# Generated by Django 4.0.4 on 2023-03-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_article_article_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitie',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
    ]
