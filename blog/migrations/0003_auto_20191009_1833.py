# Generated by Django 2.1.3 on 2019-10-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='label',
            field=models.CharField(choices=[('Business', 'Business'), ('Work', 'Work'), ('Study', 'Study'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]