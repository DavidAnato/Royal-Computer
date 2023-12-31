# Generated by Django 4.2.2 on 2023-10-22 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_remove_customuser_address_remove_customuser_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart_manage', '0006_promocode_is_valid_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('delivery_method', models.CharField(choices=[('address', "Livraison à l'adresse"), ('meeting', 'Rencontre'), ('pickup', 'Retrait en personne')], default='address', max_length=10, verbose_name='Méthode de livraison')),
                ('delivery_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.address')),
                ('items', models.ManyToManyField(related_name='orders', to='cart_manage.cartitem')),
                ('promo_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart_manage.promocode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
