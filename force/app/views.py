from django.shortcuts import render,redirect,HttpResponse
from django.views import View
# Create your views here.
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView
import requests
import random
import json
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import user_agents 
from django.contrib.auth.models import User
from django.dispatch import receiver
import datetime
# Import the receiver
#from app.models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from app.form import requirement_form,enquiry_form,manager_account_form,creat_account_form,product_add_form,shiping_enquiry_form,userprofile_form
from app.models import requirement,manager_account,product_add,product_enquiry,shiping_enquiry,UserVisit,userprofile,user_explore_list

from app.serializer import product_add_serialiser


from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic.edit import FormView,UpdateView,CreateView


from rest_framework.renderers import JSONRenderer

context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'

#home page view 
class myHome(View):
    def get(self,request):
        all_product=product_add.objects.all().values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        company_product=product_add.objects.filter(Company_Name__contains ='InterGlobe Enterprises Pvt. Ltd.' ).values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        top_rank_product=product_add.objects.filter(Views__contains = 2).values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        new_arival_product=product_add.objects.filter(Views__contains =0).values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        agriculture=product_add.objects.filter(Product_Category__contains =3).values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        user_profile='User'
     
            
            
        
        try:
            user_profile=userprofile.objects.filter(user=self.request.user ).values('id').first()
            #model_manager=manager_account.objects.get(user=request.user )
            
        except:
            return render(request,"home/home.html",{'style_weight_product':'600','all_product':all_product,'company_product':company_product,'top_rank_product':top_rank_product,'new_arival_product':new_arival_product,'agriculture':agriculture,'style_nav_item_2': context,"none_get":'none','user_profile':user_profile})
        
        finally:
            return render(request,"home/home.html",{'style_weight_product':'600','all_product':all_product,'company_product':company_product,'top_rank_product':top_rank_product,'new_arival_product':new_arival_product,'agriculture':agriculture,'style_nav_item_2': context,'user_profile':user_profile})
       
        
        
   
        
        
            
            
         
        
            
           
            
            
            

        

        
        
#explore list product         
        
        
        
        

          
            
            
            
    
 #help page view present at nav   
class help(View):
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("/home/login")
            
        
       
        
        
        return render(request,"home/help.html",{'style_nav_item_16':context   } ) 
        
    
  #why we are page view present in nav  
class why_we_are(View):
    
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("/home/login")
            
        
       
        
        return render(request,"home/why_we_are.html",{'style_nav_item_1':context   } ) 
    
    
    
    
class contract(View ,LoginRequiredMixin ):
    login_url = '/login/'
    def get(self,request):
        if request.user.is_anonymous:
            return redirect("/home/login")
            
        
       
        
        return render(request,"product_manager/contract_template.html",{'style_nav_item_9':context} )    
        
    


class user_update(UpdateView ):
    model=userprofile
    form_class=userprofile_form
    pk_url_kwarg = 'pk'
    template_name="home/user.html"
    success_url='/'
    
    error_message="something went Wrong , Try again"
    success_message="You profile successfuly created"
    def get(self,request,pk):
        model=userprofile.objects.filter(user=self.request.user)
        return render(request,'home/user.html',{'model':model,'form':userprofile_form()}
      )
  
        
class user(FormView, ):
    
    model=userprofile
    form_class=userprofile_form
    template_name="home/user.html"
    success_url='/user'
    
    error_message="something went Wrong , Try again"
    success_message="You profile successfuly created"
    
    def get_context_data(self, **kwargs):
        try:
            
            
            context = super(user,self).get_context_data(**kwargs)
        #user = self.request.user
            context["model"] =userprofile.objects.filter(user=self.request.user)#.ticket_set.all()
        #context=userprofile
            return context
        except:
            
            
            return {'form':userprofile_form()}
    
  
        
        
  
    
  
    
        
    
        
        
    def post(self,request):
        form=userprofile_form(request.POST)
        if form.is_valid():
            form_user=User.objects.get(username=self.request.user.username)
            User_Stetus=form.cleaned_data['User_Stetus']
            User_Bio=form.cleaned_data['User_Bio']
            User_Location=form.cleaned_data['User_Location']
            User_Company=form.cleaned_data['User_Company']
            User_Twitter=form.cleaned_data['User_Twitter']
            User_Website=form.cleaned_data['User_Website']
            user_profile=userprofile(user=form_user, User_Stetus= User_Stetus, User_Bio=User_Bio,User_Location=User_Location , User_Twitter=User_Twitter , User_Company= User_Company,User_Website= User_Website)
            try:
                user_profile.save()
                model=userprofile.objects.filter(user=self.request.user)
                return render(request,'home/user.html',{'model':model})
            except:
                model=userprofile.objects.filter(user=self.request.user)
                return render(request,'home/user.html',{'model':model,'form':userprofile_form()}
      )
              
            

            

