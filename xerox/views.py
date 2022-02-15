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
        return redirect("https://xeroxfin.herokuapp.com/")
    else:
        return render(request,"index2.html")
