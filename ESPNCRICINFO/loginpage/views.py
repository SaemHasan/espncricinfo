from django.shortcuts import render, redirect


# Create your views here.

loggedin = False

def login(request):
    if request.method == 'GET':
        return render(request, 'loginpage/index.html')
    else:
        email = request.POST['email']
        password = request.POST['pass']
        if(email =="sayim.hasan30@gmail.com" and password=='sayem'):
            loggedin=True
            return render(request, 'adminpage/index.html', {'loggedin': loggedin})
        else:
            return render(request, 'loginpage/index.html', {"error": "*email or password is wrong"})


def getlogin():
    return loggedin