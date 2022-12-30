from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.man import store_man
from .views.woman import store_woman
from .views.beauty import store_beauty
from .views.child import store_child
from .views.child_female import store_child_female
from .views.child_male import store_child_male
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('Erkek', store_man , name='man'),
    path('Kadin', store_woman , name='woman'),
    path('Guzellik', store_beauty, name='beauty'),
    path('Cocuk', store_child, name='child'),
    path('Kiz-Cocuk', store_child_female, name='child_female'),
    path('Erkek-Cocuk', store_child_male, name='child_male'),
    

]
