# Generated by Django 4.0.4 on 2022-04-26 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_products_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='img',
            field=models.ImageField(null=b'I01\n', upload_to=''),
        ),
    ]