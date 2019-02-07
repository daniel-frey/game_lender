# Generated by Django 2.1.5 on 2019-02-07 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gl_library', '0002_auto_20190206_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1028)),
                ('body', models.TextField()),
                ('sent_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='message_from', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='message_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('igdb_platform_id', models.IntegerField()),
                ('platform_name', models.CharField(max_length=96)),
            ],
        ),
        migrations.RenameField(
            model_name='game',
            old_name='rating',
            new_name='aggregate_rating',
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='platform',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='game_platform', to='gl_library.Platform'),
        ),
    ]