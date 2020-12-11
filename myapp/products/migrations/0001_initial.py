# Generated by Django 2.1.8 on 2020-02-17 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, max_digits=15)),
                ('min_quantity', models.IntegerField()),
                ('description', models.TextField()),
                ('features', models.TextField()),
                ('image1', models.ImageField(upload_to='products')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='products')),
                ('is_famous_product', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Categories')),
            ],
        ),
    ]
