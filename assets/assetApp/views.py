from django.shortcuts import render,redirect
from django.contrib import messages
# from django.urls import reverse
from .models import Employee,Company,Category,Assets
from django.conf import settings
# from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
   return render(request, 'index.html')

def conts(request):
    return render(request,'conts.html')
 
# @login_required
def dash(request):
   return render(request,'dashboard.html')


def comp(request):
   comps=Company.objects.all()
   if request.method =='POST':
      name=request.POST.get('name')
      address=request.POST.get('address')
      city=request.POST.get('city')
      email=request.POST.get('email')
      phone=request.POST.get('phone')
      
      company=Company(name=name,address=address,city=city,email=email,phone=phone)
      
      company.save()
      messages.success(request,'Employee Company Succesifully')
      return redirect('comp')
   return render(request,'comp.html',{'emps':comps})
   

def emp(request):
   if request.method =='POST':
      name=request.POST.get('name')
      address=request.POST.get('address')
      city=request.POST.get('city')
      email=request.POST.get('email')
      phone=request.POST.get('phone')
      
      employee=Employee(name=name,address=address,city=city,email=email,phone=phone)
      
      employee.save()
      messages.success(request,'Employee Added Succesifully')
      return redirect('emp')
   return render(request,'emp.html')

def recs(request):
   
   if request.method == 'POST':
      name=request.POST.get('name')
      desc=request.POST.get('desc')
      
      records=Category(name=name,desc=desc)
      records.save()
      messages.success(request,'Category Added Succesifully')
      return redirect('recs')
      
   return render(request,'recs.html')
def assets(request):
    comps = Company.objects.all()
    cats = Category.objects.all()
    emps = Employee.objects.all()

    if request.method == 'POST':
        aNumber = request.POST.get('aNumber')
        desc = request.POST.get('desc')
        tag = request.POST.get('tag')
        employees = request.POST.getlist('employee')  # Use getlist() for many-to-many fields
        categories = request.POST.getlist('category')  # Use getlist() for many-to-many fields
        companies = request.POST.getlist('company')  # Use getlist() for many-to-many fields

        asst = Assets(aNumber=aNumber, desc=desc, tag=tag)
        asst.save()

        # Update many-to-many relationships using set()
        asst.employee.set(Employee.objects.filter(pk__in=employees))
        asst.category.set(Category.objects.filter(pk__in=categories))
        asst.company.set(Company.objects.filter(pk__in=companies))
        print("Categories:", categories)


        messages.success(request, 'Assets Added Successfully')
        return redirect('assets')

    return render(request, 'assets.html', {'emps': emps, 'cats': cats, 'comps': comps})
def aRep(request):
   assets=Assets.objects.all()
   return render(request,'assReport.html',{'assets':assets})

from reportlab.pdfgen import canvas
# your_app/views.py
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Assets

def generate_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="assets_report.pdf"'

    # Create PDF report using ReportLab
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "Assets Report")

    # Fetch data from the database
    assets = Assets.objects.all()

    # Iterate through assets and add to the PDF
    y_position = 780
    for asset in assets:
        pdf.drawString(100, y_position, f"Asset Number: {asset.aNumber}")
        pdf.drawString(100, y_position - 20, f"{asset.employee}")
        pdf.drawString(100, y_position - 40, f"{asset.company}")
        pdf.drawString(100, y_position - 60, f"{asset.category}")
        pdf.drawString(100, y_position - 80, f"{asset.tag}")
        pdf.drawString(100, y_position - 90, f"{asset.desc}")
        # Add more data as needed...
        y_position -= 20

    pdf.save()
    return response
 
def uRep(request):
   employees=Employee.objects.all()
   return render(request,'uReport.html',{'employees':employees})

from django.http import HttpResponse
from reportlab.pdfgen import canvas


def generate_reportU(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Users_report.pdf"'

    # Create PDF report using ReportLab
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "Users Report")

    # Fetch data from the database
    employees = Employee.objects.all()

    # Iterate through employees and add to the PDF
    y_position = 780
    for employee in employees:
        pdf.drawString(100, y_position, f"Employee Name: {employee.name}")
        pdf.drawString(100, y_position - 20, f"Employee Address: {employee.address}")
        pdf.drawString(100, y_position - 40, f"Employee City: {employee.city}")
        pdf.drawString(100, y_position - 60, f"Employee Email: {employee.email}")
        pdf.drawString(100, y_position - 80, f"Employee Phone: {employee.phone}")
        
        # Add more data as needed...
        y_position -= 100  # Adjust the value based on the space needed for each employee

    pdf.save()
    return response


def cRep(request):
   companys=Company.objects.all()
   return render(request,'comReport.html',{'companys':companys})



def generate_reportCom(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Company_report.pdf"'

    # Create PDF report using ReportLab
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "Company Report")

    # Fetch data from the database
    companys = Company.objects.all()

    # Iterate through company and add to the PDF
    y_position = 780
    for company  in companys:
        pdf.drawString(100, y_position, f"Company Name: {company.name}")
        pdf.drawString(100, y_position - 20, f"Company  Address: {company.address}")
        pdf.drawString(100, y_position - 40, f"Company  City: {company.city}")
        pdf.drawString(100, y_position - 60, f"Company Email: {company.email}")
        pdf.drawString(100, y_position - 80, f"Company  Phone: {company.phone}")
        
        # Add more data as needed...
        y_position -= 100  # Adjust the value based on the space needed for each employee

    pdf.save()
    return response


def catRep(request):
   categories=Category.objects.all()
   return render(request,'catReport.html',{'categories':categories})




def generate_reportCat(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Category_report.pdf"'

    # Create PDF report using ReportLab
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 800, "Category Report")

    # Fetch data from the database
    categories=Category.objects.all()

    # Iterate through company and add to the PDF
    y_position = 780
    for category  in  categories:
        pdf.drawString(100, y_position, f"Category Name: {category.name}")
        pdf.drawString(100, y_position - 20, f"Category  Description: {category.desc}")
        
        
        # Add more data as needed...
        y_position -= 100  # Adjust the value based on the space needed for each employee

    pdf.save()
    return response


