# Generated by Django 4.2.11 on 2024-07-18 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ican', '0025_jobdata_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobdatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_post', models.CharField(max_length=30)),
                ('job_position', models.CharField(max_length=35)),
                ('upload_date', models.CharField(max_length=20)),
                ('job_timing', models.CharField(max_length=30)),
                ('company_title', models.CharField(max_length=35)),
                ('job_description', models.TextField(default='Best place to work', max_length=300)),
                ('skill_1', models.CharField(blank=True, max_length=40)),
                ('skill_2', models.CharField(blank=True, max_length=40)),
                ('skill_3', models.CharField(blank=True, max_length=40)),
                ('skill_4', models.CharField(blank=True, max_length=40)),
                ('skill_5', models.CharField(blank=True, max_length=40)),
                ('job_city', models.CharField(max_length=30)),
                ('job_Address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=10)),
                ('email_id', models.EmailField(blank=True, max_length=60)),
                ('website_link', models.CharField(blank=True, max_length=100)),
                ('gmaps_link', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='jobdata',
        ),
    ]