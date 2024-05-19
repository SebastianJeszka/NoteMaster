import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Przedmiot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notatka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('tresc', models.TextField()),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True)),
                ('przedmiot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notatnik.przedmiot')),
            ],
        ),
    ]
