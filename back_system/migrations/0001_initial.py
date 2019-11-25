# Generated by Django 2.0.1 on 2019-11-21 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'sys_role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('auth_string', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'sys_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SysUserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('role_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sys_user_role',
                'managed': False,
            },
        ),
    ]