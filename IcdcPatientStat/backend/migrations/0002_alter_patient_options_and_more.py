# Generated by Django 4.2 on 2023-04-26 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="patient",
            options={"verbose_name": "Пациента", "verbose_name_plural": "Пациенты"},
        ),
        migrations.AlterField(
            model_name="cardiovascularsystem",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cs_collection",
                to="backend.patient",
                verbose_name="Пациент",
            ),
        ),
        migrations.AlterField(
            model_name="centralnervoussystem",
            name="patient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="cns_collection",
                to="backend.patient",
                verbose_name="Пациент",
            ),
        ),
        migrations.CreateModel(
            name="ImmuneSystem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "temperature",
                    models.FloatField(verbose_name="Температуры в градусах Цельсия"),
                ),
                (
                    "description",
                    models.CharField(
                        max_length=512, verbose_name="Описание результатов"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="is_collection",
                        to="backend.patient",
                        verbose_name="Пациент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись имунной системы ",
                "verbose_name_plural": "Записи имунной системы",
            },
        ),
    ]