class Manufacturs_view(View):
    def top_company_list(self):
        a=[]
        manager_data=manager_account.objects.all()
        for data in manager_data:
            a.append(data.Company_Name)
        return a
    
    def product_list(self):
        dic_data={}
        data=[]
        
        comp_names=self.top_company_list()
        for mang_comp in comp_names:
            products_data=product_add.objects.filter(Company_Name=mang_comp).values('Product_Price','Product_Img','slug','Company_Name')[:4]
            #data.append(products_data)
            print(products_data)
            dic_data[mang_comp]=products_data
            '''for mang_pri_ in products_data:
                data.append(mang_pri_.Product_Price)
                dic_data[mang_comp]=data'''
            if len(dic_data)>4:
                break

            
            
          
        return dic_data
            
    def get(self,request):
        #byte_data=JSONRenderer().render(self.product_list() )
        
        #json_data=json.loads(byte_data)
       # print(self.product_list())
        template_name="home/manufactures.html"
        return render(request,template_name,{'style_weight_manufacture':'600','manufacture':self.top_company_list(),'product_data':self.product_list()})
              
        
        
                    
             
        
        
def explore_list_product(request,slug):
    response=redirect('/')
  
    '''response.set_cookie(f'{datetime.date.today()}_explore_product',slug)
    cookies_ver=request.COOKIES[f'{ datetime.date.today()}_explore_product' ]'''
    
    
    data=user_explore_list(slug=slug,Email=request.user.email)
    data.save()
    
    return response                             
        
        
            
        
            
        
class product_wish_list_view(View):
    def wish_list(self,request):
        list_=[]
        model_=  user_explore_list.objects.filter(Email=request.user.email  )
        for itm in model_:
            #print(itm)
            model=product_add.objects.filter( slug=itm.slug).values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
            list_.append(model)
            
            
       
        return list_
        
        
    def get(self,request):
        #model=  user_explore_list.objects.get(Email=request.user.email  )
        
        #model=product_add.objects.get( slug=model[0].slug)
        

        model=self.wish_list(request)
        
        template_name="product_manager/product_wish_list.html"
        
        return render(request,template_name,{"wish_product":model , 'style_nav_item_15':context })
    
    
    
    
class product_ordered_view(View):
    def get(self,request):
        model=product_enquiry.objects.filter(Sender_user=request.user)
        template_name="product_manager/product_ordered.html"
        
        return render(request,template_name,{"product_ordered_by_user":model,'style_nav_item_14':context })
    
         
class all_category_view(View):
    def category_data(self):
        category=[  'Agriculture','Industrial','Mashinery', 'Electronics and House Hold Equipment', 'Packaging Material', 'Enginearing', 'Civil Engineering', 'Clothings', 'Vegetable', 'Medical']
        
        return category
    def category_product_data(self):
        data_cate=self.category_data()
        category=('1','2','3','4','5','7','8','9','10','11')
        data={}
        m=0
        for cate in category:
            products_data=product_add.objects.filter(Product_Category__contains=cate).values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        
            
            data[data_cate[m]]=products_data
            m+=1

        return data
    def get(self,request):
        
        #print(self.category_product_data())
        template_name="home/all_category.html"
        return render(request,template_name,{'products':self.category_product_data(),'category': self.category_data() })       
    

        
class tech_support_view(View):
    
    def get(self,request):
        model=product_add.objects.all().values('Product_Discription','Product_Price', 'Address', 'Views','Product_Img','slug')
        
        template_name="home/tech_support.html"
        return render(request,template_name,{"wish_product":model })
    
 
    
    
class company_searvice_view(View):
    def get(self,request):
        model=product_add.objects.all()
        template_name="home/company_searvice.html"
        return render(request,template_name,{"wish_product":model })    


    
class logistic_view(View):
    def get(self,request):
        model=product_enquiry.objects.all()
        template_name="home/logistic_searvice.html"
        return render(request,template_name,{"form":model })
    
    

    

    
    
    

