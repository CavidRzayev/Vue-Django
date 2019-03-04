# Generated by Django 2.1.5 on 2019-03-04 21:47

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
            name='Article',
            fields=[
                ('city', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Qiymet')),
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_heading', models.CharField(max_length=250, verbose_name='Kategoriya')),
                ('article_body', models.TextField(verbose_name='Mezmun')),
                ('user', models.ForeignKey(blank=True, editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
