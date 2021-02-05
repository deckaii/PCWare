# Generated by Django 3.1.5 on 2021-02-04 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PCStore', '0002_address_payment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cartID', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderID', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.user')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('orderItemID', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.order')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('cartItemID', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('cartID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.cart')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='orderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.order'),
        ),
        migrations.AddField(
            model_name='cart',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PCStore.user'),
        ),
    ]