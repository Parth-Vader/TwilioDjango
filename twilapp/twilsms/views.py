from django.shortcuts import render
from django.shortcuts import HttpResponse
from twilio.rest import Client
import time
from django.views.decorators.csrf import csrf_exempt

#Twilio Account details
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

#I have ignored CSRF verification for now.
@csrf_exempt
def sendsms(number,body_sms):
    client.api.account.messages.create( to=number,
                                       from_="", #Twilio number
                                       body=body_sms)
    time.sleep(2)

@csrf_exempt
def view_info(request):
    if request.method == 'POST':
        number = request.POST.get("number",None)
        body = request.POST.get("body",None)

        sendsms(number,body)
        return HttpResponse("Message Sent!")  

    else:
        return render(request,"form_twil.html")