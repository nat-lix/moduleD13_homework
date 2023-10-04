from django.dispatch import receiver
from .models import Response
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives

@receiver(post_save, sender=Response)
def email_response_to_user(sender, instance, created, **kwargs):
    if created:
        html_content = render_to_string(
            'post_response.html',
            {
                'post_id': instance.Post_id,
                'post_title': instance.Post.notice_title,
                'user': instance.Post.notice_author,
            }
        )

        msg = EmailMultiAlternatives(
            subject=f'Комментарий к объявлению',
            body="",
            from_email='talathecat@yandex.ru',
            to=[instance.Post.Post_author.email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    else:
        if instance.Response_accepted:
            html_content = render_to_string(
                'post_response.html',
                {
                    'post_id': instance.Post_id,
                    'post_title': instance.Post.notice_title,
                    'user': instance.User.username,
                }
            )

            msg = EmailMultiAlternatives(
                subject=f'У Вас новый комментарий',
                from_email='talathecat@yandex.ru',
                to=[instance.User.email],
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()