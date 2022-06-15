from operator import mod
from django.db import models

# Create your models here.

class Contacts(models.Model):
    first_name = models.CharField('Аты', max_length=255)
    last_name = models.CharField('Фамилиясы', max_length=255)
    email = models.EmailField()
    message = models.TextField('Пикип')
    sent_at = models.DateTimeField('Убакыт', auto_now_add=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакттар'



class Product(models.Model):
    name = models.CharField("Дарынын аталышы",max_length=255)
    description = models.CharField("Инструкция",max_length=255, default='', blank=True, null=True)
    price = models.IntegerField("Баасы",default=0)
    image = models.ImageField("Сүрөт", upload_to='upload/products')
    ingredients = models.TextField('Состав')
    code_product = models.IntegerField('Товардын коду')
    manufacturer = models.CharField('Өндүрүүчү жер', max_length=255)
    country = models.CharField('Өлкө', max_length=255)
    weight_volume = models.CharField('Салмагы/Көлөмү', max_length=255)
    age_limit = models.CharField('Минималдуу жаштан баштап', max_length=255)
    temperature = models.CharField('Уруксат берилген сактоо температурасы', max_length=255)
    expiration_date = models.CharField('Жарактуулук мөөнөтү', max_length=255)
    date_manufacture = models.DateField('Өндүрүлгөн датасы')

    class Meta:
        verbose_name = 'Дары'
        verbose_name_plural = 'Дарылар'
   
class Billing_detail(models.Model):
    first_name = models.CharField('Ат/ысым', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    number = models.CharField('Телефон номер', max_length=50)
    email = models.EmailField('Почта')
    country = models.CharField('Өлкө', max_length=255)
    city = models.CharField('Шаар', max_length=255)
    street = models.CharField('Көчө', max_length=255)
    posta_zip = models.CharField('Почта/Почтанын индекси', max_length=255)
    note_message = models.TextField('Ой-пикирлер', null=True, blank=True, default='')
    sent_at = models.DateTimeField('Убакыт', auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}  {self.last_name}'
    
    class Meta:
        verbose_name = 'Кардар'
        verbose_name_plural = 'Кардарлар'


class Order(models.Model):
    product = models.CharField('Дары', max_length=255)
    p_count = models.IntegerField('Саны')
    p_price = models.IntegerField('Баасы')
    p_total = models.IntegerField('Жалпы сумма')
    customer = models.ForeignKey(Billing_detail,  on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Алуучу/кардар")

    
    class Meta:
        verbose_name = 'Буюртма'
        verbose_name_plural = 'Буюртмалар'


class Feedback(models.Model):
    image = models.ImageField("Сүрөт", upload_to='upload/reviews')
    review = models.TextField('Ой-пикирлер', null=True, blank=True, default='')
    firstLastName = models.CharField('Аты-жөнү', max_length=255)

    class Meta:
        verbose_name = 'Ой-пикир'
        verbose_name_plural = 'Ой-пикирлер'


    



