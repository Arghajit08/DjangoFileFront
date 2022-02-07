from django.http import HttpResponse
from django.shortcuts import render,redirect
def home(request):
    return render(request,"index.html")
def result(request):
    name=request.GET['name']
    address=request.GET['P']
    number=request.GET['G']
    document=request.GET['category']
    print(document)
    from twilio.rest import Client
    
    sid='ACad20495dd3bf324541f3c9a60657ddf9'
    authToken='b0daf1649d72fdaaeb2c94404eedc7db'
    client=Client(sid,authToken)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+919863103113'
    
    message=client.messages.create(body=name,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    message=client.messages.create(body=address,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)

    message=client.messages.create(body=number,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    message=client.messages.create(body=document,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    return redirect("https://xeroxfin.herokuapp.com/")
