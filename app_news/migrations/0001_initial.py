# Generated by Django 5.0.3 on 2024-03-15 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=255, verbose_name='News title')),
                ('news_txt', models.TextField(verbose_name='News content')),
                ('news_date', models.DateTimeField(auto_now_add=True, verbose_name='News published time')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news',
            },
        ),
    ]
