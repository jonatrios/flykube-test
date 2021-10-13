from django.db import models


# Destiantion Model
class DestinationModel(models.Model):
    '''Name, available (true/false), price'''
    id = models.AutoField(verbose_name='destination_id', primary_key=True)
    destination_name = models.CharField(verbose_name='destination_name', max_length=200, blank=False, null=False, unique=True)
    aviable = models.BooleanField(verbose_name='aviable', default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)



    class Meta:
        verbose_name = 'Destination'
        verbose_name_plural = 'Destinations'

    def __str__(self) -> str:
        return self.destination_name



#Passenger Model
class PassengerModel(models.Model):
    '''Passenger: Birth date, ID document, type of ID document (DNI, passport), gender'''
    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
        ('U', 'Unsure',),
    )

    id = models.AutoField(verbose_name='passenger_id', primary_key=True)
    birth_date = models.DateField(verbose_name='birth_date')
    document_id = models.CharField(verbose_name='document_id', max_length=30, blank=False, null=False, unique=True)
    document_type = models.CharField(verbose_name='document_type', max_length=30, blank=False, null=False)
    gender = models.CharField(max_length=1,choices=SEX_CHOICES)


    class Meta:
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'



#Travel Model
class TravelModel(models.Model):
    '''start date, end date, destination, confirmed'''

    id = models.AutoField(verbose_name='travel_id', primary_key=True)
    start_date = models.DateField(verbose_name='start_date')
    end_date = models.DateField(verbose_name='end_date')
    destination = models.ForeignKey(DestinationModel, on_delete=models.CASCADE, verbose_name='destination_name', null=True)
    confirmed = models.BooleanField(verbose_name='confirmed', default=True)
    passenger = models.ManyToManyField(PassengerModel)

    class Meta:
        verbose_name = 'Travel'
        verbose_name_plural = 'Travels'

    def __str__(self) -> str:
        return f'{self.destination}: start {self.start_date} and ends {self.end_date}'



