from django.shortcuts import render , redirect , HttpResponseRedirect
from accounts.decorators import dashboard_required
from hotel_system.models import *
from django.contrib import messages
from django.template.loader import get_template
from django.http import HttpResponse
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate
from xhtml2pdf import pisa

# Create your views here.
@dashboard_required
def home(request):
    order= RoomBooking.objects.all()
    orders =0
    for i in order:
        orders +=1
    user = CustomUser.objects.all()
    users = 0
    for i in user:
        users +=1
    room = Room.objects.all()
    rooms= 0
    for i in room:
        rooms +=1
    food = Resto_menu.objects.all()

    foods = 0
    for i in food:
        foods +=1

    return render(request,'dashboard/index.html',context={'current_page':'home','title':'Town Foods Admin | Home','order':order,'users':users,'orders':orders,'rooms':rooms,'foods':foods})
 
#.........Invoices............
@dashboard_required
def invoice_list(request):
    invoice = Invoices.objects.all()
    return render(request,'dashboard/invoice/invoice_list.html',context={'current_page':'invoice','invoices':invoice,'title':'Town Foods Admin | Invoice List'})

@dashboard_required
def invoice_view(request,pk):
    invoice = Invoices.objects.filter(id=pk)
    for i in invoice:
        print(i.user)

    return render(request,'dashboard/invoice/invoice_view.html',context={'invoice':invoice,'title':'Town Foods Admin | Invoice View'})


def delete_invoice(request,pk):
    inv= Invoices.objects.get(id = pk)
    Invoices.delete(inv)
    return redirect('invoice_list')

#.........Room............
@dashboard_required
def rooms_list(request):
    room = Room.objects.all()
    return render(request,'dashboard/rooms/rooms.html',context={'current_page':'room','rooms':room,'title':'Town Foods Admin | Room List'})


def delete_room(request,pk):
    room = Room.objects.get(id = pk)
    Room.delete(room)
    return redirect('rooms_list')

@dashboard_required
def add_room(request):
    if request.method=='POST':
        name = request.POST.get('name')
        image =request.FILES['image_file'] 
        price = request.POST.get('price')
        size = request.POST.get('size')
        bed_qty = request.POST.get('bed_qty')
        room_no = request.POST.get('room_no')
        availibality = request.POST.get('availability')
        if availibality == '1':
            availibality = True
        else:
            availibality = False
        num = Room.objects.filter(room_number=room_no)
        if  num:
            messages.warning(request,'Room No is Already Exists!')
            return HttpResponseRedirect(request.path_info)
        else:
            room = Room(room_name=name,room_number=room_no,room_capacity = size, room_bed_quantity=bed_qty, 
                    room_image=image,room_price=price,room_is_available=availibality)
            Room.save(room)
            messages.success(request,'Sucessfully Room is save!')
    return render(request,'dashboard/rooms/add_room.html',context={'title':'Town Foods Admin | Add Rooms'})

@dashboard_required
def update_room(request,pk):
    room = Room.objects.get(id = pk)
    if request.method=="POST":
        room_id = request.POST.get('room_id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        bed_qty = request.POST.get('bed_qty')
        img = request.FILES.get('image')
        size = request.POST.get('size')
        availibality = request.POST.get('availability')
        if availibality == '1':
            availibality = True
        else:
            availibality = False
        num = Room.objects.filter(room_number=number)
        if num:
            messages.warning(request,'Room No. is Already Exists!')
            return HttpResponseRedirect(request.path_info)        
        else:
            room = Room(id =room_id,room_name=name,room_number=number, room_capacity = size, room_bed_quantity=bed_qty, 
                    room_image=img,room_price=price,room_is_available=availibality)
            room.save()
        return redirect('rooms_list')
    return render(request,'dashboard/rooms/room_update.html',context={'rooms':room,'title':'Town Foods Admin | Update Room'})

#..............Foods...............


def delete_food(request,pk):
    room = Resto_menu.objects.get(id = pk)
    Room.delete(room)
    return redirect('foods_list')

@dashboard_required
def foods_list(request):
    food = Resto_menu.objects.all()
    return render(request,'dashboard/foods/foods.html',context={'current_page':'food','foods':food,'title':'Town Foods Admin | Food List'})

@dashboard_required
def add_food(request):
    if request.method=='POST':
        name = request.POST.get('name')
        image =request.FILES['image'] 
        price = request.POST.get('price')
        des = request.POST.get('description')
       
        food = Resto_menu(item_name=name,item_price=price,item_img=image,item_description=des)
        food.save()
    return render(request,'dashboard/foods/add_food.html',context={'title':'Town Foods Admin | Add Food'})

@dashboard_required
def update_food(request,pk):
    food = Resto_menu.objects.get(id = pk)
    if request.method=='POST':
        idd = request.POST.get('food_id')
        name = request.POST.get('name')
        image =request.FILES['image'] 
        price = request.POST.get('price')
        des = request.POST.get('description')
       
        food = Resto_menu(id=idd,item_name=name,item_price=price,item_img=image,item_description=des)
        food.save()
    return render(request,'dashboard/foods/update_food.html',context={'foods':food,'title':'Town Foods Admin | Update Food'})


    #.............Orders.......................

@dashboard_required
def orders_list(request):
    order = RoomBooking.objects.all()
    return render(request,'dashboard/orders/orders.html',context={'current_page':'order','orders':order,'title':'Town Foods Admin | Order List'})

def delete_order(request,pk):
    order = RoomBooking.objects.get(id = pk)
    RoomBooking.delete(order)
    return redirect('orders_list')


    #.............Contact Us.......................
@dashboard_required
def contact_list(request):
    contact = Contact_us.objects.all()
    return render(request,'dashboard/contacts/contact_list.html',context={'current_page':'contact','contacts':contact,'title':'Town Foods Admin | Contact List'})

def delete_contact(request,pk):
    contact = Contact_us.objects.get(id = pk)
    Contact_us.delete(contact)
    return redirect('contact_list')



    #.............Users.......................
@dashboard_required
def user_list(request):
    user = CustomUser.objects.all()
    return render(request,'dashboard/users/user.html',context={'current_page':'user','users':user,'title':'Town Foods Admin | User List'})


def delete_user(request,pk):
    user = CustomUser.objects.get(id = pk)
    CustomUser.delete(user)
    return redirect('user_list')


