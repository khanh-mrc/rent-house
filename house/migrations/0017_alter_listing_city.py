# Generated by Django 4.1.3 on 2022-12-08 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0016_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Phú Yên', 'Phú Yên'), ('Kiên Giang', 'Kiên Giang'), ('Cao Bằng', 'Cao Bằng'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Quảng Nam', 'Quảng Nam'), ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Cà Mau', 'Cà Mau'), ('Quảng Trị', 'Quảng Trị'), ('Đắk Nông', 'Đắk Nông'), ('Yên Bái', 'Yên Bái'), ('Vĩnh Long', 'Vĩnh Long'), ('Lạng Sơn', 'Lạng Sơn'), ('Tuyên Quang', 'Tuyên Quang'), ('Bình Định', 'Bình Định'), ('Điện Biên', 'Điện Biên'), ('Lai Châu', 'Lai Châu'), ('Bà Rịa – Vũng Tàu', 'Bà Rịa – Vũng Tàu'), ('An Giang', 'An Giang'), ('Tiền Giang', 'Tiền Giang'), ('Bắc Kạn', 'Bắc Kạn'), ('Quảng Bình', 'Quảng Bình'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Bạc Liêu', 'Bạc Liêu'), ('Thái Bình', 'Thái Bình'), ('Lâm Đồng', 'Lâm Đồng'), ('Tây Ninh', 'Tây Ninh'), ('Bình Thuận', 'Bình Thuận'), ('Quảng Ninh', 'Quảng Ninh'), ('Đồng Tháp', 'Đồng Tháp'), ('Hòa Bình', 'Hòa Bình'), ('Sơn La', 'Sơn La'), ('Trà Vinh', 'Trà Vinh'), ('Đồng Nai', 'Đồng Nai'), ('Bình Phước', 'Bình Phước'), ('Bến Tre', 'Bến Tre'), ('Cần Thơ', 'Cần Thơ'), ('Hậu Giang', 'Hậu Giang'), ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'), ('Hải Phòng', 'Hải Phòng'), ('Hà Nam', 'Hà Nam'), ('Bình Dương', 'Bình Dương'), ('Khánh Hòa', 'Khánh Hòa'), ('Sóc Trăng', 'Sóc Trăng'), ('Bắc Ninh', 'Bắc Ninh'), ('Thái Nguyên', 'Thái Nguyên'), ('Đắk Lắk', 'Đắk Lắk'), ('Long An', 'Long An'), ('Ninh Thuận', 'Ninh Thuận'), ('Phú Thọ', 'Phú Thọ'), ('Hải Dương', 'Hải Dương'), ('Gia Lai', 'Gia Lai'), ('Nam Định', 'Nam Định'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Ninh Bình', 'Ninh Bình'), ('Lào Cai', 'Lào Cai'), ('Hưng Yên', 'Hưng Yên'), ('Thanh Hóa', 'Thanh Hóa'), ('Bắc Giang', 'Bắc Giang'), ('Kon Tum', 'Kon Tum'), ('Đà Nẵng', 'Đà Nẵng'), ('Hà Giang', 'Hà Giang'), ('Nghệ An', 'Nghệ An'), ('Hà Nội', 'Hà Nội')], default='TP. Hồ Chí Minh', max_length=100),
        ),
    ]