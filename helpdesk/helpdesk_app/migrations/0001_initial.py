# Generated by Django 4.2 on 2024-04-04 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('is_done', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('assignee', models.CharField(choices=[('Bob', 'Bob'), ('Steve', 'Steve'), ('Sarah', 'Sarah'), ('Yui', 'Yui')], max_length=200)),
                ('priority', models.CharField(choices=[('1', 'Highest'), ('2', 'High'), ('3', 'Medium'), ('4', 'Low'), ('5', 'Lowest')], max_length=1)),
                ('contact_email', models.CharField(max_length=200)),
            ],
        ),
    ]
