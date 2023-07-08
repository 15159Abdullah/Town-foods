from django.db import models
from accounts.models import *

#  <<<<<<<<<<<<<<<<<<<<< ROOM MODEL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Room(models.Model):
    ROOM_NAME = (
        ('Family Room', 'Family Room'),
        ('Deluxe Room', 'Deluxe Room'),
        ('Classic Room', 'Classic Room'),
        ('Superior Room', 'Superior Room'),
        ('Luxury Room', 'Luxury Room'),
        ('Suite Room', 'Suite Room'), 
    )
    room_name = models.CharField(max_length=13, choices=ROOM_NAME)
    room_number = models.IntegerField(unique=True)
    room_bed_quantity = models.IntegerField()
    room_image = models.ImageField(upload_to='room_pictures/' , blank=True)
    room_price = models.IntegerField()
    room_capacity = models.IntegerField()
    room_is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_name

#  <<<<<<<<<<<<<<<<<<<<< ROOM BOOKING MODEL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class RoomBooking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    guest_name = models.CharField(max_length=100)
    booking_price =  models.IntegerField(default=True)
    booked_room_number = models.IntegerField(default=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    

class Invoices(models.Model):  
    room = models.ForeignKey(Room, on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    guest_name = models.CharField(max_length=100)
    booking_price =  models.IntegerField(default=True)
    booked_room_number = models.IntegerField(default=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    
#  <<<<<<<<<<<<<<<<<<<<< CONTACT US MODEL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Contact_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500)

    
#  <<<<<<<<<<<<<<<<<<<<< RESTURENT MENU MODEL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Resto_menu(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField(max_length=50)
    item_img = models.ImageField(upload_to='Menu_img/')
    item_description = models.CharField(max_length=50)

    def __str__(self):
        return self.item_name




