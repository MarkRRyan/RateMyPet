# Generated by Django 4.0.4 on 2022-05-10 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.TextField(max_length=300)),
                ('image_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userrating', models.TextField(max_length=300)),
                ('petid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userratings', to='RateMyPet.pet')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userratings', to='RateMyPet.user')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='RateMyPet.user'),
        ),
    ]
