from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class Util:
    @staticmethod
    def send_email(data,user_name):
        subject = data['subject']
        to_email = [data['to_email']]
        from_email = 'inaam@demomailtrap.co'  # Your Mailtrap from address
        body = data['body']

        # Optional: render HTML template
        html_message = render_to_string('email_template.html', {'body': body, 'name': user_name})
        plain_message = strip_tags(html_message)

        email = EmailMultiAlternatives(
            subject=subject, body=plain_message, from_email=from_email, to=to_email)
        email.attach_alternative(html_message, "text/html")

        # # Optional attachment (comment out if not used)
        # with open('account\pdf\myfile.pdf', 'rb') as file:
        #     email.attach('myfile.pdf', file.read(), 'application/pdf')

        email.send()
