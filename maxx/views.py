import email
from os import name

from django.contrib import messages
from django.contrib import admin, auth
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMultiAlternatives, send_mail, message
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.contrib.auth.hashers import make_password
from django.template.loader import get_template
from django.shortcuts import render, get_object_or_404
from .models import upload_images, CartItem
from maxx.forms import *
from django.conf import settings
import os
import openai
# from portfolio.settings import DEFAULT_FROM_EMAIL
OPENAI_API_KEY = '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'



def get_completion(prompt):
    query = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt}]
    )
    response = query.get('choices')[0]['message']['content']
    return response


def chatbot(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_completion(prompt)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', response)
        return JsonResponse({'response': response})
    return render(request, 'chatbot.html')











def index(request):
    return render(request, 'index.html', locals())
# def cart_page(request, id):
#     products= get_object_or_404(upload_images, id=id)
#     context = {
#         'products': products,
#         'id': id,
#     }
#     return render(request, 'cart-page.html', context)

def new(request):
    if request.method == "POST":
        form = test(request.POST)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('new')

    return render(request, 'new.html', locals())
def cart_page(request, id):
    print(id, "----------------------")

    product = get_object_or_404(upload_images, id=id)
    print(product,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    cart_item, created = CartItem.objects.get_or_create(product=product)
    quantity=1
    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    cart_items = CartItem.objects.all()
    print(cart_items,'*********************')
    return render(request, 'cart-page.html', {'cart_items':cart_items})




def p_detail(request, id):
    products = get_object_or_404(upload_images, id=id)
    context = {
        'products': products
    }
    # products = upload_images.objects.all()
    print(products,'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    return render(request, 'pdetail.html',context)


def contact_us(request):
    if request.method == "POST":
        form = contactform(request.POST)
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        if form.is_valid():
            email = request.POST.get("email")
            form.save()
            print('???????????????????????????????????????/')
            saved = True
            messages.success(request, 'Thank-you for Contacting Us')

            print(email, "---------------email")
            d = ({'email': email})
            plaintext = get_template('email.txt')
            # htmly = get_template('contact-us.html')
            subject, from_email, to = 'Thank You For Contacting Us', 'care@clindle.com', email
            text_content = plaintext.render(d)
            # html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            msg.send()
            thankyou = True

            # foterblog = blog.objects.all().order_by('-id')[:3]

            # return render(request, "messege.html", locals())
        else:
            messages.error(request, 'Your Information  Was Not  Update')


    else:
        form = contactform()

    return render(request, 'contactus.html', locals())

def faqs(request):
    return render(request, 'faq.html', locals())

def jsanimation(request):
    return render(request, 'jsanimation.html', locals())


def header(request):
    return render(request, 'header.html', locals())





def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                email=email, password=password1)
                user.save()
                return redirect('options')

        else:
            messages.info(request, 'Password didnt match')
            return redirect('register')

    else:
        return render(request, 'register.html')

def options(request):
    return render(request, 'options.html', locals())
def products(request):
    products = upload_images.objects.all()
    print(products,'************************************************************')
    return render(request, 'products.html', {'products':products})
# def upload(request, id=0):
#     if request.method == "POST":
#         if id == 0:
#             show = upload_forms()
#         else:
#             d = upload.objects.get(pk=id)
#             show = upload_forms(instance=d)
#         return render(request, 'upload.html', {'show': show})
#     else:
#         if id == 0:
#             show = upload_forms(request.POST, request.FILES)
#         else:
#             d = upload.objects.get(pk=id)
#             show = upload_forms(request.POST, request.FILES, instance=d)
#         if show.is_valid():
#             show.save()
#             messages.info(request, 'send data')
#             return redirect('products')
#         return render(request, 'upload.html', {'show': show})
def upload(request, id=0):
    if request.method == "GET":
        if id == 0:
            show = upload_forms()
        else:
            d = upload_images.objects.get(pk=id)
            show = upload_forms(instance=d)
        return render(request, 'upload.html', {'show': show})
    else:
        if id == 0:
            show = upload_forms(request.POST, request.FILES)
        else:
            d = upload_images.objects.get(pk=id)
            show = upload_forms(request.POST, request.FILES, instance=d)
        if show.is_valid():
            show.save()
            messages.info(request, 'send data')
            return redirect('products')
        return render(request, 'upload.html', {'show': show})




def loggin(request):
    if request.method == "POST":
        username = request.POST['username']
        print(username,'hhh')
        password = request.POST['password']
        print(password,'uuu')

        user = auth.authenticate(username=username, password=password)
        print(user,'kkk')
        if user is not None:
            auth.login(request, user)
            print('done``````````````````````````````````')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username/Password')
            return redirect('login')

    else:
        print('*********************************************')
        return render(request, 'login.html')










# def loggin(request):
#     if request.method == "POST":
#         print('gkdfjgkh')
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#         print(user,'hjgh')
#         if user is not None:
#             auth.login(request, user)
#             print('done``````````````````````````````````')
#             return redirect('/')
#         else:
#             messages.info(request, 'Invalid Username/Password')
#             return redirect('login')
#
#     else:
#         print('*********************************************')
#         return render(request, 'login.html')
