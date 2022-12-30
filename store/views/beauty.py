from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View

def store_beauty(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
  
  
    categories = Category.get_beauty_categories()
   
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
        
    else:
        products = Products.get_all_products();

    data = {}
    data['products'] = products
    data['categories'] = categories


    print('you are : ', request.session.get('email'))
    return render(request, 'beauty.html', data)


