from django.shortcuts import render,HttpResponse
from django.urls import path, include
from app import views
from django.views import View
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
  
  
     path('',views.myHome.as_view(),name="home"),
    path('/',views.myHome.as_view(),name="home"),
    path('product_add_to_explore/<slug>',views.explore_list_product,name=''),
    
    path('home/after_product_click/<slug>',views.after_product_click.as_view(),name="after_product_click"),
    path('home/manufacturs',views.Manufacturs_view.as_view(),name="manufature"),
    path('home/all_category',views.all_category_view.as_view(),name="all_category"),
    path('home/tech_support',views.tech_support_view.as_view(),name="tech_support"),
    path('home/company_searvice',views.tech_support_view.as_view(),name="tech_support"),
     path('home/logistic',views.logistic_view.as_view(),name="tech_support"),
   
    path('nav/why_we_are',views.why_we_are.as_view(),name="nav"),
    path('nav/contract',views.contract.as_view(),name="nav"),
    path('nav/help',views.help.as_view(),name="help"),
   path('nav/product_ordered',views.product_ordered_view.as_view(),name="nav"),
  path('nav/product_wish_list',views.product_wish_list_view.as_view(),name="nav"),  
   
    path('user/',views.user.as_view(),name="nav"),
    path('user/<pk>',views.user_update.as_view(),name="nav"),
    #path('user/<pk>',views.user.as_view(),name="nav"),
    
    path('home/login',views.login.as_view(),name="login"),
    path('home/logout',views.logout.as_view(),name="logout"),
     path('home/login/create_account',views.create_account.as_view(),name="create_account"),
    
    path('home/login/change_pass',views.change_pass.as_view(),name="change_pass"),
    path('home/search',views.search.as_view(),name="search"),
    path('home/search/',views.search.as_view(),name="search"),
    path('search/search_user',views.search_user.as_view(),name="search"),
    path('home/search_user',views.search_user.as_view(),name="search"),
    path('home/News',views.News.as_view(),name="news"),
    path('home/requirement',views.requirement_view.as_view(),name="requirement"),
    
    path('product/enquiry',views.enquiry_view.as_view(),name="enquiry"),
    path('home/after_product_click/product/enquiry/<slug>',views.enquiry_view.as_view(),name="enquiry"),
    path('nav/shiping_enquiry',views.shiping_enquiry_form_view.as_view(),name="shipment_enquiry"),
   
    
    
    path('product_manager/manager_account_update/<slug>',views.manager_account_update_view.as_view(),name="manager_account_upadate"),
    
    
    
    path('product_manager/My_products',views.My_Products_view.as_view(),name="My_Products"),
    
    path('product_manager/My_products_delete/<slug>',views.My_Products_View_Delete.as_view(),name="My_Products_delete_Form"),
    path('product_manager/manager_account_form',views.manager_account_form_view.as_view(),name="manager_account"),
  path('product_manager/My_products_update/<slug>',views.My_Products_View_Update.as_view(),name="My_Products_Update_Form"),  
    
    
    
    path('product_manager/Order_get',views.Orders_Come_in_view.as_view(),name="Orders_come_in"),
  #order delete
    path('product_manager/Order_get_delete/<slug>',views.Orders_Come_in_view_delete.as_view(),name="Orders_come_in_delete"),
    
    path('product_manager/graph',views.Graph_view.as_view(),name="performance"),
    
    
    
    
    path('home/nav/add_products',views.add_products_view.as_view(),name="navpage"),
    path('home/add_products/see_product_gig',views.see_product_gig_view.as_view(),name="navpage"),
 
    
]
