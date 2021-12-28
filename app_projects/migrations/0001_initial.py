# Generated by Django 4.0 on 2021-12-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('AUTHOR', 'AUTHOR'), ('CONTRIBUTOR', 'CONTRIBUTOR')], default='CONTRIBUTOR', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=2048)),
                ('type', models.CharField(choices=[('BACKEND', 'BACKEND'), ('FRONTEND', 'FRONTEND'), ('IOS', 'IOS'), ('ANDROID', 'ANDROID')], max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('desc', models.TextField(max_length=2048)),
                ('tag', models.CharField(choices=[('BUG', 'BUG'), ('UPGRADE', 'UPGRADE'), ('TASK', 'TASK')], max_length=100)),
                ('priority', models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], default='LOW', max_length=100)),
                ('status', models.CharField(choices=[('TODO', 'TODO'), ('IN PROGRESS', 'IN PROGRESS'), ('DONE', 'DONE')], default='TODO', max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.contributor')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.project')),
            ],
        ),
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='app_projects.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=2048)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_projects.issue')),
            ],
        ),
    ]
