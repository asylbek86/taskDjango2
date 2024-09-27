from random import choices

from django.db import models




class Car(models.Model):

    CAR_TYPES = (
        ("Седан", "Седан"),
        ("Пикап", "Пикап"),
        ("Купе", "Купе"),
        ("Унивесал", "Универса"),
        ("Минивен", "Минивен")
    )



    title = models.CharField("Название машины",max_length=100)
    description = models.TextField("Название описание" )
    image = models.ImageField(upload_to="")
    car_type = models.CharField(max_length=100, choices=CAR_TYPES)
    created_date = models.DateTimeField(auto_now=True)
    price = models.PositiveIntegerField("Цена")
    video = models.URLField()

    def __str__(self):
        return self.title



class CommentCar(models.Model):

    RATING = (
        ('*', '*'),
        ('**', '**'),
        ('***', '***'),
        ('****', '****'),
        ('*****', '*****'),
    )


    car_choice_comment = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comment_object')
    text = models.TextField()
    rate_stars = models.CharField(max_length=100, choices=RATING)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.rate_stars



















