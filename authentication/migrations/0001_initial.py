# Generated by Django 4.2.2 on 2023-07-15 11:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'devise',
                'verbose_name_plural': 'devises',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='code')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'langue',
                'verbose_name_plural': 'langues',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
            ],
            options={
                'verbose_name': 'méthode de paiement',
                'verbose_name_plural': 'méthodes de paiement',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='numéro de téléphone')),
                ('profile_photo', models.ImageField(blank=True, upload_to='profile_photos/', verbose_name='photo de profil')),
                ('receive_confirmation_emails', models.BooleanField(default=True, verbose_name='recevoir des e-mails de confirmation')),
                ('receive_order_updates', models.BooleanField(default=True, verbose_name='recevoir des mises à jour de commande')),
                ('receive_promotions', models.BooleanField(default=True, verbose_name='recevoir des promotions')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='adresse')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='ville')),
                ('postal_code', models.CharField(blank=True, max_length=10, verbose_name='code postal')),
                ('mobile_money_number', models.CharField(blank=True, max_length=20, verbose_name='numéro mobile money')),
                ('paypal_email', models.EmailField(blank=True, max_length=254, verbose_name='adresse e-mail PayPal')),
                ('profile_visibility', models.BooleanField(default=True, verbose_name='visibilité du profil')),
                ('data_sharing', models.BooleanField(default=True, verbose_name='autorisations de partage de données')),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.currency', verbose_name='devise')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.language', verbose_name='langue préférée')),
                ('payment_method', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.paymentmethod', verbose_name='méthode de paiement')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'utilisateur personnalisé',
                'verbose_name_plural': 'utilisateurs personnalisés',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
