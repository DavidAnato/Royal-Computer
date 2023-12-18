# Generated by Django 4.2.2 on 2023-07-15 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='additional_images/', verbose_name='image supplémentaire')),
            ],
            options={
                'verbose_name': 'image supplémentaire',
                'verbose_name_plural': 'images supplémentaires',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'marque',
                'verbose_name_plural': 'marques',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'catégorie',
                'verbose_name_plural': 'catégories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='image')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='prix')),
                ('promo_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='prix promo')),
                ('in_promo', models.BooleanField(default=False, verbose_name='en promo')),
                ('in_stock', models.BooleanField(default=True, verbose_name='en stock')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('stock_count', models.IntegerField(default=1, verbose_name='quantité en stock')),
                ('additional_images', models.ManyToManyField(blank=True, related_name='products', to='ecommerce.additionalimage', verbose_name='images supplémentaires')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecommerce.brand', verbose_name='marque')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.category', verbose_name='catégorie')),
            ],
            options={
                'verbose_name': 'produit',
                'verbose_name_plural': 'produits',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 étoile'), (2, '2 étoiles'), (3, '3 étoiles'), (4, '4 étoiles'), (5, '5 étoiles')], verbose_name='notation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product', verbose_name='produit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'verbose_name': 'notation',
                'verbose_name_plural': 'notations',
            },
        ),
        migrations.AddField(
            model_name='additionalimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additional_image_set', to='ecommerce.product', verbose_name='produit'),
        ),
    ]
