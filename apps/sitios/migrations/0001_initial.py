# Generated by Django 5.0.2 on 2024-02-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AGG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ATT_ID_A', models.TextField(max_length=50)),
                ('TX_A', models.TextField(max_length=50)),
                ('TX_GRUPOS_A', models.TextField(max_length=50)),
                ('TX_DETALLE_A', models.TextField(max_length=50)),
                ('CONTROL', models.TextField(max_length=50)),
                ('FECHA', models.TextField(max_length=50)),
                ('POC', models.TextField(max_length=50)),
                ('OBSERVACIONES', models.TextField(max_length=50)),
                ('TRACKER', models.TextField(max_length=50)),
                ('ID_ATT', models.TextField(max_length=50)),
                ('NOMBRE', models.TextField(max_length=50)),
                ('LATITUD', models.TextField(max_length=50)),
                ('LONGITUD', models.TextField(max_length=50)),
                ('ESTADO', models.TextField(max_length=50)),
                ('MUNICIPIO', models.TextField(max_length=50)),
                ('MERCADO', models.TextField(max_length=50)),
                ('MERCADO_FO', models.TextField(max_length=50)),
                ('REGION_CELULAR', models.TextField(max_length=50)),
                ('AGREGADOR', models.TextField(max_length=50)),
                ('AÑO', models.TextField(max_length=50)),
                ('PROYECTO', models.TextField(max_length=50)),
                ('TOPOLOGIA', models.TextField(max_length=50)),
                ('SEGMENTO_IPBH', models.TextField(max_length=50)),
                ('STATUS', models.TextField(max_length=50)),
                ('TX_FO', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'agregadores',
            },
        ),
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT_C', models.TextField(max_length=50)),
                ('TX', models.TextField(max_length=50)),
                ('TX_GRUPOS', models.TextField(max_length=50)),
                ('TX_DETALLE', models.TextField(max_length=50)),
                ('CONTROL', models.TextField(max_length=50)),
                ('FECHA_ALTA_BAJA', models.TextField(max_length=50)),
                ('POC', models.TextField(max_length=50)),
                ('OBSERVACIONES', models.TextField(max_length=50)),
                ('TX_CARRIER', models.TextField(max_length=50)),
                ('PROYECTO_FO', models.TextField(max_length=50)),
                ('SEGUNDO_PUERTO_HABILITADO', models.TextField(max_length=50)),
                ('CID_CARRIER', models.TextField(max_length=50)),
                ('REGION', models.TextField(max_length=50)),
                ('MERCADO', models.TextField(max_length=50)),
                ('PUNTA_A_NAMING_CONVECTION', models.TextField(max_length=50)),
                ('PUNTA_A_ID_SITIO', models.TextField(max_length=50)),
                ('PUNTA_A_NOMBRE_SITIO', models.TextField(max_length=50)),
                ('LATITUD_PUNTA_A', models.TextField(max_length=50)),
                ('LONGITUD_PUNTA_A', models.TextField(max_length=50)),
                ('PUNTA_B_NAMING_CONVECTION', models.TextField(max_length=50)),
                ('PUNTA_B_ID_SITIO', models.TextField(max_length=50)),
                ('PUNTA_B_NOMBRE_SITIO', models.TextField(max_length=50)),
                ('LATITUD_PUNTA_B', models.TextField(max_length=50)),
                ('LONGITUD_PUNTA_B', models.TextField(max_length=50)),
                ('CARRIER', models.TextField(max_length=50)),
                ('TIPO_ENLACE', models.TextField(max_length=50)),
                ('PROYECTO_PRINCIPAL', models.TextField(max_length=50)),
                ('FASE', models.TextField(max_length=50)),
                ('CAPACIDAD_MBPS', models.TextField(max_length=50)),
                ('ESTATUS', models.TextField(max_length=50)),
                ('TRACKER', models.TextField(max_length=50)),
                ('ATT_ID', models.TextField(max_length=50)),
                ('NOMBRE', models.TextField(max_length=50)),
                ('CONTROL_DE_CAMBIOS_RAN', models.TextField(max_length=50)),
                ('BASE_ORIGEN_TX', models.TextField(max_length=50)),
                ('GRUPOS_MEDIO_TX', models.TextField(max_length=50)),
                ('TX_DETALLE_2', models.TextField(max_length=50)),
                ('BASE_ORIGEN_PROYECCION', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'carrier',
            },
        ),
        migrations.CreateModel(
            name='FibraOptica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT_F', models.CharField(max_length=50)),
                ('TX', models.CharField(max_length=50)),
                ('TX_GRUPOS', models.CharField(max_length=50)),
                ('TX_DETALLE', models.CharField(max_length=50)),
                ('CONTROL', models.CharField(max_length=50)),
                ('FECHA', models.DateField(max_length=50)),
                ('POC', models.CharField(max_length=50)),
                ('OBSERVACIONES', models.CharField(max_length=50)),
                ('TRACKER', models.CharField(max_length=50)),
                ('ATT_ID', models.CharField(max_length=50)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('LATITUD', models.CharField(max_length=50)),
                ('LONGITUD', models.CharField(max_length=50)),
                ('ESTADO', models.CharField(max_length=50)),
                ('MUNICIPIO', models.CharField(max_length=50)),
                ('MERCADO', models.TextField(max_length=50)),
                ('MERCADO_FO', models.TextField(max_length=50)),
                ('REGION_CELULAR', models.TextField(max_length=50)),
                ('AGREGADOR', models.TextField(max_length=50)),
                ('AÑO', models.TextField(max_length=50)),
                ('PROYECTO', models.TextField(max_length=50)),
                ('TOPOLOGIA', models.TextField(max_length=50)),
                ('SEGMENTO_IPBH', models.TextField(max_length=50)),
                ('STATUS', models.TextField(max_length=50)),
                ('TX_FO', models.TextField(max_length=50)),
            ],
            options={
                'verbose_name': 'Fibra',
                'verbose_name_plural': 'Fibras',
                'db_table': 'fibraoptica',
            },
        ),
        migrations.CreateModel(
            name='Migracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT_M', models.TextField(max_length=50)),
                ('ORIGEN_TX', models.TextField(max_length=50)),
                ('TX_GRUPOS', models.TextField(max_length=50)),
                ('TX_DETALLE', models.TextField(max_length=50)),
                ('CONTROL', models.TextField(max_length=50)),
                ('FECHA', models.TextField(max_length=50)),
                ('POC', models.TextField(max_length=50)),
                ('OBSERVACIONES', models.TextField(max_length=50)),
                ('ID_PANDA', models.TextField(max_length=50)),
                ('ID_ATT', models.TextField(max_length=50)),
                ('SITE_NAME', models.TextField(max_length=50)),
                ('MARKET', models.TextField(max_length=50)),
                ('PROYECTO', models.TextField(max_length=50)),
                ('REAL_MIGRACION', models.TextField(max_length=50)),
                ('SCOPE', models.TextField(max_length=50)),
                ('PANDA', models.TextField(max_length=50)),
                ('STATUS', models.TextField(max_length=50)),
                ('TX_TYPE', models.TextField(max_length=50)),
                ('ATT_ID', models.TextField(max_length=50)),
                ('LATITUD', models.TextField(max_length=50)),
                ('LONGITUD', models.TextField(max_length=50)),
                ('ESTADO', models.TextField(max_length=50)),
                ('MUNICIPIO', models.TextField(max_length=50)),
                ('MERCADO', models.TextField(max_length=50)),
                ('REGION_CELULAR', models.TextField(max_length=50)),
                ('CLASIFICACION', models.TextField(max_length=50)),
                ('CONTROL_DE_CAMBIOS_RAN', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'migracion',
            },
        ),
        migrations.CreateModel(
            name='MW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ATT_ID_MW', models.TextField(max_length=50)),
                ('TX_MW', models.TextField(max_length=50)),
                ('TX_GRUPOS_MW', models.TextField(max_length=50)),
                ('TX_DETALLE_MW', models.TextField(max_length=50)),
                ('CONROL', models.TextField(max_length=50)),
                ('POC', models.TextField(max_length=50)),
                ('NOMBRE', models.TextField(max_length=50)),
                ('LATITUD', models.TextField(max_length=50)),
                ('LONGITUD', models.TextField(max_length=50)),
                ('ESTADO', models.TextField(max_length=50)),
                ('MUNICIPIO', models.TextField(max_length=50)),
                ('MERCADO', models.TextField(max_length=50)),
                ('REGION_CELULAR', models.TextField(max_length=50)),
                ('CONTROL_DE_CAMBIOS_RAN', models.TextField(max_length=50)),
                ('PROYECTO_MIGRADOS', models.TextField(max_length=50)),
                ('REAL_MIGRACION', models.TextField(max_length=50)),
                ('TX_ORIGEN', models.TextField(max_length=50)),
                ('MEDIO_TX_GRUPOS', models.TextField(max_length=50)),
                ('TX_DETALLE', models.TextField(max_length=50)),
                ('PANDA', models.TextField(max_length=50)),
                ('STATUS', models.TextField(max_length=50)),
                ('TX_TYPE', models.TextField(max_length=50)),
                ('CAPACIDAD_1G', models.TextField(max_length=50)),
                ('SITIO_A', models.TextField(max_length=50)),
                ('SITIO_B', models.TextField(max_length=50)),
                ('ENLACE', models.TextField(max_length=50)),
                ('TECNOLOGIA', models.TextField(max_length=50)),
                ('AGREGADOR_GRUPO', models.TextField(max_length=50)),
                ('AGREGADOR_DETALLE', models.TextField(max_length=50)),
                ('TRACKER', models.TextField(max_length=50)),
                ('ATTID_1', models.TextField(max_length=50)),
                ('SITE_A', models.TextField(max_length=50)),
                ('SITE_B', models.TextField(max_length=50)),
                ('LINK', models.TextField(max_length=50)),
                ('AGREGADOR', models.TextField(max_length=50)),
                ('SITE_1', models.TextField(max_length=50)),
                ('SITE_2', models.TextField(max_length=50)),
                ('SITE_3', models.TextField(max_length=50)),
                ('SITE_4', models.TextField(max_length=50)),
                ('SITE_5', models.TextField(max_length=50)),
                ('SITE_6', models.TextField(max_length=50)),
                ('SITE_7', models.TextField(max_length=50)),
                ('SITE_8', models.TextField(max_length=50)),
                ('SITE_9', models.TextField(max_length=50)),
                ('SITE_10', models.TextField(max_length=50)),
                ('SITIOS_CARGA', models.TextField(max_length=50)),
                ('TIPO', models.TextField(max_length=50)),
                ('ATTID_2', models.TextField(max_length=50)),
                ('TECNOLOGIA_ACTUAL', models.TextField(max_length=50)),
                ('CAPACIDAD_MBPS', models.TextField(max_length=50)),
                ('UTILIZACION_MBPS', models.TextField(max_length=50)),
                ('FLAG_H', models.TextField(max_length=50)),
                ('NUMERO_DE_CERTIFICADO', models.TextField(max_length=50)),
                ('NUMERO_DE_LINK', models.TextField(max_length=50)),
                ('IDENTIFICADOR_CERTIFICADO', models.TextField(max_length=50)),
                ('CONCESIONARIO', models.TextField(max_length=50)),
                ('RESPONSABLE_CONS', models.TextField(max_length=50)),
                ('DIRECCION_CONS', models.TextField(max_length=50)),
                ('TELEFONO_CONS', models.TextField(max_length=50)),
                ('E_MAIL_CONS', models.TextField(max_length=50)),
                ('USUARIO_FINAL', models.TextField(max_length=50)),
                ('RESPONSABLE_US', models.TextField(max_length=50)),
                ('DIRECCION_US', models.TextField(max_length=50)),
                ('TELEFONO_US', models.TextField(max_length=50)),
                ('E_MAIL_US', models.TextField(max_length=50)),
                ('FECHA_SOLICITUD', models.TextField(max_length=50)),
                ('FECHA_CONSTANCIA', models.TextField(max_length=50)),
                ('FECHA_DE_CANCELACION', models.TextField(max_length=50)),
                ('MOTIVO', models.TextField(max_length=50)),
                ('NOMBRE_A', models.TextField(max_length=50)),
                ('DOMICILIO_A', models.TextField(max_length=50)),
                ('CIUDAD_A', models.TextField(max_length=50)),
                ('CLAVE_ESTADO_A', models.TextField(max_length=50)),
                ('LATITUD_GRAD_A', models.TextField(max_length=50)),
                ('LATITUD_MIN_A', models.TextField(max_length=50)),
                ('LATITUD_SEG_A', models.TextField(max_length=50)),
                ('LONGITUD_GRAD_A', models.TextField(max_length=50)),
                ('LONGITUD_MIN_A', models.TextField(max_length=50)),
                ('LONGITUD_SEG_A', models.TextField(max_length=50)),
                ('ASNM_A', models.TextField(max_length=50)),
                ('AZIMUT_A', models.TextField(max_length=50)),
                ('NOMBRE_B', models.TextField(max_length=50)),
                ('DOMICILIO_B', models.TextField(max_length=50)),
                ('CIUDAD_B', models.TextField(max_length=50)),
                ('CLAVE_ESTADO_B', models.TextField(max_length=50)),
                ('LATITUD_GRAD_B', models.TextField(max_length=50)),
                ('LATITUD_MIN_B', models.TextField(max_length=50)),
                ('LATITUD_SEG_B', models.TextField(max_length=50)),
                ('LONGITUD_GRAD_B', models.TextField(max_length=50)),
                ('LONGITUD_MIN_B', models.TextField(max_length=50)),
                ('LONGITUD_SEG_B', models.TextField(max_length=50)),
                ('ASNM_B', models.TextField(max_length=50)),
                ('AZIMUT_B', models.TextField(max_length=50)),
                ('LONGITUD_ENLACE', models.TextField(max_length=50)),
                ('BANDA_FRECUENCIA', models.TextField(max_length=50)),
                ('FRECUENCIA_TX', models.TextField(max_length=50)),
                ('FRECUENCIA_RX', models.TextField(max_length=50)),
                ('MARCA_RADIO', models.TextField(max_length=50)),
                ('MODELO_RADIO', models.TextField(max_length=50)),
                ('MODULACION', models.TextField(max_length=50)),
                ('EMISION', models.TextField(max_length=50)),
                ('ANCHO_BANDA', models.TextField(max_length=50)),
                ('TX_PLANNED', models.TextField(max_length=50)),
                ('SEPARACION_CANAL', models.TextField(max_length=50)),
                ('SUB_BANDA_OP', models.TextField(max_length=50)),
                ('SEPARACION_DUPLEX', models.TextField(max_length=50)),
                ('UMBRA_RECEPCION', models.TextField(max_length=50)),
                ('TASA_DE_BITS_UMBRAL', models.TextField(max_length=50)),
                ('PIRE', models.TextField(max_length=50)),
                ('PIRE_A', models.TextField(max_length=50)),
                ('PIRE_B', models.TextField(max_length=50)),
                ('VELOCIDAD_TX', models.TextField(max_length=50)),
                ('CAPACIDAD_CANALES', models.TextField(max_length=50)),
                ('HOMOLOGACION_EQUIPO', models.TextField(max_length=50)),
                ('CONFIGURACION_ENLACE', models.TextField(max_length=50)),
                ('ANTENA_TIPO_A', models.TextField(max_length=50)),
                ('ANTENA_MARCA_A', models.TextField(max_length=50)),
                ('ANTENA_MODELO_A', models.TextField(max_length=50)),
                ('ANTENA_DIAMETRO_A', models.TextField(max_length=50)),
                ('ANTENA_GANANCIA_A', models.TextField(max_length=50)),
                ('ANTENA_POLARIZACION_A', models.TextField(max_length=50)),
                ('ANTENA_ANGULO_ABERTURA_A', models.TextField(max_length=50)),
                ('ANTENA_ANGULO_ELEVACION_A', models.TextField(max_length=50)),
                ('MODELO_RADIO_B', models.TextField(max_length=50)),
                ('ANTENA_TIPO_B', models.TextField(max_length=50)),
                ('ANTENA_MARCA_B', models.TextField(max_length=50)),
                ('ANTENA_MODELO_B', models.TextField(max_length=50)),
                ('ANTENA_DIAMETRO_B', models.TextField(max_length=50)),
                ('ANTENA_GANANCIA_B', models.TextField(max_length=50)),
                ('ANTENA_POLARIZACION_B', models.TextField(max_length=50)),
                ('ANTENA_ANGULO_ABERTURA_B', models.TextField(max_length=50)),
                ('ANTENA_ANGULO_ELEVACION_B', models.TextField(max_length=50)),
                ('LINEA_MARCA_A', models.TextField(max_length=50)),
                ('LINEA_TIPO_A', models.TextField(max_length=50)),
                ('LINEA_LONGITUD_A', models.TextField(max_length=50)),
                ('LINEA_ATENUACION_A', models.TextField(max_length=50)),
                ('OTRAS_PERDIDAS_TX_A', models.TextField(max_length=50)),
                ('OTRAS_PERDIDAS_RX_A', models.TextField(max_length=50)),
                ('LINEA_MARCA_B', models.TextField(max_length=50)),
                ('LINEA_TIPO_B', models.TextField(max_length=50)),
                ('LINEA_LONGITUD_B', models.TextField(max_length=50)),
                ('LINEA_ATENUACION_B', models.TextField(max_length=50)),
                ('OTRAS_PERDIDAS_TX_B', models.TextField(max_length=50)),
                ('OTRAS_PERDIDAS_RX_B', models.TextField(max_length=50)),
                ('EDIFICIO_ALTURA_A', models.TextField(max_length=50)),
                ('TORRE_ALTURA_A', models.TextField(max_length=50)),
                ('TORRE_ANTENA_ALTURA_A', models.TextField(max_length=50)),
                ('TORRE_TIPO_A', models.TextField(max_length=50)),
                ('EDIFICIO_ALTURA_B', models.TextField(max_length=50)),
                ('TORRE_ALTURA_B', models.TextField(max_length=50)),
                ('TORRE_ANTENA_ALTURA_B', models.TextField(max_length=50)),
                ('TORRE_TIPO_B', models.TextField(max_length=50)),
                ('POT_TX_A', models.TextField(max_length=50)),
                ('RX_PLANNED_A', models.TextField(max_length=50)),
                ('POTE_TX_B', models.TextField(max_length=50)),
                ('RX_PLANNED_B', models.TextField(max_length=50)),
                ('NO_CHANNEL', models.TextField(max_length=50)),
                ('CHANNEL_ID_A', models.TextField(max_length=50)),
                ('CHANNEL_ID_B', models.TextField(max_length=50)),
                ('CONFIGURACION', models.TextField(max_length=50)),
                ('PROYECTO', models.TextField(max_length=50)),
                ('SOLICITUD', models.TextField(max_length=50)),
                ('ELLIPSE', models.TextField(max_length=50)),
                ('GOOGLE', models.TextField(max_length=50)),
                ('ORDEN_DE_TRABAJO', models.TextField(max_length=50)),
                ('CONTRATISTA', models.TextField(max_length=50)),
                ('PROTOCOLO_DE_RECEPCION', models.TextField(max_length=50)),
                ('RX_MED_A', models.TextField(max_length=50)),
                ('RX_MED_B', models.TextField(max_length=50)),
                ('GESTION', models.TextField(max_length=50)),
                ('IPLOCAL', models.TextField(max_length=50)),
                ('IP_REMOTO', models.TextField(max_length=50)),
                ('NO_SERIE_IDU_LOCAL', models.TextField(max_length=50)),
                ('NO_SERIE_ODU_LOCAL', models.TextField(max_length=50)),
                ('NO_SERIE_IDU_REMOTO', models.TextField(max_length=50)),
                ('NO_SERIE_ODU_REMOTO', models.TextField(max_length=50)),
                ('OBSERVACIONES', models.TextField(max_length=50)),
                ('INGENIERIA', models.TextField(max_length=50)),
                ('DESMONTAJES', models.TextField(max_length=50)),
                ('FECHA', models.TextField(max_length=50)),
                ('RESPONSABLE', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'microondas',
            },
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ATT_P', models.TextField(max_length=50)),
                ('TX', models.TextField(max_length=50)),
                ('TX_GRUPOS_PROYECCION', models.TextField(max_length=50)),
                ('TX_DETALLE_PROYECCION', models.TextField(max_length=50)),
                ('CONTROL', models.TextField(max_length=50)),
                ('AÑO_PROYECCION', models.TextField(max_length=50)),
                ('FECHA', models.TextField(max_length=50)),
                ('POC', models.TextField(max_length=50)),
                ('OBSERVACIONES', models.TextField(max_length=50)),
                ('TRACKER', models.TextField(max_length=50)),
                ('ATT_ID', models.TextField(max_length=50)),
                ('NOMBRE', models.TextField(max_length=50)),
                ('LATITUD', models.TextField(max_length=50)),
                ('LONGITUD', models.TextField(max_length=50)),
                ('ESTADO', models.TextField(max_length=50)),
                ('MUNICIPIO', models.TextField(max_length=50)),
                ('MERCADO', models.TextField(max_length=50)),
                ('MERCADO_FO', models.TextField(max_length=50)),
                ('REGION_CELULAR', models.TextField(max_length=50)),
                ('AGREGADOR', models.TextField(max_length=50)),
                ('AÑO', models.TextField(max_length=50)),
                ('PROYECTO', models.TextField(max_length=50)),
                ('TOPOLOGIA', models.TextField(max_length=50)),
                ('SEGMENTO_IPBH', models.TextField(max_length=50)),
                ('STATUS', models.TextField(max_length=50)),
                ('TX_F', models.TextField(max_length=50)),
            ],
            options={
                'db_table': 'proyeccion',
            },
        ),
        migrations.CreateModel(
            name='SitiosTotales',
            fields=[
                ('TRACKER', models.CharField(max_length=50)),
                ('S_ATT_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('ID_LITE', models.CharField(max_length=50)),
                ('ID_ROJO', models.CharField(max_length=50)),
                ('ID_NARANJA', models.CharField(max_length=50)),
                ('IDEN', models.CharField(max_length=50)),
                ('LATITUD', models.CharField(max_length=50)),
                ('LONGITUD', models.CharField(max_length=50)),
                ('ESTADO', models.CharField(max_length=50)),
                ('MUNICIPIO', models.CharField(max_length=50)),
                ('MERCADO', models.CharField(max_length=50)),
                ('REGION_CELULAR', models.CharField(max_length=50)),
                ('REGION', models.CharField(max_length=50)),
                ('VENDOR', models.CharField(max_length=50)),
                ('COBERTURA', models.CharField(max_length=50)),
                ('TIPO', models.CharField(max_length=50)),
                ('PROYECTO', models.CharField(max_length=50)),
                ('CLASIFICACION', models.CharField(max_length=50)),
                ('TECNOLOGIA', models.CharField(max_length=50)),
                ('CONFIGURACION_3G', models.CharField(max_length=50)),
                ('CONFIGURACION_4G', models.CharField(max_length=50)),
                ('CONFIGURACION_5G', models.CharField(max_length=50)),
                ('IOT', models.CharField(max_length=50)),
                ('TDD', models.CharField(max_length=50)),
                ('TRAFICO_3G_LTE_5G', models.CharField(max_length=50)),
                ('TRAFICO_3G', models.CharField(max_length=50)),
                ('TRAFICO_4G', models.CharField(max_length=50)),
                ('TRAFICO_5G', models.CharField(max_length=50)),
                ('SL', models.CharField(max_length=50)),
                ('REUBICACION', models.CharField(max_length=50)),
                ('COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('PLAN', models.CharField(max_length=50)),
                ('ENE_3G_B5_850', models.CharField(max_length=50)),
                ('ENE_3G_B2_PCS', models.CharField(max_length=50)),
                ('ENE_3G_B4_AWS', models.CharField(max_length=50)),
                ('ENE_LTE_B26_800', models.CharField(max_length=50)),
                ('ENE_LTE_B5_850', models.CharField(max_length=50)),
                ('ENE_LTE_B2_PCS', models.CharField(max_length=50)),
                ('ENE_LTE_B4_AWS', models.CharField(max_length=50)),
                ('ENE_LTE_B7_2600', models.CharField(max_length=50)),
                ('ENE_LTE_B38_2600', models.CharField(max_length=50)),
                ('ENE_5G_B7_2600', models.CharField(max_length=50)),
                ('ENE_5G_B38_2600', models.CharField(max_length=50)),
                ('ENE_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('ENE_PLAN', models.CharField(max_length=50)),
                ('FEB_3G_B5_850', models.CharField(max_length=50)),
                ('FEB_3G_B2_PCS', models.CharField(max_length=50)),
                ('FEB_3G_B4_AWS', models.CharField(max_length=50)),
                ('FEB_LTE_B26_800', models.CharField(max_length=50)),
                ('FEB_LTE_B5_850', models.CharField(max_length=50)),
                ('FEB_LTE_B2_PCS', models.CharField(max_length=50)),
                ('FEB_LTE_B4_AWS', models.CharField(max_length=50)),
                ('FEB_LTE_B7_2600', models.CharField(max_length=50)),
                ('FEB_LTE_B38_2600', models.CharField(max_length=50)),
                ('FEB_5G_B7_2600', models.CharField(max_length=50)),
                ('FEB_5G_B38_2600', models.CharField(max_length=50)),
                ('FEB_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('FEB_PLAN', models.CharField(max_length=50)),
                ('MAR_3G_B5_850', models.CharField(max_length=50)),
                ('MAR_3G_B2_PCS', models.CharField(max_length=50)),
                ('MAR_3G_B4_AWS', models.CharField(max_length=50)),
                ('MAR_LTE_B26_800', models.CharField(max_length=50)),
                ('MAR_LTE_B5_850', models.CharField(max_length=50)),
                ('MAR_LTE_B2_PCS', models.CharField(max_length=50)),
                ('MAR_LTE_B4_AWS', models.CharField(max_length=50)),
                ('MAR_LTE_B7_2600', models.CharField(max_length=50)),
                ('MAR_LTE_B38_2600', models.CharField(max_length=50)),
                ('MAR_5G_B7_2600', models.CharField(max_length=50)),
                ('MAR_5G_B38_2600', models.CharField(max_length=50)),
                ('MAR_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('MAR_PLAN', models.CharField(max_length=50)),
                ('ABR_3G_B5_850', models.CharField(max_length=50)),
                ('ABR_3G_B2_PCS', models.CharField(max_length=50)),
                ('ABR_3G_B4_AWS', models.CharField(max_length=50)),
                ('ABR_LTE_B26_800', models.CharField(max_length=50)),
                ('ABR_LTE_B5_850', models.CharField(max_length=50)),
                ('ABR_LTE_B2_PCS', models.CharField(max_length=50)),
                ('ABR_LTE_B4_AWS', models.CharField(max_length=50)),
                ('ABR_LTE_B7_2600', models.CharField(max_length=50)),
                ('ABR_LTE_B38_2600', models.CharField(max_length=50)),
                ('ABR_5G_B7_2600', models.CharField(max_length=50)),
                ('ABR_5G_B38_2600', models.CharField(max_length=50)),
                ('ABR_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('ABR_PLAN', models.CharField(max_length=50)),
                ('MAY_3G_B5_850', models.CharField(max_length=50)),
                ('MAY_3G_B2_PCS', models.CharField(max_length=50)),
                ('MAY_3G_B4_AWS', models.CharField(max_length=50)),
                ('MAY_LTE_B26_800', models.CharField(max_length=50)),
                ('MAY_LTE_B5_850', models.CharField(max_length=50)),
                ('MAY_LTE_B2_PCS', models.CharField(max_length=50)),
                ('MAY_LTE_B4_AWS', models.CharField(max_length=50)),
                ('MAY_LTE_B7_2600', models.CharField(max_length=50)),
                ('MAY_LTE_B38_2600', models.CharField(max_length=50)),
                ('MAY_5G_B7_2600', models.CharField(max_length=50)),
                ('MAY_5G_B38_2600', models.CharField(max_length=50)),
                ('MAY_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('MAY_PLAN', models.CharField(max_length=50)),
                ('JUN_3G_B5_850', models.CharField(max_length=50)),
                ('JUN_3G_B2_PCS', models.CharField(max_length=50)),
                ('JUN_3G_B4_AWS', models.CharField(max_length=50)),
                ('JUN_LTE_B26_800', models.CharField(max_length=50)),
                ('JUN_LTE_B5_850', models.CharField(max_length=50)),
                ('JUN_LTE_B2_PCS', models.CharField(max_length=50)),
                ('JUN_LTE_B4_AWS', models.CharField(max_length=50)),
                ('JUN_LTE_B7_2600', models.CharField(max_length=50)),
                ('JUN_LTE_B38_2600', models.CharField(max_length=50)),
                ('JUN_5G_B7_2600', models.CharField(max_length=50)),
                ('JUN_5G_B38_2600', models.CharField(max_length=50)),
                ('JUN_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('JUN_PLAN', models.CharField(max_length=50)),
                ('JUL_3G_B5_850', models.CharField(max_length=50)),
                ('JUL_3G_B2_PCS', models.CharField(max_length=50)),
                ('JUL_3G_B4_AWS', models.CharField(max_length=50)),
                ('JUL_LTE_B26_800', models.CharField(max_length=50)),
                ('JUL_LTE_B5_850', models.CharField(max_length=50)),
                ('JUL_LTE_B2_PCS', models.CharField(max_length=50)),
                ('JUL_LTE_B4_AWS', models.CharField(max_length=50)),
                ('JUL_LTE_B7_2600', models.CharField(max_length=50)),
                ('JUL_LTE_B38_2600', models.CharField(max_length=50)),
                ('JUL_5G_B7_2600', models.CharField(max_length=50)),
                ('JUL_5G_B38_2600', models.CharField(max_length=50)),
                ('JUL_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('JUL_PLAN', models.CharField(max_length=50)),
                ('AGO_3G_B5_850', models.CharField(max_length=50)),
                ('AGO_3G_B2_PCS', models.CharField(max_length=50)),
                ('AGO_3G_B4_AWS', models.CharField(max_length=50)),
                ('AGO_LTE_B26_800', models.CharField(max_length=50)),
                ('AGO_LTE_B5_850', models.CharField(max_length=50)),
                ('AGO_LTE_B2_PCS', models.CharField(max_length=50)),
                ('AGO_LTE_B4_AWS', models.CharField(max_length=50)),
                ('AGO_LTE_B7_2600', models.CharField(max_length=50)),
                ('AGO_LTE_B38_2600', models.CharField(max_length=50)),
                ('AGO_LTE_B42_3500', models.CharField(max_length=50)),
                ('AGO_5G_B7_2600', models.CharField(max_length=50)),
                ('AGO_5G_B38_2600', models.CharField(max_length=50)),
                ('AGO_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('AGO_PLAN', models.CharField(max_length=50)),
                ('SEP_3G_B5_850', models.CharField(max_length=50)),
                ('SEP_3G_B2_PCS', models.CharField(max_length=50)),
                ('SEP_3G_B4_AWS', models.CharField(max_length=50)),
                ('SEP_LTE_B26_800', models.CharField(max_length=50)),
                ('SEP_LTE_B5_850', models.CharField(max_length=50)),
                ('SEP_LTE_B2_PCS', models.CharField(max_length=50)),
                ('SEP_LTE_B4_AWS', models.CharField(max_length=50)),
                ('SEP_LTE_B7_2600', models.CharField(max_length=50)),
                ('SEP_LTE_B38_2600', models.CharField(max_length=50)),
                ('SEP_LTE_B42_3500', models.CharField(max_length=50)),
                ('SEP_5G_B7_2600', models.CharField(max_length=50)),
                ('SEP_5G_B38_2600', models.CharField(max_length=50)),
                ('SEP_COMENTARIO_OPERACIONES', models.CharField(max_length=50)),
                ('SEP_PLAN', models.CharField(max_length=50)),
                ('OCT_3G_B5_850', models.CharField(max_length=50)),
                ('OCT_3G_B2_PCS', models.CharField(max_length=50)),
                ('OCT_3G_B4_AWS', models.CharField(max_length=50)),
                ('OCT_LTE_B26_800', models.CharField(max_length=50)),
                ('OCT_LTE_B5_850', models.CharField(max_length=50)),
                ('OCT_LTE_B2_PCS', models.CharField(max_length=50)),
                ('OCT_LTE_B4_AWS', models.CharField(max_length=50)),
                ('OCT_LTE_B7_2600', models.CharField(max_length=50)),
                ('OCT_LTE_B38_2600', models.CharField(max_length=50)),
                ('OCT_LTE_B42_3500', models.CharField(max_length=50)),
                ('OCT_5G_B7_2600', models.CharField(max_length=50)),
                ('OCT_5G_B38_2600', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Sitio',
                'verbose_name_plural': 'Sitios',
                'db_table': 'sitiosTotales',
            },
        ),
    ]
