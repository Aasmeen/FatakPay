# Generated by Django 5.0.3 on 2024-03-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MASCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.IntegerField(db_column='nGrpNo', null=True)),
                ('category_name', models.CharField(blank=True, db_column='sGrpName', max_length=20)),
                ('system_code', models.CharField(blank=True, db_column='sSysNo', max_length=2, null=True)),
                ('program_code', models.CharField(blank=True, db_column='sPrgCode', max_length=8, null=True)),
            ],
            options={
                'verbose_name': 'a8.Category Master',
                'db_table': 'MASCAT',
                'ordering': ['category_code'],
            },
        ),
        migrations.CreateModel(
            name='MASDiv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_name', models.CharField(db_column='sBuName', max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='MASLan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(db_column='sLanguage', max_length=40)),
            ],
            options={
                'verbose_name': 'a9.Language',
                'db_table': 'MASLAN',
            },
        ),
        migrations.CreateModel(
            name='MASSlm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='sFrstNm', max_length=255)),
                ('last_name', models.CharField(blank=True, db_column='sLstNm', max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, db_column='sMobile', max_length=30, null=True)),
                ('telephone', models.CharField(blank=True, db_column='stelephn', max_length=30, null=True)),
                ('email', models.EmailField(db_column='eEmail', max_length=255)),
            ],
            options={
                'verbose_name': 'a6.Sales Person',
                'db_table': 'MASSLM',
            },
        ),
        migrations.CreateModel(
            name='MASUom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_of_measure', models.CharField(db_column='sUomName', max_length=5)),
                ('measure_type', models.CharField(choices=[('1', 'Count'), ('2', 'Area'), ('3', 'Volume'), ('4', 'Weight'), ('5', 'Time')], db_column='sUomType', default='1', max_length=1)),
                ('unit_desc', models.CharField(blank=True, db_column='sDesc', max_length=25)),
            ],
            options={
                'verbose_name': 'd1.UoM Master',
                'db_table': 'MASUOM',
            },
        ),
    ]
