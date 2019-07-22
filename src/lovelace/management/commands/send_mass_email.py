import sys
import json
import requests

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from users.models import UserProfile
from lovelace.settings import MAILGUN_API_URL, MAILGUN_API_KEY, LOVELACE_FROM_EMAIL

class Command(BaseCommand):
    help = "Send a mass email to all Project Lovelace users."

    def add_arguments(self, parser):
        parser.add_argument('-S', '--subject', type=str, help="Subject of the email.")
        parser.add_argument('-M', '--message', type=str, help="File containing a message to email out.")

    def handle(self, *args, **kwargs):
        subject = kwargs['subject']
        message_filepath = kwargs['message']

        with open(message_filepath, 'r') as f:
            message_html = f.read()

        soup = BeautifulSoup(message_html, "html.parser")
        message_text = soup.get_text()

        users_to_email = UserProfile.objects.filter(subscribe_to_emails=True)

        to_emails = []
        recipient_vars = {}
        for user in users_to_email:
            to_emails.append(user.user.email)
            recipient_vars[user.user.email] = {'username': user.user.username}

        self.stdout.write(self.style.WARNING("MAILGUN_API_KEY={:s}".format(MAILGUN_API_KEY)))
        self.stdout.write(self.style.WARNING("FROM: {:s}\n".format(LOVELACE_FROM_EMAIL)))
        self.stdout.write(self.style.WARNING("Subject: {:s}".format(subject)))
        self.stdout.write(self.style.WARNING("Email HTML content ({:s}):".format(message_filepath)))
        self.stdout.write("{:s}".format(message_html))
        self.stdout.write(self.style.WARNING("\nEmail text content ({:s}):".format(message_filepath)))
        self.stdout.write("{:s}".format(message_text))

        self.stdout.write(self.style.WARNING("\nThis email will be sent to {:d} recipients.".format(len(to_emails))))
        send_for_sure = input(self.style.WARNING("Are you sure you want to send this mass email? [Y/n] "))

        if send_for_sure != "Y":
            self.stdout.write(self.style.NOTICE("No email was sent. Aborting script."))
            sys.exit(0)

        self.stdout.write(self.style.SUCCESS("\nSending Mailgun request..."))
        response = requests.post(MAILGUN_API_URL,
                auth=('api', MAILGUN_API_KEY),
                data={'from': LOVELACE_FROM_EMAIL,
                      'to': to_emails,
                      'subject': subject,
                      'html': message_html,
                      'text': message_text,
                      'recipient-variables': json.dumps(recipient_vars)})

        self.stdout.write(self.style.WARNING("Mailgun response:"))
        self.stdout.write("{:}".format(response))
        self.stdout.write("{:}".format(response.content))

        self.stdout.write(self.style.SUCCESS("\nEmails sent!"))

