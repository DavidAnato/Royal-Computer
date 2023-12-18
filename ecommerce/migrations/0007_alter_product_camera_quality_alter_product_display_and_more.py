# Generated by Django 4.2.2 on 2023-10-10 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_product_camera_quality_product_display_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='camera_quality',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Camera'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ecran'),
        ),
        migrations.AlterField(
            model_name='product',
            name='graphics',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Graphisme'),
        ),
        migrations.AlterField(
            model_name='product',
            name='harddisk_capacity',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Capacite memoire'),
        ),
        migrations.AlterField(
            model_name='product',
            name='memory',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Memoire RAM'),
        ),
        migrations.AlterField(
            model_name='product',
            name='processor_capacity',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Processeur'),
        ),
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, null=True, verbose_name='Specification'),
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty_info',
            field=models.TextField(blank=True, null=True, verbose_name='Info Garantie'),
        ),
        migrations.CreateModel(
            name='KeyWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=100, null=True, verbose_name='Mot clé')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='keyword_set', to='ecommerce.product', verbose_name='produit')),
            ],
            options={
                'verbose_name': 'Mot clé',
                'verbose_name_plural': 'Mots clés',
            },
        ),
    ]