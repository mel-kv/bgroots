from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
  order = Order.objects.get(id=order_id)
  subject = f'Order N. {order.id} from BG Roots Shop'
  message = f'Dear {order.first_name}, \n\n You have successfully place an order with N. { order.id}.'
  mail_sent = send_mail(subject, message, 'admin@bgshop.com', [order.email])
  return mail_sent 
