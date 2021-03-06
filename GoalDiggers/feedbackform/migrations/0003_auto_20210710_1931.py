# Generated by Django 3.2.5 on 2021-07-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbackform', '0002_feedback_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='question1',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='question2',
            field=models.CharField(default='stri', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='question3',
            field=models.CharField(default='stri', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='question4',
            field=models.CharField(default='stri', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='question5',
            field=models.CharField(default='stri', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='feedback',
            name='session',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Others', max_length=20),
        ),
    ]
