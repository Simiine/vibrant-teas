# Generated by Django 3.2 on 2023-01-09 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producers', '0001_initial'),
        ('products', '0005_alter_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='producer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producers.producer'),
        ),
    ]