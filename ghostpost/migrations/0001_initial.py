# Generated by Django 2.2.7 on 2019-11-11 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boast_roast', models.BooleanField(choices=[(True, 'Boast'), (False, 'Roast')])),
                ('upvote', models.IntegerField(default=0)),
                ('downvote', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=280)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