class login(SuccessMessageMixin,LoginView):
    template_name="authenticate/login.html"
    success_message="You login successfuly"
    
    #context['style_nav_item']=context
    
    
    
    error_url="/"
    error_message="Wrong password or email"
    def get_context_data(self, **kwargs):
        if 'context_key' not in kwargs:  # set value if not present
            kwargs['style_nav_item_3'] = context
        return super().get_context_data(**kwargs)

   
    
   
    
    
        
        
    
            
    
        
        
    

class logout( SuccessMessageMixin, LogoutView):
    template_name="home/home.html"
    def get(self,request):
        
        messages.success(request,"you are successfuly logout")
        return redirect("/")         

 



  
       
        

      
    
    
        
   
        
            
        
        
         
        
        
        
            
        
    
    
    
        
    
class create_account( SuccessMessageMixin, FormView):
    form_class=creat_account_form
    template_name="authenticate/create_account.html"
    
    success_message="You acount creat successfuly"
    
    
   
        
        
     
       
    def post(self,request):
        try:
            
            
            #if request.method=="POST":
            username=request.POST.get("Name")
            
            
            #Last=request.POST.get("Last")
            useremail=request.POST.get("Email")
            password=request.POST.get("Password")
            NewUser=User.objects.create_user(username,useremail,password)
            NewUser.first_name=request.POST.get("Name")
            NewUser.last_name=request.POST.get("Last_Name")
            NewUser.save()
            
            messages.success(request,"you are successfuly creat account")
        
            return redirect ("/")
        except:
                messages.error(request,"user name or email have such problem ")
                return redirect("/home/login/create_account")

            
            
          
        
        
        
class change_pass(View):
    def get(self,request):
        template_name = 'authenticate/change_pass.html'
        return render(request,template_name)
    def post(self,request):
        Old_pass=request.POST.get("Old_pass")
        New_pass=request.POST.get("Confirm_pass")
        if Old_pass!=New_pass:
            messages.error(request, 'Please correct the error below.')
        
        
        user=User.objects.get(id=request.user.id)
        
        chack=user.check_password(Old_pass)
        un=user.username
        pwd=New_pass
        if chack==True:
            user.set_password(New_pass)
            user.save()
            template_name ='home/home.html'
            return render(request,template_name)
        return render(request,"authenticate/change_pass.html")
    
     
    
    
   
       
    
    
    
    
    
    
   
        
    
    
    


    
       
class News(View, LoginRequiredMixin ):
    login_url = '/login/'
    def get(self,request):
        
        if 'search' in request.GET:
            search_term=request.GET['search']
            url=f"https://gnews.io/api/v4/search?q={search_term}&token=2b3b9cae88b403ca4a651466ec9ea033&lang=en"
            req=requests.get(url=url)
            data_india=req.json()
            data_2=data_india["articles"]
            return render(request,"home/News.html",{"datanews":data_2})
        else:
            url=f"https://gnews.io/api/v4/search?q=buisness&token=2b3b9cae88b403ca4a651466ec9ea033&lang=en"
            req=requests.get(url=url)
            data_india=req.json()
            data_2=data_india["articles"]
            
            return render(request,"home/News.html",{"datanews":data_2,'style_nav_item_6':context})
            
            
            
            
        
        
        
        
                        
            
            
            
     
        
                
        
        
       
        

        
       
        
        

    

class search_user(View):
    
    
        
    def get(self,request):
        
        
        if 'search' in request.GET:
            def URL_split(string):
                return "?".join(string.split())
            URL_request=URL_split(request.build_absolute_uri())
           
            
        
            
            
                
            
       
            search_term_1=request.GET['search']
        if search_term_1=='':
            return render(request,'home/search.html')
        def remove_space(string):
            return "".join(string.split()) 
        
        def split_word(string):
            return (string.split()) 
        list=split_word(search_term_1)
        
            
            


            
        search_term=remove_space(str(search_term_1))
        
                
        
        it=0

        for it in range(len(list)) :
          
            articles=product_add.objects.filter(Product_Name__contains = list[it])
            articles_Dis=product_add.objects.filter(Product_Discription__contains= list[it])
            articles_category=product_add.objects.filter(Product_Category__contains= list[it])
            
            return render(request,'home/search.html',{'articles':articles, 'search_term':search_term_1,'articles_Dis':articles_Dis, 'articles_Price':articles_category ,'style_nav_item_4':context})
            
            
                
            '''if URL_request[:40]=='http://127.0.0.1:8000/search/search_user':
                return render(request,'home/search.html',{'articles':articles, 'search_term':search_term_1,'articles_Dis':articles_Dis, 'articles_Price':articles_category  })
            else:
                               return render(request,'home/home.html',{'articles':articles, 'search_term':search_term_1,'articles_Dis':articles_Dis, 'articles_Price':articles_category  })'''
         
            
            
            
           
        
            
   
        
        
        
                  
           
        
        
           
        
            
   
        
        
        
        
        
        

        
        
        
