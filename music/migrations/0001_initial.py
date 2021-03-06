# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 01:31
from __future__ import unicode_literals

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
            name='AirtimeTopUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('amount', models.PositiveIntegerField()),
                ('point_earned', models.PositiveIntegerField(default=0)),
                ('transaction_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'AirtimeTopUp',
                'verbose_name_plural': 'AirtimeTopUps',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('other_name', models.CharField(blank=True, max_length=20)),
                ('stage_name', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email Address')),
                ('photo', models.FileField(blank=True, upload_to='images')),
                ('slug', models.SlugField(max_length=20)),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='ArtistAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('slug', models.SlugField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
            options={
                'verbose_name_plural': 'Artist Accounts',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_count', models.PositiveIntegerField(default=0)),
                ('user_location', models.CharField(blank=True, max_length=50)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField()),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Artist')),
            ],
            options={
                'verbose_name_plural': 'Downloads',
                'ordering': ('download_count',),
            },
        ),
        migrations.CreateModel(
            name='Hits254Ac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_earned', models.PositiveIntegerField()),
                ('date_update', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Hits254AC',
                'verbose_name_plural': 'Hits254ACs',
            },
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('points', models.PositiveIntegerField()),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
                'ordering': ('amount',),
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=50)),
                ('song_type', models.CharField(choices=[('MP3', 'MP3'), ('MP4', 'MP4')], max_length=3)),
                ('song_url', models.FileField(upload_to='media')),
                ('snippet_url', models.FileField(blank=True, upload_to='media/snippets')),
                ('download_point', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField()),
                ('date_released', models.DateField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.Artist')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music.Category')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30, verbose_name='First Name')),
                ('LastName', models.CharField(max_length=30, verbose_name='Last Name')),
                ('phone_no', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'HITS254 Users',
            },
        ),
        migrations.AddField(
            model_name='hits254ac',
            name='phone_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.UserAccount'),
        ),
        migrations.AddField(
            model_name='downloads',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Song'),
        ),
        migrations.AddField(
            model_name='artistaccount',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Downloads'),
        ),
        migrations.AddField(
            model_name='artist',
            name='phone_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.UserAccount'),
        ),
        migrations.AddField(
            model_name='airtimetopup',
            name='phone_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.UserAccount'),
        ),
    ]
