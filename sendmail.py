#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(email_message, to_email, student_name, my_password):

	# me == my email address
	# you == recipient's email address
	me = "####YOUREMAIL####"
	you = to_email
	subjectline = "Derek Adam: Piano lessons for " + student_name

	password = my_password
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subjectline
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	text = str(email_message)
	html = email_message

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.gmail.com', 587)

	s.ehlo()
	s.starttls()
	s.login(me, password)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(me, you, msg.as_string())
	s.quit()
