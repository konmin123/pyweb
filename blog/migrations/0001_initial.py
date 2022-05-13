# Generated by Django 4.0.4 on 2022-05-13 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('message', models.TextField(default='', verbose_name='Текст статьи')),
                ('public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
        ),
    ]
