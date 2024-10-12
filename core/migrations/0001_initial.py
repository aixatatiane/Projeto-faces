# Generated by Django 5.0.6 on 2024-07-13 11:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('ocupacao', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('data_falecimento', models.DateField(blank=True, null=True)),
                ('imagem', models.ImageField(upload_to='uploads/')),
                ('postado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Face',
                'verbose_name_plural': 'Faces',
            },
        ),
    ]