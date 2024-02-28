# Generated by Django 5.0.2 on 2024-02-28 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT_PON', models.TextField()),
                ('TX_PON', models.TextField()),
                ('TX_GRUPOS_PON', models.TextField()),
                ('TX_DETALLE_PON', models.TextField()),
                ('CONTROL_PON', models.TextField()),
                ('FECHA_PON', models.TextField()),
                ('POC_PON', models.TextField()),
                ('OBSERVACIONES_PON', models.TextField()),
                ('REGION', models.TextField()),
                ('CIUDAD', models.TextField()),
                ('OLT_NAME_1', models.TextField()),
                ('OLT_ATT_ID', models.TextField()),
                ('OLT_IP', models.TextField()),
                ('OLT_NAME_2', models.TextField()),
                ('OLT_TYPE', models.TextField()),
                ('FRAME_ID', models.TextField()),
                ('SLOT_ID', models.TextField()),
                ('PORT_ID', models.TextField()),
                ('ONU_ID', models.TextField()),
                ('ONT_NAME', models.TextField()),
                ('ONT_OLD_NAME', models.TextField()),
                ('SITE_ID', models.TextField()),
                ('ID_ATT', models.TextField()),
                ('CON_SIN_SERVICIOS', models.TextField()),
                ('ONU_IP', models.TextField()),
                ('ONT_TYPE', models.TextField()),
                ('ONU_TYPE', models.TextField()),
                ('SN_MAC', models.TextField()),
                ('VENDOR', models.TextField()),
                ('RUNNIG_STATUS', models.TextField()),
                ('OPERATION_STATUS', models.TextField()),
            ],
            options={
                'db_table': 'pon',
            },
        ),
    ]
