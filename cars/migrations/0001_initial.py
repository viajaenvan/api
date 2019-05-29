# Generated by Django 2.1.7 on 2019-05-29 03:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('models', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=10)),
                ('year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], max_length=4)),
                ('kind_of_car', models.IntegerField(choices=[(1, 'MINI VAN'), (2, 'VAN'), (3, 'TECHO ALTO')], max_length=2)),
                ('passenger_capacity', models.IntegerField(choices=[(6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16')], max_length=2)),
                ('kind_of_chairs', models.IntegerField(choices=[(1, 'OSCUROS'), (2, 'CLAROS')], max_length=2)),
                ('power_suppliers', models.PositiveIntegerField(default=0, max_length=3)),
                ('usb_ports', models.PositiveIntegerField(default=0, max_length=3)),
                ('air_conditioner', models.BooleanField()),
                ('glasses', models.IntegerField(choices=[(1, 'OSCUROS'), (2, 'CLAROS')], max_length=2)),
                ('luggage_carrier', models.IntegerField(choices=[(1, 'INTERNO'), (2, 'EXTERNO')], max_length=2)),
                ('wifi', models.BooleanField()),
                ('brand', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='brands.Brand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='models.Model')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
