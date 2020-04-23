# Generated by Django 3.0.4 on 2020-04-23 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_auto_20200423_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basistemplate',
            name='indicator_factor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basis_templates', to='plan.IndicatorFactor', verbose_name='支撑课程以及指标系数'),
        ),
        migrations.AlterField(
            model_name='indicatorfactor',
            name='target',
            field=models.TextField(blank=True, default='', null=True, verbose_name='课程教学目标'),
        ),
    ]
