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
    
    sid='ACc536c7fac505fff2f410b3d6d31f876f'
    authToken='0cb21332809498875ab1ebb2e99cb7f7'
    client=Client(sid,authToken)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+919774141994'
    
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
