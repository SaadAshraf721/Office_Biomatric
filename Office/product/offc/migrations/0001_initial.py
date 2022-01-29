# Generated by Django 3.0 on 2021-04-07 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('di', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offc.department')),
                ('oi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offc.office')),
            ],
        ),
    ]
