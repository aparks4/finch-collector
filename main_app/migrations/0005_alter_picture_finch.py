# Generated by Django 4.1.1 on 2022-10-03 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_img_picture_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='finch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='main_app.finch'),
        ),
    ]