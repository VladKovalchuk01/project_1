# Generated by Django 4.0.1 on 2022-01-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_post_post_cats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_cats',
            field=models.CharField(choices=[("men's", "man's"), ("women's", "woman's"), ("children's", "child's")], default="men's", max_length=10),
        ),
    ]
