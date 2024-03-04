# Generated by Django 5.0.2 on 2024-03-01 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0003_capacidadmanual_panda_tellus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semaforos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AGGREGATOR', models.TextField()),
                ('SITE_1', models.TextField()),
                ('SITE_2', models.TextField()),
                ('SITE_3', models.TextField()),
                ('SITE_4', models.TextField()),
                ('SITE_5', models.TextField()),
                ('SITE_6', models.TextField()),
                ('SITE_7', models.TextField()),
                ('SITE_8', models.TextField()),
                ('SITE_9', models.TextField()),
                ('SITE_10', models.TextField()),
                ('SITE_ID', models.TextField()),
                ('ATTID', models.TextField()),
                ('LINK', models.TextField()),
                ('TX_ACTUAL', models.TextField()),
                ('SITIOS_QUE_CARGA', models.TextField()),
                ('TECNOLOGIA_ACTUAL', models.TextField()),
                ('CAPACIDAD_MBPS', models.TextField()),
                ('CONFIGURACION', models.TextField()),
                ('ANCHO_DE_BANDA', models.TextField()),
                ('TX_A', models.TextField()),
                ('TX_B', models.TextField()),
                ('UTILIZACION_MBPS_1', models.TextField()),
                ('PORCENTAJE_UTILIZACION_PICOS_MAXIMOS', models.TextField()),
                ('FLAG_H', models.TextField()),
                ('UTILIZACION_MBPS_2', models.TextField()),
                ('PORCENTAJE_UTILIZACION_PICOS_MAXIMOS_2', models.TextField()),
                ('FLAG_V', models.TextField()),
                ('SITIOS', models.TextField()),
                ('SITE_FLOATING_MERCADO', models.TextField()),
                ('LINK_FLOATING_2023_MBPS', models.TextField()),
                ('FLAG_FLOATING_2023_MBPS', models.TextField()),
                ('PRIORIDAD_TAC_FLOATING_2023_MBPS', models.TextField()),
                ('SALUD_FLOATING_2023_MBPS', models.TextField()),
                ('PUNTO_AFECTACION_FLOATING_2023_MBPS', models.TextField()),
                ('SITE_FLOATING_MUNICIPIO', models.TextField()),
                ('LINK_FLOATING_2024_MBPS', models.TextField()),
                ('FLAG_FLOATING_2024_MBPS', models.TextField()),
                ('PRIORIDAD_TAC_FLOATING_2024_MBPS', models.TextField()),
                ('SALUD_FLOATING_2024_MBPS', models.TextField()),
                ('PUNTO_DE_AFECTACION_FLOATING_2024_MBPS', models.TextField()),
            ],
            options={
                'db_table': 'semaforos',
            },
        ),
    ]