class after_product_click(View):
    
    def get(self,request,slug):
        articles=product_add.objects.get(slug=slug)
        #.values('Product_Discription','Product_Price','Address','Views','Product_Img','slug')
        
        View_u= articles.Views
        View_u+=1
        
        view=product_add.objects.filter(slug__contains=slug).values('Product_Discription','Product_Price','Address','Views','Product_Img','slug')
        
        view.update( Views=View_u )
        
        address=request.META.get('HTTP_X_FORWARDED_FOR')
        if request.user.is_authenticated:
            def ip():
                if address:
                    ip=address.split(',')[0].strip()
                else:
                    ip=request.META.get('REMOTE_ADDR')
                return ip
        
        
        
            def username():
                user=User.objects.get(id=request.user.id)
                return user
            def User_agent():
                if request.user_agent.is_mobile:
                    # returns True
                    a=request.user_agent.browser
                    return ('Mobile',a)
                if request.user_agent.is_tablet:
                    # returns False
                    a=request.user_agent.browser
                    return ('tablet',a)
                if request.user_agent.is_pc:
                    # returns False
                    a=request.user_agent.browser
                    return('PC',a)
           
            visitdata=UserVisit(user=username(),remote_addr=ip(), ua_string=User_agent(),hash=slug)
            visitdata.save()
            view=view.values('Product_Category')
            related_products=product_add.objects.filter(Product_Category__contains=view )
            template_name="product_manager/after_product_click.html"
            return render(request,template_name,{'products':related_products,'product':articles})
          
    
        
        
    
class search(View):
    def get(self,request):
        template_name="home/search.html"
        context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
        return render(request,template_name ,{'style_nav_item_4':context})

    
    
    
    
class requirement_view(  SuccessMessageMixin,    FormView):
    template_name = 'product_manager/requirement.html'
    form_class = requirement_form
    success_url = '/'
    success_message="form submit successfuly"
    
    
    error_url="/"
    error_message="Wrong password or email"
    '''def form_valid(self, form):
        
        form.save()
        return super().form_valid(form)'''
    def get_context_data(self, **kwargs):
        if 'context_key' not in kwargs:  # set value if not present
            kwargs['style_nav_item_5'] = context
        return super().get_context_data(**kwargs)
    
    def post(self,request):
        user=User.objects.get(username=self.request.user.username)
        Product_Name=request.POST.get('Product_Name')
        Product_Category=request.POST.get('Product_Category')
        Comp_Name=request.POST.get('Comp_Name')
        Mobile_No=request.POST.get('Mobile_No')
        Discription=request.POST.get('Discription')
        model=requirement(user=user,Product_Name=Product_Name,Product_Category=Product_Category,Comp_Name=Comp_Name,Mobile_No=Mobile_No,Discription=Discription)
        model.save()
        messages.success(request,"you are successfuly send requirement")
        return redirect('/')
        
    
    
    
class enquiry_view( SuccessMessageMixin,  FormView):
    template_name = 'product_manager/enquiry_form.html'
    form_class = enquiry_form
   
    success_url = '/'
    success_message="form submit successfuly"
    error_url="/"
    error_message="Wrong password or email"
    
    
    '''def form_valid(self, form ):
        
        
        
        
        form.save()
        return super().form_valid(form)
      '''
    def post(self,request,slug):
        
        model=product_add.objects.get(slug=slug)
        
        Sender_user=User.objects.get(username=self.request.user.username)
        Product_Name=model.Product_Name
        Product_user=model.user
        Mobile_No=request.POST['Mobile_No']
        Discription=request.POST['Discription']
        enquiry=product_enquiry(Product_Name=Product_Name,Mobile_No=Mobile_No,Discription=Discription,Product_user=Product_user,Sender_user=Sender_user)
        
        enquiry.save()
        messages.success(request,"you are successfuly send enquiry")
        #template_name="product_manager/after_product_click.html"
        #return render(request,template_name, )
        return redirect('/home/search')
          
    
                               
    
    
    
