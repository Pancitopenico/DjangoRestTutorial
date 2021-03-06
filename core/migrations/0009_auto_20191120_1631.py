# Generated by Django 2.2.7 on 2019-11-20 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pontoturistico_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoIdentificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='cod_identificacao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.CodigoIdentificacao'),
        ),
    ]
