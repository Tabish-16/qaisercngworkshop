import json
from django.db.models import Sum, F
from django.http import JsonResponse
from django.utils.dateparse import parse_date
import datetime
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from OilTraders.models import *
from sms import send_sms
from django.core import serializers 
from fpdf import FPDF
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail




def home(request):
    context = {}
    if request.method == 'POST':
        search = request.POST.get('search_input', '').lower()
        if search and 'search' in request.POST:
            filter_entries = NewEntry.objects.filter(registeration_num=search)
            context['filter'] = filter_entries if filter_entries.exists() else None
            if not filter_entries.exists():
                context['message'] = "No entries found matching the search criteria."
    return render(request, 'index.html', context)


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        user = authenticate(request, username=name, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to a home page or any other page
        else:
            return redirect('home')


def logoutUser(request):
    if request.user.is_authenticated:
        auth_logout(request)
    else:    
        return redirect("home")
    return redirect('home')    
@login_required        
def dashboard(request):
    entries = NewEntry.objects.all().order_by('-id')
    oil_companies = Oil_Companies.objects.all()
    body_parts = Body_Parts.objects.all()
    spare_parts = Spare_Parts.objects.all()
    cng_parts = CNG_Parts.objects.all()
    kabli_parts = Kabli_Parts.objects.all()
    silencer = Silencer.objects.all()
    decoration = Decoration.objects.all()
    oil_filter = Oil_Filter.objects.all()
    air_filter = Air_Filter.objects.all()
    ac_filter = AC_Filter.objects.all()
    whole_sale = Whole_Sale.objects.all()
    
    all_oil = serializers.serialize('json',oil_companies)    
    existing_entries = serializers.serialize('json', entries)    
    all_body_parts = serializers.serialize('json', body_parts)    
    all_spare_parts = serializers.serialize('json', spare_parts)    
    all_cng_parts = serializers.serialize('json', cng_parts)    
    all_kabli_parts = serializers.serialize('json', kabli_parts)    
    all_silencer = serializers.serialize('json', silencer)    
    all_decoration = serializers.serialize('json', decoration)    
    all_oil_filter = serializers.serialize('json', oil_filter)    
    all_air_filter = serializers.serialize('json', air_filter)    
    all_ac_filter = serializers.serialize('json', ac_filter)    
    all_wholeSale = serializers.serialize('json', whole_sale)    
    
    return render(request,'dashboard.html',{
                    'entries':entries,
                    'existing_entries':json.loads(existing_entries),
                    "all_oil":all_oil,
                    "all_body_parts":all_body_parts,
                    "all_spare_parts":all_spare_parts,
                    "all_cng_parts":all_cng_parts,
                    "all_kabli_parts":all_kabli_parts,
                    "all_silencer":all_silencer,
                    "all_decoration":all_decoration,
                    "all_oil_filter":all_oil_filter,
                    "all_air_filter":all_air_filter,
                    "all_ac_filter":all_ac_filter,
                    "all_wholeSale":all_wholeSale,
                    })


    # Send an email to the admin
    # subject = 'Low Product Alert'
    # message = 'The product ' + product + ' is running low. Please restock ASAP.'
    # send_mail(
    #     subject,
    #     message,
    #     "tabishali121619@gmail.com",
    #     ["tabishyt121619@gmail.com"],
    #     fail_silently=False,
    # )
    

def subtract_product_quantity(product_data, model_class, product_name_key='name', quantity_key='qty'):
    try:
        
        if product_data:
            if isinstance(product_data, list) and product_data:
                product_list = product_data[0]
                
                if isinstance(product_list, dict):
                    product_quantity = int(product_list.get(quantity_key, 0))
                    if product_quantity > 0:
                        product = model_class.objects.get(name=product_list[product_name_key])
                        subtract = product.total_products - product_quantity
                        product.total_products = subtract
                        product.save()
                        # if product.total_products < 10:
                        #      message = alertLowProduct(product)  # Get the alert message
                             
                        #      return JsonResponse({"message": str(message)})
                            
                        # else:
                        #     return JsonResponse({"message": ""})
                else:
                    print("Product List is not a dictionary:", type(product_list))
            else:
                print("Product Data is not a list or is empty:", type(product_data))
    except Exception as e:
        print("Product error:", e)


def alertLowProduct(request):
    try:
        messages = []

        # Check each model for low stock and add message to list
        for model_class in [Oil_Companies, Oil_Filter, Air_Filter, AC_Filter, Body_Parts, Spare_Parts, CNG_Parts, Kabli_Parts, Decoration, Whole_Sale, Silencer]:
            for data in model_class.objects.all():
                if data.total_products < 10:
                    messages.append(f"The product {data.name} is running low. Please restock ASAP")

        return JsonResponse({"messages": messages})
    except Exception as e:
        print("Error:", e)
        return JsonResponse({"messages": ["An error occurred."]}, status=500)
    
    
    
def product_subtract(data):
    try:
        oil_companies_data = json.loads(data.get('engin_oil_data', '[]'))
        subtract_product_quantity(oil_companies_data, Oil_Companies)
    except Exception as e:
        print("Oil filter error:", e)
    
    try:
        oil_filter_data = json.loads(data.get('oil_filter_data', '[]'))
        subtract_product_quantity(oil_filter_data, Oil_Filter)
    except Exception as e:
        print("Oil filter error:", e)
    
    try:
        ac_filter_data = json.loads(data.get('ac_filter_data', '[]'))
        subtract_product_quantity(ac_filter_data, AC_Filter)
    except Exception as e:
        print("AC filter error:", e)
    
    try:
        air_filter_data = json.loads(data.get('air_filter_data', '[]'))
        subtract_product_quantity(air_filter_data, Air_Filter)
    except Exception as e:
        print("Air filter error:", e)
    
    try:
        bodyPartEntry_data = json.loads(data.get('body_parts_data', '[]'))
        subtract_product_quantity(bodyPartEntry_data, Body_Parts)
    except Exception as e:
        print("Body part error:", e)
    
    try:
        sparePartEntry_data = json.loads(data.get('spare_parts_data', '[]'))
        subtract_product_quantity(sparePartEntry_data, Spare_Parts)
    except Exception as e:
        print("Spare part error:", e)
    
    try:
        cngPartEntry_data = json.loads(data.get('cng_parts_data', '[]'))
        subtract_product_quantity(cngPartEntry_data, CNG_Parts)
    except Exception as e:
        print("CNG error:", e)
    
    try:
        kabliPartEntry_data = json.loads(data.get('kabli_parts_data', '[]'))
        subtract_product_quantity(kabliPartEntry_data, Kabli_Parts)
    except Exception as e:
        print("Kabli error:", e)
    
    try:
        decorationEntry_data = json.loads(data.get('decoration_parts_data', '[]'))
        subtract_product_quantity(decorationEntry_data, Decoration)
    except Exception as e:
        print("Decoration error:", e)
    
    try:
        silencerEntry_data = json.loads(data.get('silencer_parts_data', '[]'))
        subtract_product_quantity(silencerEntry_data, Silencer)
    except Exception as e:
        print("Silencer error:", e)
    
    try:
        wholeSaleEntry_data = json.loads(data.get('whole_sale_data', '[]'))
        subtract_product_quantity(wholeSaleEntry_data, Whole_Sale)
    except Exception as e:
        print("Whole sale error:", e)



def new_entry(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode())
            try:
                product_subtract(data)
            except Exception as e:
                print(e)    
            saveData = NewEntry(
                name=data.get('name'),
                phone_number=data.get('phone'),
                vehicle=data.get('vehicle'),
                registeration_num=data.get('registration_num'),
                date=data.get('date'),
                last_reading=data.get('last_reading'),
                next_reading=data.get('next_reading'),
                next_changing_date=data.get('next_changing_date'),
                oil_companies=json.loads(data.get('engin_oil_data', {})),
                oil_filter=json.loads(data.get('oil_filter_data', {})),
                ac_filter=json.loads(data.get('ac_filter_data', {})),
                air_filter=json.loads(data.get('air_filter_data', {})),
                bodyPartEntry=json.loads(data.get('body_parts_data', {})),
                sparePartEntry=json.loads(data.get('spare_parts_data', {})),
                cngPartEntry=json.loads(data.get('cng_parts_data', {})),
                kabliPartEntry=json.loads(data.get('kabli_parts_data', {})),
                decorationEntry=json.loads(data.get('decoration_parts_data', {})),
                silencerEntry=json.loads(data.get('silencer_parts_data', {})),
                wholeSaleEntry=json.loads(data.get('whole_sale_data', {}))
            )

            saveData.save()
            if "save_view" in request.POST:
                id = (NewEntry.objects.last()).id
                url = f"/bill_pdf/{str(id)}/"
                return redirect(to=url)
            return JsonResponse({"status": "success", "message": "Data saved successfully."})

        except json.JSONDecodeError as e:
            print(e)
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Oil_Companies.DoesNotExist:
            print(e)
            return JsonResponse({"status": "error", "message": "Invalid Oil Company ID"}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

def sales_report(request):
    return render(request,'sales_report.html')

@login_required   
def generate_report(request):
    report_data = []
    if request.method == 'POST':
        month = request.POST.get('month')
        if not month:
            return HttpResponse('Month is required.', status=400)
        
        # Parse the month and calculate start and end dates
        start_date = parse_date(f"{month}-01")
        if not start_date:
            return HttpResponse('Invalid date format.', status=400)
        
        # Calculate end date by finding the first day of the next month
        next_month = start_date.month % 12 + 1
        next_year = start_date.year if start_date.month < 12 else start_date.year + 1
        end_date = parse_date(f"{next_year}-{next_month:02d}-01")
        
        # Filter entries for the selected month
        report = NewEntry.objects.filter(date__gte=start_date, date__lt=end_date)
        
        total_sales = 0
        total_profit = 0
        items_sold={
            
        }
        for entry in report:
            for part_entry in ['bodyPartEntry', 'sparePartEntry', 'cngPartEntry', 'kabliPartEntry', 'decorationEntry', 'silencerEntry','oil_companies','oil_filter','ac_filter','air_filter','wholeSaleEntry']:
                parts = getattr(entry, part_entry, [])
                for part in parts:
                    qty = int(part['qty'])
                    sale_price = int(part['price'])
                    product_name = part['name']

                    # Get the corresponding product model and calculate profit
                    if part_entry == 'bodyPartEntry':
                        product = Body_Parts.objects.get(name=product_name)
                    elif part_entry == 'sparePartEntry':
                        product = Spare_Parts.objects.get(name=product_name)
                    elif part_entry == 'cngPartEntry':
                        product = CNG_Parts.objects.get(name=product_name)
                    elif part_entry == 'kabliPartEntry':
                        product = Kabli_Parts.objects.get(name=product_name)
                    elif part_entry == 'decorationEntry':
                        product = Decoration.objects.get(name=product_name)
                    elif part_entry == 'silencerEntry':
                        product = Silencer.objects.get(name=product_name)
                    elif part_entry == 'oil_companies':
                        product = Oil_Companies.objects.get(name=product_name)
                    elif part_entry == 'oil_filter':
                        product = Oil_Filter.objects.get(name=product_name)
                    elif part_entry == 'ac_filter':
                        product = AC_Filter.objects.get(name=product_name)
                    elif part_entry == 'air_filter':
                        product = Air_Filter.objects.get(name=product_name)
                    elif part_entry == 'wholeSaleEntry':
                        product = Whole_Sale.objects.get(name=product_name)
                    
                    purchase_price = int(product.purchase_price)
                    
                    profit = (sale_price - purchase_price) *qty

                    # Calculate total sales and profit
                    total_sales += (sale_price * qty)  # Total sales for the quantity sold
                    total_profit += profit  # Total profit calculated above
                    
                    if product_name in items_sold:
                        items_sold[product_name]['qty'] += qty
                        items_sold[product_name]['sale_price'] += sale_price
                    else:
                        items_sold[product_name] = {
                            'product_name': product_name,
                            'qty': qty,
                            'sale_price': sale_price,
                            'single_price':sale_price,
                            'purchase_price': purchase_price,
                           
                        }
                        
            
        final_total_sales = 0
        final_total_profit =0
        final_total_unit_sale_price =0
        final_total_unit_purchase_price = 0
        final_total_item_qty = 0
        
        for k in items_sold:
            item = items_sold[k]
            final_total_unit_sale_price += item['single_price']
            final_total_unit_purchase_price += item['purchase_price'] 
            final_total_item_qty += item['qty']
            final_total_sales += item['sale_price']
            total_purchase_price = item['purchase_price'] * item['qty']          
            current_item_profit = item['sale_price'] - total_purchase_price
            items_sold[k]['profit'] = current_item_profit
            final_total_profit += current_item_profit
        
        context = {
            'total_qty':final_total_item_qty,
            "total_unit_sale_price":final_total_unit_sale_price,
            "total_unit_purchase_price":final_total_unit_purchase_price,
            'total_sales': final_total_sales,
            'total_profit': final_total_profit,
            'report_data': items_sold.values(),
            'month': month,
        }

        return render(request,"sales_report.html",context)
    return HttpResponse('Method not allowed', status=405)
    #send sms 

def sendReminders(request):
    send_sms(
    'Here is the message',
    '+923168771688',
    ['+923185858855'],
    fail_silently=True
    )    
    return HttpResponse('message sent')

class POSReceipt(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', (80, 150))

    def header(self):
        pass

    def footer(self):
        pass

def invoice_pdf(request,pk):
    # Create instance of POSReceipt
    pdf = POSReceipt()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial","B" ,size=14)

    
    
    invoice = NewEntry.objects.get(id=pk)
    # Add content
    pdf.set_fill_color(28, 28, 28) 
    pdf.rect(0,0,80,20,"DF")
    pdf.image("static/assets/QCW-removebg-preview.png", x=5, y=2.5, w=25, h=15)
    pdf.set_text_color(122, 122, 122)
    pdf.text(57,9,"Qaiser")
    pdf.set_font("Arial","B" ,size=10)
    pdf.text(50,15," CNG Workshop")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", "B",size=10)
    pdf.set_y(25)
    pdf.cell(35, 10, f"Name",)
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, invoice.name, ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Phone Number", )
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, invoice.phone_number, ln=True,)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Vehicle", )
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, invoice.vehicle, ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Registration num")
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, invoice.registeration_num, ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Date")
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, str(invoice.date), ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Last Reading")
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, invoice.last_reading, ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Next Reading")
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, invoice.next_reading, ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 10, f"Changing Date")
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 10, str(invoice.next_changing_date), ln=True)
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(0, 10, "---------------------------", ln=True,align="C")
    
    pdf.set_y(40)
    pdf.set_fill_color(28, 28, 28) 
    pdf.rect(0,130,80,20,"DF")
    pdf.set_text_color(122, 122, 122)
    pdf.set_font("Arial", "B",size=9)
    pdf.text(3,135,"Contact Us")
    pdf.text(3,139,"0300-8339202")
    pdf.text(50,135,"Our Location")
    pdf.text(37,139,"G.T Road Wah Garden Pull")

    # Get the PDF content as a string
    pdf_output = pdf.output(dest='S').encode('latin1')

    # Create the HttpResponse object with the appropriate PDF headers
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{invoice.name}-invoice.pdf"'

    return response




