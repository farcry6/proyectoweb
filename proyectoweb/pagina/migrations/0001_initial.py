# Generated by Django 3.2 on 2021-05-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('texto', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('borrador', 'Borrador'), ('publicado', 'Publicado')], default='borrador', max_length=10)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
