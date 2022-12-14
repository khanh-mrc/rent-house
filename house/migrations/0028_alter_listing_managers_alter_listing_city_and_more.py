# Generated by Django 4.1.3 on 2022-12-18 08:11

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0027_listing_favourites_alter_listing_city'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='listing',
            managers=[
                ('newmanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Bà Rịa – Vũng Tàu', 'Bà Rịa – Vũng Tàu'), ('Vĩnh Long', 'Vĩnh Long'), ('Đà Nẵng', 'Đà Nẵng'), ('Sơn La', 'Sơn La'), ('Hòa Bình', 'Hòa Bình'), ('Khánh Hòa', 'Khánh Hòa'), ('Lâm Đồng', 'Lâm Đồng'), ('Quảng Ninh', 'Quảng Ninh'), ('Thái Bình', 'Thái Bình'), ('Nam Định', 'Nam Định'), ('An Giang', 'An Giang'), ('Kon Tum', 'Kon Tum'), ('Cao Bằng', 'Cao Bằng'), ('Cà Mau', 'Cà Mau'), ('Đồng Tháp', 'Đồng Tháp'), ('Đồng Nai', 'Đồng Nai'), ('Quảng Bình', 'Quảng Bình'), ('Cần Thơ', 'Cần Thơ'), ('Kiên Giang', 'Kiên Giang'), ('Bến Tre', 'Bến Tre'), ('Bình Thuận', 'Bình Thuận'), ('Điện Biên', 'Điện Biên'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Lào Cai', 'Lào Cai'), ('Trà Vinh', 'Trà Vinh'), ('Bắc Ninh', 'Bắc Ninh'), ('Lạng Sơn', 'Lạng Sơn'), ('Quảng Trị', 'Quảng Trị'), ('Phú Thọ', 'Phú Thọ'), ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Nghệ An', 'Nghệ An'), ('Lai Châu', 'Lai Châu'), ('Tây Ninh', 'Tây Ninh'), ('Hà Nội', 'Hà Nội'), ('Gia Lai', 'Gia Lai'), ('Bình Định', 'Bình Định'), ('Hà Nam', 'Hà Nam'), ('Bình Phước', 'Bình Phước'), ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'), ('Bạc Liêu', 'Bạc Liêu'), ('Hưng Yên', 'Hưng Yên'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Yên Bái', 'Yên Bái'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Đắk Nông', 'Đắk Nông'), ('Tuyên Quang', 'Tuyên Quang'), ('Bắc Giang', 'Bắc Giang'), ('Hải Dương', 'Hải Dương'), ('Bắc Kạn', 'Bắc Kạn'), ('Long An', 'Long An'), ('Ninh Bình', 'Ninh Bình'), ('Hà Giang', 'Hà Giang'), ('Phú Yên', 'Phú Yên'), ('Đắk Lắk', 'Đắk Lắk'), ('Bình Dương', 'Bình Dương'), ('Thanh Hóa', 'Thanh Hóa'), ('Hậu Giang', 'Hậu Giang'), ('Ninh Thuận', 'Ninh Thuận'), ('Tiền Giang', 'Tiền Giang'), ('Quảng Nam', 'Quảng Nam'), ('Thái Nguyên', 'Thái Nguyên'), ('Hải Phòng', 'Hải Phòng'), ('Sóc Trăng', 'Sóc Trăng')], default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Unvailable', 'Unavailable'), ('Sale', 'For Sale'), ('draft', 'Draft'), ('published', 'Published')], default='Available', max_length=20),
        ),
    ]
