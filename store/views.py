from django.shortcuts import render
from . models import Sub_category, Product, Sub_product,Vendor,Contact,Front,Market
# Create your views here.


def index(request):

    market = Market.objects.all()
    front = Front.objects.all()
    sub_category = Sub_category.objects.all()
    product = Product.objects.all()
    sub_product = Sub_product.objects.all()
    vendor = Vendor.objects.all()
    context = {
        'market': market,
        'sub_category': sub_category,
        'product': product,
        'sub_product': sub_product,
        'vendor': vendor,
        'front': front,

    }
    return render(request, 'index.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()      
    
    return render(request, 'contact.html',)



# def cart(request):
#      return render(request, 'cart.html',)


# def checkout(request):
#     return render(request, 'checkout.html',)


# def shop(request):
#     return render(request, 'shop.html',)

# def detail(request):
#     return render(request, 'detail.html',)m django.shortcuts import render

# Create your views here.
