import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail, Substitution
from django.conf import settings


class EmailService(object):
    from_email = Email("test@example.com")

    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)

    def send_registration_confirmation_email(self, to_email, to_name, address, quote):
        from_email = self.from_email
        to_email = Email(to_email)
        subject = 'Vacayo Property Rental Quote'
        content = Content("text/html", 'TESTING')

        mail = Mail(from_email, subject, to_email, content)
        mail.template_id = '5e8cabc6-aa9f-49fb-b4c1-effe3e00cf84'
        personalization = mail.personalizations[0]
        personalization.add_substitution(Substitution("-first_name-", to_name))
        personalization.add_substitution(Substitution("-address-", address))
        personalization.add_substitution(Substitution("-quote-", quote))

        self.sg.client.mail.send.post(request_body=mail.get())
