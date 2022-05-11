# Generated by Django 4.0.4 on 2022-05-10 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('state', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('image', models.CharField(max_length=1024)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrines.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrines.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrines.country')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('itens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vitrines.itens')),
            ],
        ),
    ]
