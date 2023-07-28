# Generated by Django 4.1.4 on 2023-07-27 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_project_checklist_delete_checklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_name', models.CharField(max_length=80, unique=True)),
                ('checklist_document', models.FileField(upload_to='Checklist_Documents/')),
                ('contract_period_months', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('main_contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to='tracker.contractor')),
                ('procurrement_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procuring_dpt', to='tracker.procurement_department')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='tracker.project')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Project_Checklist',
        ),
    ]
