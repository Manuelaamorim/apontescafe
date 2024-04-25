# Generated by Django 5.0.3 on 2024-04-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0025_delete_usercliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(default='Desconhecido', max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('confirm_password', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
