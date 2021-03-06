# Generated by Django 3.2.7 on 2021-12-02 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
