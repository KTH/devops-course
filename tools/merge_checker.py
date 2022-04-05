import os
import re
import smtplib
import ssl
import sys
import pytz
from datetime import datetime, timezone

REPO_FULLNAME = os.getenv("REPO_FULLNAME")
FILE_CHANGES = os.getenv("FILE_CHANGES")
FILE_CHANGES_2 = os.getenv("FILE_CHANGES_2")
AUTHOR = os.getenv("AUTHOR")
BODY = os.getenv("BODY")
MERGER = os.getenv("MERGER")

utc_dt = datetime.now(timezone.utc)
CEST = pytz.timezone('Europe/Stockholm')
time_of_merge = utc_dt.astimezone(CEST)

tasks = ['task 1', 'task 2', 'task 3', 'task 4', 'task 5']
tasks_to_dates = {'task 1': '5 April, 2022 15:00:00',
                  'task 2': '19 April, 2022 15:00:00',
                  'task 3': '3 May, 2022 15:00:00',
                  'task 4': '17 May, 2022 15:00:00',
                  'task 5': '23 May, 2022 15:00:00',
                  }

def mail_content(body):
    title = ''
    deadline = ''
    cat = ''
    description = ''
    body_list = body.split()

    # find title name
    title_idx = body_list.index('Title')

    names_idx = body_list.index('Names')

    for i in body_list[title_idx + 1:names_idx - 1]:
        title += i + ' '

    # find deadline
    deadline_idx = body_list.index('Deadline')
    category_idx = body_list.index('Category')

    for i in body_list[deadline_idx + 1:category_idx - 1]:
        deadline += i + ' '

    # find category
    cat_idx = body_list.index('Category')

    desc_idx = body_list.index('Description')

    for i in body_list[cat_idx + 1:desc_idx - 1]:
        cat += i + ' '

    # find description of project
    for i in body_list[desc_idx + 1:-1]:
        description += i + ' '
    description += body_list[-1]

    msg = f'Your PR was successfully merged on the KTH devops-course repository by:\n\n https://github.com/{MERGER} on {time_of_merge} (CEST).\n \nHere are the details: \n \nTitle: {title}\nType of contribution: {cat}' \
          f'\nDescription: {description}\nDeadline: {deadline}\n\nK&S :)'

    return msg, deadline


def send_mails_1():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.utils import formatdate
    from email import encoders
    import os, datetime
    COMMASPACE = ', '

    CRLF = "\r\n"
    login = "devops.kth@gmail.com"
    password = "devops2022"
    attendees = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', BODY)
    organizer = "ORGANIZER;CN=devops.kth@gmail.com:mailto:."
    fro = "devops.kth@gmail.com"
    
    eml_body, deadline = mail_content(BODY)
    
    for c in tasks:
      if c in deadline.lower():
        date_string = tasks_to_dates[c]
    
    ddtstart = datetime.datetime.strptime(date_string, "%d %B, %Y %H:%M:%S")

    # ddtstart = datetime.datetime.now()
    
    dur = datetime.timedelta(hours = 0)
    dtend = ddtstart + dur
    dtstamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%SZ")
    dtstart = ddtstart.strftime("%Y%m%dT%H%M%SZ")
    dtend = dtend.strftime("%Y%m%dT%H%M%SZ")

    description = "DESCRIPTION: test invitation from pyICSParser"+CRLF
    attendee = ""
    for att in attendees:
        attendee += "ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-    PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=TRUE"+CRLF+" ;CN="+att+";X-NUM-GUESTS=0:"+CRLF+" mailto:"+att+CRLF
    ical = "BEGIN:VCALENDAR"+CRLF+"PRODID:pyICSParser"+CRLF+"VERSION:2.0"+CRLF+"CALSCALE:GREGORIAN"+CRLF
    ical+="METHOD:REQUEST"+CRLF+"BEGIN:VEVENT"+CRLF+"DTSTART:"+dtstart+CRLF+"DTEND:"+dtend+CRLF+"DTSTAMP:"+dtstamp+CRLF+organizer+CRLF
    ical+= "UID:FIXMEUID"+dtstamp+CRLF
    ical+= attendee+"CREATED:"+dtstamp+CRLF+description+"LAST-MODIFIED:"+dtstamp+CRLF+"LOCATION:"+CRLF+"SEQUENCE:0"+CRLF+"STATUS:CONFIRMED"+CRLF
    # ical+= "SUMMARY:test "+ddtstart.strftime("%Y%m%d @ %H:%M")+CRLF+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF
    ical+= "SUMMARY:DevOps PR reminder"+CRLF+"TRANSP:OPAQUE"+CRLF+"END:VEVENT"+CRLF+"END:VCALENDAR"+CRLF


    eml_body_bin = "This is the email body in binary - two steps"
    msg = MIMEMultipart('mixed')
    msg['Reply-To']=fro
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = "DevOps KTH - PR confirmation - noreply"
    msg['From'] = fro
    msg['To'] = ",".join(attendees)

    part_email = MIMEText(eml_body,"plain")
    part_cal = MIMEText(ical,'calendar;method=REQUEST')

    msgAlternative = MIMEMultipart('alternative')
    msg.attach(msgAlternative)

    ical_atch = MIMEBase('application/ics',' ;name="%s"'%("invite.ics"))
    ical_atch.set_payload(ical)
    encoders.encode_base64(ical_atch)
    ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"'%("invite.ics"))

    eml_atch = MIMEText('', 'plain')
    encoders.encode_base64(eml_atch)
    eml_atch.add_header('Content-Transfer-Encoding', "")

    msgAlternative.attach(part_email)
    msgAlternative.attach(part_cal)

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(login, password)
    mailServer.sendmail(fro, attendees, msg.as_string())
    mailServer.close()
    
def send_mails_2():
    recipients = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', BODY)
    content = mail_content(BODY)[0]
    message = 'Subject: {}\n\n{}'.format('DevOps KTH - PR confirmation - noreply', content)
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"

    sender_email = "devops.kth@gmail.com"  # Enter your address
    password = "devops2022"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        for receiver in recipients:
            try:
                server.sendmail(sender_email, receiver, message)
            except:
                pass

if __name__ == '__main__':
  try:
    send_mails_1()
  except:
    send_mails_2()
