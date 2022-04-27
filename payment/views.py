from locale import currency
from django.http import JsonResponse,HttpResponse
# from django.shortcuts import redirect, render
from django.conf import settings
from django.shortcuts import render
# from stripe import Charge
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import stripe
from .models  import Products,Cart
from .forms import Productform

#defining global variable
# mycartlist= mylist

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'base.html'
    # stripe.api_key = settings.STRIPE_SECRET_KEY
  
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config)



@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        products = Cart.objects.values() 
       
            
        cartlist=[]
        for i in products:
            dic = {'name':'name','quantity':'quantity','currency':'currency','amount':'amount'}
            dic['name']= i['name']
            dic['quantity']= i['quantity']
            dic['currency']= i['currency']
            dic['amount']= i['amount']
            cartlist.append(dic)
        
        print("))))))))))))))))))))))))))))))))))))))",cartlist)
        # line_items1=[]
        # for i in range(len(products)):
        #     iteams= {"name":'name',"quantity": 0,"currency": "currency","amount" : "amount"}
        #     name=products[i]['name']
        #     iteams['name']=name
        #     quantity=int(products[i]['quantity'])
        #     iteams['quantity']=quantity
        #     currency=products[i]['currency']
        #     iteams['currency']=currency
        #     amount=products[i]['amount']
        #     iteams['amount']=amount

        #     line_items1.append(iteams)

        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,

                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items= cartlist
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})



def successView(request):
    # template_name = 'success.html'
    return render(request,'success.html')


#For display products on dashboard
def products(request):

    iteams = Products.objects.values()
    names=[]
    imgs=[]
    for i in range(len(iteams)):
        name=iteams[i]['name']
        img=iteams[i]['img']
        names.append(name)
        imgs.append(img) 

    
    return render(request, 'base.html',{'names':names,'imgs':imgs })
    
        
#to add new products on your dashborad
def add_products(request):
    if request.method == 'POST':
        form = Productform(request.POST,request.FILES)
        if form.is_valid():
            name = request.POST['name']
            quantity = request.POST['quantity']
            currency = request.POST['currency']
            amount = request.POST['amount']
            img = request.FILES['img']
            user = Products(name = name, quantity = quantity, currency = currency,amount=amount,img=img)
            user.save()

    else:
        form = Productform()
        
    return render(request, 'add_products.html',{'form':form})

class CancelledView(TemplateView):
    template_name = 'cancelled.html'


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)

@csrf_exempt
def mycart(request):
    if request.method == 'POST':
        id = request.POST['id']
        added_product = Products.objects.get(name=id)
        name = id
        quantity = added_product.quantity
        currency = added_product.currency
        amount = added_product.amount
        
        cartlist= Cart.objects.create(

            name = name,
            quantity = quantity,
            currency = currency,
            amount = amount
        )

        cartlist.save()
        return JsonResponse({'status':'Save'})
    else:
        return JsonResponse({'status': 0})


def view_cart(request):
    products = Cart.objects.values() 
    # for i in range(len(products)):
    name= products[0]['name']
    amount= products[0]['amount']


    return render(request,'cart.html',{"name":name,"amount":amount})


@csrf_exempt
def deletedata(request):
    if request.method == 'POST':
        iteam = Cart.objects.values().delete()
          
        # print("?????????????????????????",iteam)



    return JsonResponse({'status':'Save'})
    