class add_products_view(SuccessMessageMixin,  View):
 
    form_class = product_add_form
    
    success_url = '/'
    success_message="form submit successfuly"
    
    
    '''def form_valid(self, form):
        
        
        #form.save()
        return super().form_valid(form)
        '''
    def get(self,request):
        form=product_add_form()
        template_name = 'product_manager/add_product.html'
        return render(request,template_name,{'form':form,'style_nav_item_8':context}  )
        
    def post(self,request):
        
        rpg=request.POST.get
        
        user=User.objects.get(username=self.request.user.username)
        Product_Name=rpg('Product_Name')
        Product_Img_=rpg('Product_Img')
        Product_Category=rpg("Product_Category")
        Company_Img_=rpg('Company_Img')
        Product_Price=rpg("Product_Price")
        Product_Discription=rpg('Product_Discription')
        Phone_No=rpg('Phone_No')
        Company_Logo_=rpg('Company_Logo')
        Gst_No=rpg('Gst_No')
        Company_Name=rpg('Company_Name')
        Registration_Number=rpg('Registration_Number')
        Founded_Year=rpg('Founded_Year')
        Workers_Company=rpg('Workers_Company')
        Company_Founder=rpg('Company_Founder')
        Company_Ceos=rpg('Company_Ceos')
        Youtube_Video_URL=rpg('Youtube_Video_URL')
        Address=rpg('Address')
        model=product_add(user=user, Product_Name=Product_Name,Product_Category=Product_Category,Product_Price=Product_Price,Product_Discription=Product_Discription, Phone_No= Phone_No,Gst_No=Gst_No,Company_Name=Company_Name,Registration_Number=Registration_Number,Founded_Year=Founded_Year,Workers_Company = Workers_Company,Company_Founder=Company_Founder,Company_Ceos=Company_Ceos, Youtube_Video_URL=Youtube_Video_URL,Address= Address,Company_Logo=Company_Logo_, Product_Img=Product_Img_,Company_Img=Company_Img_ )
        model.save()
        messages.success(request,"you are successfuly add product")
        form=product_add_form()
        template_name = 'product_manager/add_product.html'
        context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
        
        response=render(request,template_name,{'form':form,'style_nav_item_9':context}  )
        response.set_cookie( 'product_add_gig',model.slug )
           
        
        
        return response

        

    
class see_product_gig_view(View):
    def get(self,request):
        
        slug=request.COOKIES.get('product_add_gig')
        articles=product_add.objects.filter(slug=slug)
        #.values_list('slug','Product_Discription','Product_Price','Address','Views', )
        print(articles)
       
        response=render(request,'home/see_product_gig.html',{'product':articles})
        
        
        
        return response


class manager_account_form_view( View):
   
        
        
  
    def get (self,request):
        try:
            model=manager_account.objects.get(user=request.user)
            
            
            
            
            model=product_enquiry.objects.filter(Product_user=request.user)
           
            context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
            return render(request,"product_manager/orders_get.html" ,{"form":model,'style_nav_item_7':context} )
        
            
            
        except:
            context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
            return render(request, "product_manager/startup_manager_account_form.html",{"form": manager_account_form() ,'style_nav_item_7':context  } )
        #form.instance.user=self.request.user
        
        
        
       
        
    #user_email = user.email
    def post (self,request):
        user_name=User.objects.get(username=request.user.username)
        Name_= request.POST['Name']
        Email_=request.POST['Email']
        Phone_No_=request.POST['Phone_No']
        Gst_No_=request.POST['Gst_No']
        Company_Name_=request.POST['Company_Name']
        Registration_Number_=request.POST['Registration_Number']
        Founded_Year_=request.POST['Founded_Year']
        Workers_Company_=request.POST['Workers_Company']
        Company_Img_=request.POST['Company_Img']
        Company_Founder_=request.POST['Company_Founder']
        Company_Ceos_=request.POST['Company_Ceos']
        Address_=request.POST['Address']
        #slug_= request.POST['slug']
        Company_Logo_=request.POST['Company_Logo']
        Discription_=request.POST['Discription']
        manager_creat=manager_account(Name=Name_,Email=Email_,user=user_name,Phone_No=Phone_No_,Gst_No=Gst_No_,Company_Name=Company_Name_,Registration_Number=Registration_Number_,Founded_Year=Founded_Year_,Workers_Company=Workers_Company_,Company_Founder=Company_Founder_,Company_Ceos=Company_Ceos_ ,Address=Address_ ,Discription=Discription_,Company_Logo=Company_Logo_ , Company_Img=Company_Img_  )
        
        manager_creat.save()
        messages.success(request,"Successfuly Creat Manager Account")
        #model=product_enquiry.objects.filter(Product_user=model.user)
           
            
        return render(request,"product_manager/orders_get.html" ,{"form":product_add_form()} )
        
        
        
            
            
      
                
                
                
            
            
        
       
            
        
                              
    
    
                              
    

        
        
