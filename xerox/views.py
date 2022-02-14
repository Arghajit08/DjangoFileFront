from django.http import HttpResponse
from django.shortcuts import render,redirect
def home(request):
    from django.shortcuts import render,redirect
    return render(request,"index.html")
def result(request):
    from django.shortcuts import render,redirect
    name=request.GET['name']
    address=request.GET['P']
    number=request.GET['G']
    document=request.GET['category']
    print(document)
    from twilio.rest import Client
    import random
    
    sid='ACad20495dd3bf324541f3c9a60657ddf9'
    authToken='d380ee5774d810f58cc5fb3f8cd89b85'

    client=Client(sid,authToken)
    str_number='+91'+str(number)

    
    sid1='ACdc82b5afee95e7d01d983bfa471b869a'
    authToken1='1ef64a3025557673b50064bc1b1009e4'
    
    client1=Client(sid1,authToken1)

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
    import requests
    url='https://www.fast2sms.com/dev/bulkV2'
    n=random.randint(1000,9999)
    message=str(n)
    numbers=str(number)
    payload= f'sender_id=TXTIND&message={message}&language=english&route=p&numbers={numbers}'
    headers= {'authorization':'HGZXp9BAmOQjh8LKIaf3F75UuSrkYtWEd0neslioVTzJgPxNR4H0Z3RoUcaJxEsFCX8nWQgPmItKVpGd','Content-Type':'application/x-www-form-urlencoded'}
    response=requests.request('POST',url,data=payload,headers=headers)
    print(response.text)
    return render(request,"index1.html",{'otp':n})
    
def otp_verification(request):
    actual=request.GET['otp1']
    new=request.GET['abc']
    if actual==new:
        return redirect("https://xeroxfin.herokuapp.com/")
    else:
        return render(request,"index2.html")
