# Generated by Django 4.1.1 on 2022-11-17 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_contact_options_contact_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('-name', 'created_at'), 'verbose_name': 'Elaqe', 'verbose_name_plural': 'Elaqeler'},
        ),
    ]
