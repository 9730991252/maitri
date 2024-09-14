# Generated by Django 5.1.1 on 2024-09-14 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.bill')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.item')),
            ],
        ),
    ]
