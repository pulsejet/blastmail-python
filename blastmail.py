#!/usr/bin/python3

import csv
import time
from tqdm import tqdm
import smtplib
from email.mime.text import MIMEText

# ===========================================================================

TEMPLATE_FILE = 'template.html'
DATA_FILE = 'data.csv'
SLEEP_TIME = 4
FROM_ADDRESS = 'John Doe <john@doe.com>'

# ===========================================================================

def blast_merge():
        reader = csv.DictReader(open(DATA_FILE))

        with open(TEMPLATE_FILE, 'r') as file:
                template = file.read()

        rows = [row for row in reader]

        for row in tqdm(rows):
                tqdm.write('=' * 60)

                body = str(template)


                tqdm.write('Sending e-mail to' + ' ' + row['name'] + ' ' + row['email'])

                for col in row:
                        body = body.replace('{{' + col + '}}', row[col])

                tqdm.write(body)
                time.sleep(SLEEP_TIME)

                sendmail(body, FROM_ADDRESS, row['email'], row['subject'])


def sendmail(body, addr_from, addr_to, subject):
        msg = MIMEText(body, 'html')

        msg['Subject'] = subject
        msg['From'] = addr_from
        msg['To'] = addr_to

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail(addr_from, [addr_to], msg.as_string())
        s.quit()

if __name__ == '__main__':
        blast_merge()
ubuntu@ferrous:~/mail$ import csv
DATA_FILE = 'data.csv'
SLEEP_TIME = 4
FROM_ADDRESS = 'Himank Jain <himank@moodi.org>'

# ===========================================================================

def blast_merge():
        reader = csv.DictReader(open(DATA_FILE))

        with open(TEMPLATE_FILE, 'r') as file:
                template = file.read()

        rows = [row for row in reader]

        for row in tqdm(rows):
                tqdm.write('=' * 60)

                body = str(template)


                tqdm.write('Sending e-mail to' + ' ' + row['name'] + ' ' + row['email'])

                for col in row:
                        body = body.replace('{{' + col + '}}', row[col])

                tqdm.write(body)
                time.sleep(SLEEP_TIME)

                sendmail(body, FROM_ADDRESS, row['email'], row['subject'])


def sendmail(body, addr_from, addr_to, subject):
        msg = MIMEText(body, 'html')

        msg['Subject'] = subject
        msg['From'] = addr_from
        msg['To'] = addr_to

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('localhost')
        s.sendmail(addr_from, [addr_to], msg.as_string())
        s.quit()

if __name__ == '__main__':
        blast_merge()
