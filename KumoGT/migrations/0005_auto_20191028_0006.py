# Generated by Django 2.2.6 on 2019-10-28 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KumoGT', '0004_auto_20191028_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deg_plan_doc',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student'),
        ),
        migrations.AlterField(
            model_name='fin_exam_doc',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student'),
        ),
        migrations.AlterField(
            model_name='pre_exam_doc',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student'),
        ),
        migrations.AlterField(
            model_name='t_d_doc',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student'),
        ),
        migrations.AlterField(
            model_name='t_d_prop_doc',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='KumoGT.Student'),
        ),
    ]
