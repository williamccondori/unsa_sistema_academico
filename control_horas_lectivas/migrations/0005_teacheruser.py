# Generated by Django 2.0.3 on 2018-04-05 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control_horas_lectivas', '0004_auto_20180319_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_horas_lectivas.Teacher')),
                ('user_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control_horas_lectivas.UserSystem')),
            ],
        ),
    ]