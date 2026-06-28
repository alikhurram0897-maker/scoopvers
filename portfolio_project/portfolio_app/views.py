from django.shortcuts import render, redirect
from .models import Contact


# Home Page
def home(request):
    return render(
        request,
        'portfolio_app/home.html'
    )


# Projects Page
def project(request):
    return render(
        request,
        'portfolio_app/projects.html'
    )


# Contact Page
def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")

        email = request.POST.get("email")

        subject = request.POST.get("subject")

        message = request.POST.get("message")


        Contact.objects.create(

            name=name,

            email=email,

            subject=subject,

            message=message

        )


        return redirect('contact')


    return render(
        request,
        'portfolio_app/contact.html'
    )