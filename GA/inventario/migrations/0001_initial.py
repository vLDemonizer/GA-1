# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-20 16:54
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import inventario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('enterprise', models.CharField(default=b'Grupo Alcars', max_length=20)),
                ('country', models.CharField(default=b'Venezuela', max_length=20)),
                ('city', models.CharField(default=b'Puerto La Cruz', max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Move_Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destiny', models.CharField(default=b'Almacen', max_length=30)),
                ('date', models.DateTimeField()),
                ('origin', models.CharField(default=b'Almacen', max_length=30)),
                ('authorized_by', models.SmallIntegerField()),
                ('received_by', models.SmallIntegerField()),
                ('given_by', models.SmallIntegerField()),
                ('reason', models.CharField(max_length=15)),
                ('reason_description', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoveIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destiny', models.CharField(default=b'Almacen', max_length=30)),
                ('date', models.DateTimeField()),
                ('is_move_in', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_code', models.CharField(blank=True, max_length=60, unique=True)),
                ('available', models.BooleanField(default=True)),
                ('location', models.CharField(default=b'Almacen', max_length=30)),
                ('number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=50)),
                ('size', models.CharField(blank=True, max_length=15, null=True)),
                ('description', models.TextField(blank=True, max_length=120)),
                ('code', models.CharField(default=inventario.models.generate_product_code, max_length=5, unique=True)),
                ('min_amount', models.SmallIntegerField(blank=True, null=True)),
                ('is_disposable', models.BooleanField(default=False)),
                ('cost_value', models.FloatField(default=0)),
                ('our_value', models.FloatField(default=0)),
                ('their_value', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MoveOut',
            fields=[
                ('movein_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventario.MoveIn')),
                ('origin', models.CharField(default=b'Almacen', max_length=30)),
                ('authorized_by', models.SmallIntegerField()),
                ('received_by', models.SmallIntegerField()),
                ('given_by', models.SmallIntegerField()),
                ('reason', models.CharField(max_length=15)),
                ('reason_description', models.TextField(blank=True, max_length=300, null=True)),
            ],
            bases=('inventario.movein',),
        ),
        migrations.AddField(
            model_name='product',
            name='product_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ProductClass'),
        ),
        migrations.AddField(
            model_name='movein',
            name='product_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ProductClass'),
        ),
        migrations.AddField(
            model_name='movein',
            name='products',
            field=models.ManyToManyField(to='inventario.Product'),
        ),
        migrations.AddField(
            model_name='move_out',
            name='product_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ProductClass'),
        ),
        migrations.AddField(
            model_name='move_out',
            name='products',
            field=models.ManyToManyField(to='inventario.Product'),
        ),
    ]
