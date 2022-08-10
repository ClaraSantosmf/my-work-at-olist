# Generated by Django 4.1 on 2022-08-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('edicao', models.PositiveIntegerField()),
                ('ano_de_publicacao', models.CharField(max_length=4)),
                ('autores', models.ManyToManyField(related_name='books', to='core.autor')),
            ],
        ),
    ]