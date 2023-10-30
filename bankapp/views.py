from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import application,District,Branch
from django.views.generic.detail import DetailView
# Create your views here.

def test(request):

    return render(request, 'index.html')
def get_items(request, district_id):
    items = Branch.objects.filter(district_id=district_id)
    data = [{'id': item.id, 'name': item.name} for item in items]
    return JsonResponse(data, safe=False)




@login_required
def add_application(request):
    debit, credit, cheque = 0, 0, 0
    dist = District.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        DOB = request.POST.get('DOB')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        district = request.POST.get('district')
        branch = request.POST.get('branch')
        account_type = request.POST.get('account_type')
        debit = request.POST.get('debit')
        #user= request.user
        if debit == None:
            debit=False
        credit = request.POST.get('credit')
        if credit == None:
            credit=False
        cheque = request.POST.get('cheque')
        if cheque == None:
            cheque=False
        application_details = application(name=name,email=email, gender=gender, DOB=DOB, age=age, phone_number=phone_number,
                                          address=address, account_type=account_type,debit=debit,credit=credit,cheque=cheque,district_id=district,branch_id=branch,application_user=request.user)

        application_details.save()

        return redirect('bankapp:confirm')
#

    return render(request,'add.html',{'district':dist})

def details_application(request):

    details=application.objects.filter(application_user=request.user)
    return render(request, 'myapplication.html', {'details': details})

def edit(request,id):
    app=application.objects.get(id=id)
    form=ApplicationForm(request.POST or None,request.FILES,instance=app)
    if form.is_valid():
        form.save()
        return redirect('bankapp:details')
    return render(request,"edit.html",{'form':form,'app':app})

def delete (request,id):
    if request.method == 'POST':

        app=application.objects.get(id=id)
        app.delete()
        return redirect('bankapp:details')
    return  render(request,"delete.html")

class DetailListview(DetailView):
    model = application
    template_name = 'details.html'
    context_object_name = 'app'

def confirmation(request):
    return render(request,'confirmation.html')