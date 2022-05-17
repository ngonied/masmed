# #from __future__ import absolute_import, unicode_literals
from masmed.celery import celery_app
from django.core.mail import send_mail
from .models import Order
from celery import shared_task
from django.shortcuts import get_object_or_404


@shared_task
def order_created(order_id):
    
    order = get_object_or_404(Order, id = order_id )
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n You have successfully placed an order with MASMAD. Your order ID is {order.id}. Here is what you ordered: '
    
    mail_sent = send_mail(subject,
    message,
    'ngoniechizororo@gmail.com',
    [order.email])
    print("Mail sent")
    
    return mail_sent
    
    return mail_sent