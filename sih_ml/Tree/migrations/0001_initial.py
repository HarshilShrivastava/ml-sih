# Generated by Django 2.0.13 on 2020-07-07 11:55

from django.db import migrations, models
import django.db.models.deletion
import tree.fields
import tree.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('path', tree.fields.PathField()),
                ('public', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Tree.Tree')),
            ],
            options={
                'ordering': ('path',),
            },
            bases=(models.Model, tree.models.TreeModelMixin),
        ),
    ]
