from django.http import HttpResponse
from django.shortcuts import render,redirect
def home(request):
    from django.shortcuts import render,redirect
    return render(request,"index.html")
def result(request):
    from django.shortcuts import render,redirect
    number=request.GET['G']
    
    from twilio.rest import Client
    
    sid='ACad20495dd3bf324541f3c9a60657ddf9'
    authToken='06fbf11c35fb80bb47a24105f33cd18d'

    client=Client(sid,authToken)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+919863103113'
    
    message=client.messages.create(body=number,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    import random
    str_number='+91'+str(number)
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
        return redirect("https://xeroxdetail.herokuapp.com/")
    else:
        return render(request,"index2.html")
