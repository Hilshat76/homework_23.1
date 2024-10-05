
from django.core.mail import send_mail

send_mail(
    "Тема письма",
    "Сам текст сообщения",
    'hilshat76@mail.ru',
    ['hilshat76@mail.ru'],

)

