# Generated by Django 2.1.5 on 2019-05-31 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('pan', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('Year_of_filing', models.IntegerField()),
                ('Aadhar', models.IntegerField()),
                ('Mobile_no', models.IntegerField()),
                ('DOB', models.DateField()),
                ('Fname', models.CharField(max_length=200)),
                ('Mname', models.CharField(max_length=200)),
                ('Lname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Capital_gain',
            fields=[
                ('Asset_amount', models.IntegerField()),
                ('pan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tax.user')),
                ('Asset_type', models.CharField(choices=[('HOUSE', 'HOUSE'), ('FIXED DEPOSIT', 'FIXED DEPOSIT'), ('SHARES', 'SHARES'), ('CASH IN HAND', 'CASH IN HAND'), ('LAND PROPERTY', 'LAND PROPERTY')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('pan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tax.user')),
                ('Life_insurance', models.IntegerField()),
                ('PPF', models.IntegerField()),
                ('NSC', models.IntegerField()),
                ('Tax_saving_fd', models.IntegerField()),
                ('Stamp_duty_reg', models.IntegerField()),
                ('EPF', models.IntegerField()),
                ('ELSS', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Income_Tax_Slab',
            fields=[
                ('Age_Category', models.CharField(choices=[('<18', '<18'), ('18-35', '18-35'), ('35-60', '35-60'), ('>60', '>60')], max_length=20)),
                ('Income_Category', models.CharField(choices=[('<5,00,000', '<5,00,000'), ('5,00,001-20,00,000', '5,00,001-20,00,000'), ('>20,00,000', '>20,00,000')], max_length=20)),
                ('pan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tax.user')),
                ('Tax_percentage', models.IntegerField(choices=[(5, '<5,00,000: 5'), (15, '5,00,001-20,00,000: 15'), (30, '>20,00,000: 30')])),
            ],
        ),
        migrations.CreateModel(
            name='Other_Income',
            fields=[
                ('pan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tax.user')),
                ('Savings', models.IntegerField()),
                ('Rent', models.IntegerField()),
                ('FD', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('Standard_Deduction', models.IntegerField()),
                ('Special_allowance', models.IntegerField()),
                ('HRA', models.IntegerField()),
                ('Basic_salary', models.IntegerField()),
                ('pan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tax.user')),
            ],
        ),
        migrations.CreateModel(
            name='tax_on_capital_gain',
            fields=[
                ('Gain_category', models.CharField(choices=[('HIGH', 'HIGH'), ('LOW', 'LOW')], max_length=20)),
                ('Asset_type', models.CharField(choices=[('HOUSE', 'HOUSE'), ('FIXED DEPOSIT', 'FIXED DEPOSIT'), ('SHARES', 'SHARES'), ('CASH IN HAND', 'CASH IN HAND'), ('LAND PROPERTY', 'LAND PROPERTY')], max_length=20)),
                ('Holding_period', models.IntegerField()),
                ('Tax_percentage', models.IntegerField(choices=[(15, 'HOUSE: 15'), (12, 'FIXED DEPOSIT: 12'), (10, 'SHARES/CASH IN HAND: 10'), (14, 'LAND PROPERTY: 14')])),
                ('pan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tax.user')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='other_income',
            unique_together={('pan', 'Savings')},
        ),
        migrations.AlterUniqueTogether(
            name='income_tax_slab',
            unique_together={('pan',)},
        ),
    ]
