# Generated by Django 4.0.3 on 2022-04-22 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('busi', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=100)),
                ('auth_user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]