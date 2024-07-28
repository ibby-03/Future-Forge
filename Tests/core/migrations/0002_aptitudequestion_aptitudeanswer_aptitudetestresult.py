# Generated by Django 5.0.7 on 2024-07-28 00:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AptitudeQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('technical', 'Technical Skills'), ('creative', 'Creative Skills'), ('communication', 'Communication Skills'), ('analytical', 'Analytical Skills'), ('social', 'Social Skills')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AptitudeAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('score', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.aptitudequestion')),
            ],
        ),
        migrations.CreateModel(
            name='AptitudeTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technical_score', models.IntegerField()),
                ('creative_score', models.IntegerField()),
                ('communication_score', models.IntegerField()),
                ('analytical_score', models.IntegerField()),
                ('social_score', models.IntegerField()),
                ('total_score', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
