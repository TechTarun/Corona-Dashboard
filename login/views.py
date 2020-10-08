from django.shortcuts import render

# Create your views here.
def getform(request):
    return render(request, 'login/login.html', {'message' :""})

def verifylogin(request):
    is_verified = False
    # logic for verfication
    if is_verified == True:
        return render(request, 'home/home.html')
    else:
        return render(request, 'login/login.html', {'message': "Credentials are wrong!!"})
