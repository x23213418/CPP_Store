from django.shortcuts import render, redirect, HttpResponse
from cart.models import Category, SubCategory, Product, MyCart, Order
from django.contrib.auth.models import User
from django.contrib.auth import login as xlogin, authenticate, logout as xlogout

def home(request):
    p= Product.objects.all()
    # cat = Subcategory.objects.all()
    # return render(request, 'index.html', {'p':p, 'cat':cat})
    return render(request, 'index.html', {'p':p,})

def store(request):
    p= Product.objects.all()
    # cat = Subcategory.objects.all()
    # return render(request, 'index.html', {'p':p, 'cat':cat})
    return render(request, 'store.html', {'p':p,})

def product(request, id):
   
    
    p= Product.objects.get(pk=id)
    # cat = Subcategory.objects.all()
    # return render(request, 'index.html', {'p':p, 'cat':cat})
    return render(request, 'product.html', {'p':p,})        

def login(request):
    return render(request, 'login.html')

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        p1 = request.POST.get("p1")
        user = authenticate(username=uname, password=p1)
        if user is not None:
            xlogin(request, user)

            # messages.success(request, "Logged in")
            return redirect('home')
        else:
            # messages.info(request,'invalid credentials')
            return redirect('login')  
    return redirect('login') 

def signup(request):
    return render(request, 'signup.html')

def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("uname")
        email = request.POST.get('email')
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        
        if p1==p2:
        

            u = User.objects.create_user(username=uname, email=email, password=p1)
            u.first_name = fname
            u.last_name = lname

            u.save()
            # messages.success(request, "Your account has been created")
            print('success')
            return redirect("home")
    else:

        return HttpResponse("404 error")     

def logout(request):
    xlogout(request)
    return redirect('home')        

def order_now(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id=request.POST.get('id')
            q=request.POST.get('q')
            adr=request.POST.get('adr')
            p=Product.objects.get(pk=id)
            o=Order(prod_id=id, quantity=q, user_id=request.user.pk, order_main_id='DSDSD23DS', status='Pending', address=adr)
            o.save()
            return redirect('home')
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("please login")

def my_orders(request):
    o= Order.objects.filter(user_id=request.user.pk)
    # cat = Subcategory.objects.all()
    # return render(request, 'index.html', {'p':p, 'cat':cat})
    return render(request, 'my_orders.html', {'o':o})        

def edit_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id= request.POST.get('id')
            o=Order.objects.get(pk=id)
            return render(request, 'edit_order.html', {'o':o})
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("please login")    

def handle_edit_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id=request.POST.get('id')
            q=request.POST.get('q')
            adr=request.POST.get('adr')
            o=Order.objects.get(pk=id)
            o.quantity=q
            o.address=adr
            o.price=int(q)*int(o.prod.price)
            o.save()
            return redirect('home')
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("please login")    

def delete_order(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            id= request.POST.get('id')
            o=Order.objects.get(pk=id)
            o.delete()
            return redirect('my_orders')  
        else:

            return HttpResponse("404 error")
    else:

        return HttpResponse("please login")    