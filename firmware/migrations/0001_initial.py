# Generated by Django 3.0.4 on 2020-03-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EncoderFirmware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameVersion', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=10)),
                ('buildVersion', models.IntegerField()),
                ('updateDate', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='encoder_firmware')),
            ],
            options={
                'verbose_name_plural': 'Firmware del encoder',
            },
        ),
        migrations.CreateModel(
            name='ServerFirmware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameVersion', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=10)),
                ('buildVersion', models.IntegerField()),
                ('updateDate', models.DateField(auto_now_add=True)),
                ('file', models.FileField(upload_to='server_firmware')),
            ],
            options={
                'verbose_name_plural': 'Firmware del servidor',
            },
        ),
    ]