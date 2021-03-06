# Generated by Django 3.1.7 on 2021-03-12 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_statedemographic_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statedemographic',
            name='black_college_grad_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='statedemographic',
            name='black_highschool_grad_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='statedemographic',
            name='black_population_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='statedemographic',
            name='white_college_grad_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='statedemographic',
            name='white_highschool_grad_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='statedemographic',
            name='white_population_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
