from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib import messages
from accounts.decorators import hotel_required


def home_page(request):
    food = Resto_menu.objects.filter(item_price__range=(100,800))
    room = Room.objects.filter(room_price__range=(1500,3000))
    return render(request,'hotel_product/home.html',context={'current_page':'home','rooms':room,'foods':food,'title':'Town Foods | Home'})

def contact_us(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Subject = request.POST.get('subject')
        Message = request.POST.get('message')
        mail = Contact_us(name=Name,email=Email,subject=Subject,message = Message)
        mail.save()

        email_to = [Email]
        email_from = settings.EMAIL_HOST_USER
        subject = Subject
        message =  f'Hi MR.{Name}. We Have Received Your Email  THANK YOU FOR JIONING US!' + Message
        send_mail(subject,message,email_from,email_to)
    return render(request,'hotel_product/contact_us.html',context={'current_page':'contact_us','title':'Town Foods | Contact Us'})

def rooms(request):
    room = Room.objects.all()
    return render(request,'hotel_product/rooms.html',context={'current_page':'rooms', 'rooms':room,'title':'Town Foods | Rooms'})

def is_room_available(check_in_date, check_out_date,room):
    bookings = RoomBooking.objects.filter(
        Q(check_in_date__range=(check_in_date, check_out_date)) & Q(check_out_date__range=(check_in_date, check_out_date)),
        room=room
    )
    return not bookings.exists()


@hotel_required
def room_detail_page(request,pk):
    uid =request.session.get('_auth_user_id')
    user_now = CustomUser.objects.get(id = uid)
    room_detail = Room.objects.get(id = pk)
    booked_room_No =room_detail.room_number
    room = room_detail
    if request.method == "POST":
        check_in = request.POST.get('check_in_date')
        check_out = request.POST.get('check_out_date')
        if is_room_available(check_in, check_out,room):
            booked = RoomBooking.objects.create( booked_room_number= booked_room_No,guest_name = user_now.username,booking_price =room_detail.room_price,room=room_detail,check_in_date=check_in,check_out_date=check_out)
            booked.save()
            invoice = Invoices.objects.create(user=user_now,booked_room_number= booked_room_No,guest_name = user_now.username,booking_price =room_detail.room_price,room=room_detail,check_in_date=check_in,check_out_date=check_out)
            invoice.save()
            email = request.user.email
            email_to = [email]
            email_from = settings.EMAIL_HOST_USER
            subject = f"YOUR {room_detail.room_name} Successfully BOOKED."
            message = f"""

                    Hi MR {user_now}! YOUR ROOM bOOKING SATUS.
                    ROOM NAME   {room_detail.room_name}
                    ROOM NO.    {room_detail.room_number}
                    BED QTY     {room_detail.room_bed_quantity}
                    PRICE       {room_detail.room_price}
                    CHECK-IN    {check_in}
                    CHECK-OUT   {check_out}

                MEHBOOB LIGHTS HOTEL 

                THANK YOU
                   It Feels Like Staying In Your Own Home.
            """
            send_mail(subject,message,email_from,email_to)
            return redirect('order')  
        messages.warning(request,"Room Is Not Availbal In This Date!")
    context = {'room_detail':room_detail,'title':'Town Foods | Room Detail Page'}
    return render(request,'hotel_product/room_detail_page.html',context=context)

def Order(request):
    user = request.user
    order = RoomBooking.objects.filter(guest_name=user)
    return render(request,'hotel_product/order.html',context = {'order':order,'title':'Town Foods | Your Order'})

def about_us(request):
    return render(request,'hotel_product/about_us.html',context={'current_page':'about_us','title':'Town Foods | About Us'})

def restaurant(request):
    menu = Resto_menu.objects.all()
    return render(request,'hotel_product/restaurant.html',context={'current_page':'restaurant','menu':menu ,'title':'Town Foods | Menu'})




