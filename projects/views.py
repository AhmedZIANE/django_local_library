from django.shortcuts import render

import re



from .forms import NameForm
from .models import Contact
# Create your views here.

def index(request):
    if request.method == 'POST':

        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        message =  request.POST.get("message", "")

        flag = True
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if re.search(regex,email):
            emailError = ''
        else:
            emailError = 'Non valid mail'
            flag = False

        contact = Contact(name = name, email = email, phone = phone, message = message)

        if flag == True :
            contact.save()
            context = {'errors' : {'nameError': '', 'emailError' : emailError, 'phoneError' : '', 'messageError' : ''}}
        else:
            context = {'errors' : {'nameError': '', 'emailError' : emailError, 'phoneError' : '', 'messageError' : ''}, 'contact' : contact}
            
        return render(request, 'projects/index.html', context)

    return render(request, 'projects/index.html')