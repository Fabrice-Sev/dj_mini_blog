# Generated by Django 3.2.5 on 2021-08-12 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(verbose_name='Date Joined')),
                ('blogger_bio', models.CharField(max_length=1000, verbose_name='Bio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('post_date', models.DateField(default=django.utils.timezone.now, verbose_name='Post Date')),
                ('content', models.CharField(max_length=1000)),
                ('blog_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogger')),
            ],
            options={
                'ordering': ['post_date', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Post Date')),
                ('comment_text', models.CharField(max_length=255, verbose_name='Text')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
                ('comment_author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]
