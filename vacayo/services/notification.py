import sendgrid
from sendgrid.helpers.mail import Email, Content, Mail, Substitution
from django.conf import settings
from .email import EmailService


class NotificationService(object):

    @classmethod
    def send_new_lead_notifications(cls, lead):
        return lead

    @classmethod
    def send_new_property_notifications(cls, property):
        # Notify owners by email
        for owner in property.owners.all():
            EmailService.send_new_property_email_to_owner(
                to_email=owner.user.email,
                to_name=owner.user.first_name,
                address=property.location.address,
                offer=property.offer
            )

        # Notify hosts by email
        for host in property.hosts.all():
            EmailService.send_new_property_email_to_host(
                to_email=host.user.email,
                to_name=host.user.first_name,
                address=property.location.address,
                # within_range=within_range
            )

        # Notify Vacayo by email
        EmailService.send_new_property_email_to_vacayo(
            address=property.location.address
        )
