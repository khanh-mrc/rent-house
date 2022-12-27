# Generated by Django 4.1.3 on 2022-12-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0022_alter_listing_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(choices=[('Bến Tre', 'Bến Tre'), ('Sóc Trăng', 'Sóc Trăng'), ('Bình Dương', 'Bình Dương'), ('Quảng Nam', 'Quảng Nam'), ('Tuyên Quang', 'Tuyên Quang'), ('Đồng Nai', 'Đồng Nai'), ('Điện Biên', 'Điện Biên'), ('Bắc Ninh', 'Bắc Ninh'), ('Quảng Ninh', 'Quảng Ninh'), ('Cà Mau', 'Cà Mau'), ('Tiền Giang', 'Tiền Giang'), ('Yên Bái', 'Yên Bái'), ('Hậu Giang', 'Hậu Giang'), ('Đắk Nông', 'Đắk Nông'), ('Quảng Trị', 'Quảng Trị'), ('Hà Nam', 'Hà Nam'), ('Bắc Giang', 'Bắc Giang'), ('Khánh Hòa', 'Khánh Hòa'), ('Phú Yên', 'Phú Yên'), ('Thừa Thiên Huế', 'Thừa Thiên Huế'), ('Hải Phòng', 'Hải Phòng'), ('Trà Vinh', 'Trà Vinh'), ('Thái Bình', 'Thái Bình'), ('Quảng Bình', 'Quảng Bình'), ('Cao Bằng', 'Cao Bằng'), ('Bình Phước', 'Bình Phước'), ('Vĩnh Phúc', 'Vĩnh Phúc'), ('Nam Định', 'Nam Định'), ('Lào Cai', 'Lào Cai'), ('Hải Dương', 'Hải Dương'), ('TP. Hồ Chí Minh', 'TP. Hồ Chí Minh'), ('Kon Tum', 'Kon Tum'), ('An Giang', 'An Giang'), ('Hà Tĩnh', 'Hà Tĩnh'), ('Hà Giang', 'Hà Giang'), ('Sơn La', 'Sơn La'), ('Bạc Liêu', 'Bạc Liêu'), ('Kiên Giang', 'Kiên Giang'), ('Nghệ An', 'Nghệ An'), ('Cần Thơ', 'Cần Thơ'), ('Long An', 'Long An'), ('Phú Thọ', 'Phú Thọ'), ('Hà Nội', 'Hà Nội'), ('Vĩnh Long', 'Vĩnh Long'), ('Hưng Yên', 'Hưng Yên'), ('Đắk Lắk', 'Đắk Lắk'), ('Bắc Kạn', 'Bắc Kạn'), ('Đồng Tháp', 'Đồng Tháp'), ('Tây Ninh', 'Tây Ninh'), ('Ninh Bình', 'Ninh Bình'), ('Thái Nguyên', 'Thái Nguyên'), ('Bình Thuận', 'Bình Thuận'), ('Lạng Sơn', 'Lạng Sơn'), ('Lâm Đồng', 'Lâm Đồng'), ('Gia Lai', 'Gia Lai'), ('Thanh Hóa', 'Thanh Hóa'), ('Quảng Ngãi', 'Quảng Ngãi'), ('Bình Định', 'Bình Định'), ('Đà Nẵng', 'Đà Nẵng'), ('Lai Châu', 'Lai Châu'), ('Hòa Bình', 'Hòa Bình'), ('Bà Rịa – Vũng Tàu', 'Bà Rịa – Vũng Tàu'), ('Ninh Thuận', 'Ninh Thuận')], default='TP. Hồ Chí Minh', max_length=100),
        ),
    ]