# Generated by Django 2.2.3 on 2020-08-15 21:20

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Название товара')),
                ('namee', models.CharField(max_length=50, verbose_name='Название товара')),
                ('photo', models.CharField(max_length=200, verbose_name='Фото file_id')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('description', models.CharField(max_length=3000, null=True, verbose_name='Описание')),
                ('category_code', models.CharField(max_length=20, verbose_name='Код категории')),
                ('category_name', models.CharField(max_length=30, verbose_name='Название категории')),
                ('subcategory_code', models.CharField(max_length=20, verbose_name='Код подкатегории')),
                ('subcategory_name', models.CharField(max_length=30, verbose_name='Название подкатегории')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(default=1, unique=True, verbose_name='ID Пользователя Телеграм')),
                ('name', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('username', models.CharField(max_length=100, null=True, verbose_name='Username Телеграм')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='usersmanage.User', unique=True)),
                ('referrer_id', models.BigIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchase_time', models.DateTimeField(auto_created=True, verbose_name='Время покупки')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('shipping_address', jsonfield.fields.JSONField(null=True, verbose_name='Адрес Доставки')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=100, null=True, verbose_name='Email')),
                ('receiver', models.CharField(max_length=100, null=True, verbose_name='Имя получателя')),
                ('successful', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('buyer', models.ForeignKey(on_delete=models.SET('deleted_user'), to='usersmanage.User', verbose_name='Покупатель')),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersmanage.Item', verbose_name='Идентификатор Товара')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
