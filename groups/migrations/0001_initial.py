# Generated by Django 2.1.4 on 2018-12-17 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('city_or_town', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=200, null=True)),
                ('facebook_group', models.CharField(max_length=200, null=True)),
                ('facebook_page', models.CharField(max_length=200, null=True)),
                ('official_email', models.CharField(max_length=200, null=True)),
                ('lean_email', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]