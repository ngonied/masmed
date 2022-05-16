#from __future__ import absolute_import, unicode_literals
from masmed.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' 
    f'You have successfully placed an order.' 
    f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
    message,
    'admin@masmed.com',
    [order.email])
    
    return mail_sent