class manager_account_update_view(UpdateView):
    model = manager_account
    form_class=manager_account_form
    #pk_url_kwarg = 'pk'
    Slug_url_kwargs="slug"
    template_name = "product_manager/product_manager_account_update.html"
    success_url = '/'  
    def get_context_data(self, **kwargs):
        if 'context_key' not in kwargs:  # set value if not present
            kwargs['style_nav_item_17'] = context
        return super().get_context_data(**kwargs)
    
    
    
    
    
            
    
        
        
        
    
    
    
    
    
    
       
    
        
            
            
        
    
    
   

    
    
    
    
    
class My_Products_view(View):
    
    
    def get (self,request):
        model=product_add.objects.filter(user=request.user)
        context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
        return render(request,"product_manager/products_added.html" ,{"form":model,'style_nav_item_11':context} )
    
        
    
    
#product view and update template    

# blog/views.py




class  My_Products_View_Update(UpdateView):
    model = product_add
    form_class=product_add_form
    #pk_url_kwarg = 'pk'
    #slug_url_kwarg = 'slug'
    template_name = "product_manager/products_added_update.html"
    success_url = '/product_manager/My_products'    
    
    
class shiping_enquiry_form_view(SuccessMessageMixin, View):
    model=shiping_enquiry
    template_name = 'product_manager/shiping_enquiry.html'
    form_class = shiping_enquiry_form
    success_url = '/'
    success_message="form submit successfuly"
  
            
    '''def form_valid(self, form):
        
        form.save()
        return super().form_valid(form)
    '''
    def get(self,request):
        context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
        return render(request,'product_manager/shiping_enquiry.html',{'form':shiping_enquiry_form(),'style_nav_item_10':context})
        
        
    def post(self,request):
        #model=product_add.objects.get(slug=slug)
        user=User.objects.get(username=request.user.username)
        Product_Name=request.POST["Product_Name"]
        Comp_Name=request.POST['Comp_Name']
        Name=request.POST['Name']
        Email=request.POST['Email']
        Mobile_No=request.POST['Mobile_No']
        Discription=request.POST['Discription']
        Carry_Load=request.POST['Carry_Load']
        
       
       
        enquiry=shiping_enquiry(user=user,Product_Name=Product_Name,Name=Name,Email=Email,Mobile_No=Mobile_No,Discription=Discription,Comp_Name=Comp_Name,Carry_Load=Carry_Load)
        enquiry.save()
        messages.success(request,"Successfuly Creat Manager Account")
        context='box-shadow:0 4px 10px 0 rgba(32,125,225,0.6);'
        return render(request,'product_manager/shiping_enquiry.html',{'form':shiping_enquiry_form(),'style_nav_item_10':context})
        
        
       
     
        
    
    
    
    
class My_Products_View_Delete(View):    
    
    
    def get(self,request,slug):
        modl=product_add.objects.get(slug=slug).delete()
        model=product_add.objects.all()
        
        
        return render(request,"product_manager/products_added.html" ,{"form":model} )
     
    
    
        
        
    
  


    
    
class Graph_view(View):
    def get (self,request):
        
        return render(request,"product_manager/performance_graph.html" ,{'style_nav_item_13':context} )        
            
    
    
    
class Orders_Come_in_view (View):
    def get(self,request):
        model=product_enquiry.objects.filter(Sender_user=request.user)
        return render(request,"product_manager/orders_get.html" ,{"form":model,'style_nav_item_12':context} )

class Orders_Come_in_view_contact (View):
    def get(self,request):
        
        
        model=product_enquiry.objects.filter(Product_user=request.user)
        
        return render(request,"product_manager/orders_get.html" ,{"form":model} )
                  
    
    
class Orders_Come_in_view_delete (View):
    def get(self,request,slug):
        model=product_enquiry.objects.get(slug=slug).delete()
        model=product_enquiry.objects.all()
        return render(request,"product_manager/orders_get.html" ,{"form":model} )
    
    
    

    
    
    
              
