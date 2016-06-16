#!/usr/bin/env python
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import glob

def email123():
			recipients = ['destination email id'] #fill in
			emaillist = [elem.strip().split(',') for elem in recipients]
			msg = MIMEMultipart()
			msg['Subject'] = "subject"				#fill in
			msg['From'] = 'from address @gmail.com'	#fill in
			msg['Reply-to'] = 'from address@gmail.com'	#fill in
			 
			msg.preamble = 'Multipart massage.\n'
			 
			part = MIMEText("Email text")			#fill in
			msg.attach(part)
			 
			part = MIMEApplication(open("name_of_image.jpg","rb").read())				#fill in
			part.add_header('Content-Disposition', 'attachment', filename="name_of_image.jpg")		#fill in
			msg.attach(part)
			 

			server = smtplib.SMTP("smtp.gmail.com:587")
			server.ehlo()
			server.starttls()
			server.login("your email id", "your password")			#fill in
			 
			server.sendmail(msg['From'], emaillist , msg.as_string())




if __name__ == "__main__":

 		send_email()