# Generated by Django 3.2.9 on 2022-01-05 01:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('quantity', models.FloatField()),
                ('is_countable', models.BooleanField()),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='server.bill')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='server.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='server.user')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='server.user'),
        ),
    ]
