from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from allauth.account.forms import AddEmailForm
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated


def home(request):
    return render(request, "index.html")

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

@login_required
def email_view(request):
    emailaddresses = EmailAddress.objects.filter(user=request.user)  # Fetch emails
    form = EmailForm()

    return render(request, "account/email.html", {
        "emailaddresses": emailaddresses,
        "form": form,
        "can_add_email": True,  # Ensure this is properly set
    })\

@login_required
def home_json(request):
    return JsonResponse({
        "email": request.user.email,
        "username": request.user.username
    })


class HomeViwew(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self,request,*args, **kwargs):
        return Response({
            "email": request.user.email
        })