class POSBill(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', (80, 150))
        self.set_font('Arial', '', 12)
        
    def header(self):
        self.set_fill_color(28, 28, 28) 
        self.rect(0,0,80,20,"DF")
        self.image("static/assets/QCW-removebg-preview.png", x=5, y=2.5, w=25, h=15)
        self.set_text_color(122, 122, 122)
        self.text(57,9,"Qaiser")
        self.set_font("Arial","B" ,size=10)
        self.text(50,15," CNG Workshop")
        self.set_text_color(0, 0, 0)
        self.set_font("Arial", "B",size=10)
        self.set_y(20)
        self.set_x(2)
        self.set_font("Arial", "B",size=10)
        self.cell(35, 10, f"Items",)
        self.cell(10, 10, f"Qty",)
        self.cell(30, 10, "Price", ln=True, align="R")

    def footer(self):
        self.set_y(40)
        self.set_fill_color(28, 28, 28) 
        self.rect(0,130,80,20,"DF")
        self.set_text_color(122, 122, 122)
        self.set_font("Arial", "B",size=9)
        self.text(3,135,"Contact Us")
        self.text(3,139,"0300-8339202")
        self.text(50,135,"Our Location")
        self.text(37,139,"G.T Road Wah Garden Pull")

def bill_pdf(request, pk):
    # Create instance of POSBill
    pdf = POSBill()
    
    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Arial","B" ,size=14)
    
    bill = NewEntry.objects.get(id=pk)
    
    # Add content
    total = 0
    
    def add_part_entries(part_entries):
        nonlocal total
        if isinstance(part_entries, list):  # Ensure part_entries is a list
            for data in part_entries:
                if isinstance(data, dict):  # Ensure data is a dict
                    pdf.set_x(2)
                    pdf.set_font("Arial", "B", size=10)
                    pdf.cell(35, 7, data.get('name', ''))
                    pdf.set_font("Arial", size=10)
                    pdf.cell(10, 7, str(data.get('qty', 0)), align="C")
                    pdf.cell(30, 7, str(data.get('price', 0)) + " /-", ln=True, align="R")
                    total += int(data.get('price', 0))  # Safely convert to int

    # Add totals for all part entries
    add_part_entries(bill.bodyPartEntry)
    add_part_entries(bill.sparePartEntry)
    add_part_entries(bill.cngPartEntry)
    add_part_entries(bill.kabliPartEntry)
    add_part_entries(bill.decorationEntry)
    add_part_entries(bill.oil_companies)  # Ensure this is iterable and correct
    add_part_entries(bill.oil_filter)  # Ensure this is iterable and correct
    add_part_entries(bill.ac_filter)  # Ensure this is iterable and correct
    add_part_entries(bill.air_filter)  # Ensure this is iterable and correct
    add_part_entries(bill.wholeSaleEntry)  # Ensure this is iterable and correct
        
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(0, 4, "----------------------------------------------------", ln=True, align="C")
    
    pdf.set_font("Arial", "B",size=10)
    pdf.cell(35, 5, f"Total", align="L")
    
    pdf.set_font("Arial", size=10)
    pdf.cell(40, 5, str(total) + "/-", ln=True)
    
    # Get the PDF content as a string
    pdf_output = pdf.output(dest='S').encode('latin1')

    # Create the HttpResponse object with the appropriate PDF headers
    response = HttpResponse(pdf_output, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="{bill.name}-invoice.pdf"'

    return response