import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail, Substitution
from django.conf import settings


class EmailService(object):
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    from_email = Email("hello@vacayo.com")

    @classmethod
    def send_new_property_email_to_owner(cls, to_email, to_name, address, offer):
        try:
            from_email = cls.from_email
            to_email = Email(to_email)
            subject = 'Vacayo Rental Offer'
            content = Content("text/html", 'TESTING')

            mail = Mail(from_email, subject, to_email, content)
            mail.template_id = '5e8cabc6-aa9f-49fb-b4c1-effe3e00cf84'
            personalization = mail.personalizations[0]
            personalization.add_substitution(Substitution("-first_name-", to_name))
            personalization.add_substitution(Substitution("-address-", address))
            personalization.add_substitution(Substitution("-offer-", offer))

            cls.sg.client.mail.send.post(request_body=mail.get())
            return True
        except (Exception,) as e:
            return False

    @classmethod
    def send_new_property_email_to_host(cls, to_email, to_name, address):
        try:
            from_email = cls.from_email
            to_email = Email(to_email)
            subject = 'Vacayo Rental Offer'
            content = Content("text/html", 'TESTING')

            mail = Mail(from_email, subject, to_email, content)
            mail.template_id = '5e8cabc6-aa9f-49fb-b4c1-effe3e00cf84'
            personalization = mail.personalizations[0]
            personalization.add_substitution(Substitution("-first_name-", to_name))
            personalization.add_substitution(Substitution("-address-", address))

            cls.sg.client.mail.send.post(request_body=mail.get())
            return True
        except (Exception,) as e:
            return False

    @classmethod
    def send_new_property_email_to_vacayo(cls, address):
        try:
            from_email = cls.from_email
            to_email = cls.from_email
            subject = 'Vacayo Rental Offer'
            content = Content("text/html", 'TESTING')

            mail = Mail(from_email, subject, to_email, content)
            mail.template_id = '5e8cabc6-aa9f-49fb-b4c1-effe3e00cf84'
            personalization = mail.personalizations[0]
            personalization.add_substitution(Substitution("-first_name-", 'Vacayo'))
            personalization.add_substitution(Substitution("-address-", address))

            cls.sg.client.mail.send.post(request_body=mail.get())
            return True
        except (Exception,) as e:
            return False
