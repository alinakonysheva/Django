# Generated by Django 4.0.2 on 2022-03-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resumeitem',
            options={'ordering': ['-date_from', '-date_till', 'company']},
        ),
        migrations.AlterModelOptions(
            name='skillcategory',
            options={},
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]