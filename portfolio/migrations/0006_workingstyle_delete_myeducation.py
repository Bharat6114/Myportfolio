# Generated by Django 4.0 on 2022-01-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_remove_comment_blog_remove_comment_commenter_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workingstyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_style', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Myeducation',
        ),
    ]
