# Generated by Django 4.2.1 on 2023-05-23 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='item_brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.brand'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.itemgroup'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.state'),
        ),
    ]