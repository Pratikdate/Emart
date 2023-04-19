from django import forms
from django.core import validators
from .models import requirement,product_enquiry,manager_account,product_add,shiping_enquiry,userprofile
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.models import User

class userprofile_form(forms.ModelForm):
    class Meta:
        model=userprofile
        exclude=('user',)
        #fields='__all__'
        widgets = {
            "User_Stetus": forms.TextInput(attrs={'class':'creat_profile',"placeholder":"Enter your Stetus",'name':'User_Stetus',}),
            "User_Bio": forms.TextInput(attrs={'class':'creat_profile',"placeholder":"Enter your biography",'name':"User_Bio" }),
            "User_Location": forms.TextInput(attrs={'class':'creat_profile',"placeholder":"Enter your Location",'name':'User_Location' }),
            "User_Company": forms.TextInput(attrs={'class':'creat_profile',"placeholder":"Enter your Company Name",'name':'User_Company' }),
            
            "User_Website": forms.TextInput(attrs={'class':'creat_profile',"placeholder":"Enter your website Name",'name':'User_Website'}),
            
            "User_Twitter": forms.TextInput(attrs={'class':'creat_profile',"placeholder":"Enter your Twitter Id",'name':'User_Twitter'}),
            
        }
    
    

class creat_account_form(forms.Form):
    Name=forms.CharField(max_length=100,widget = forms.TextInput(attrs={'class':'form-input',"placeholder":"Enter your First Name","name":"Name"}), )
    
    Last_Name=forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-input',"placeholder":"Enter your Last Name","name":"Last_Name"}),     )
    Email=forms.EmailField(max_length=100,   widget=   forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Email","name":"Email"}), )
    Password=forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class': 'form-input',"placeholder":"Enter Password","name":"Password"}),)
    class Meta :
        
        
        widgets = {
            
            "Name": forms.TextInput(attrs={'class':'form-input',"placeholder":"Enter your First Name","name":"Name"}),
            'Last_Name':forms.TextInput(attrs={'class':'form-input',"placeholder":"Enter your Last Name","name":"Last_Name"}),
                      "Email": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Email","name":"Email"}),
                      "Password": forms.PasswordInput(attrs={'class': 'form-input',"placeholder":"Enter Password","name":"Email"}),

        }
    
    
    


        


class requirement_form(forms.ModelForm):
    class Meta:
        model=requirement
        exclude=("Slug","Post_Date",'user',)
        widgets = {
            "Comp_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Company or startup Name"}),
            "Product_Category": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter Product Category Name"}),
             "Discription": forms.Textarea(attrs={'class':'discription',"placeholder":"Enter Discription about product","rows":5,"cols":20}   ),
             "Mobile_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your contact no"}),
             "Product_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter required product name"}),
             "Comp_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your company name"}),
            
             
        }
        

class enquiry_form(forms.ModelForm):
    class Meta:
        model=product_enquiry
        #fields=("Mobile_No","Discription",'Sender_user','Product_user')
        exclude=('Product_user','Sender_user','Product_Name')
        widgets = {
         
             "Mobile_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your contact no"}),
            
            
             "Discription": forms.Textarea(attrs={'class': 'discription',"placeholder":"Enter discription","rows":10,"cols":20}),
            
        }  
        
        
        
class shiping_enquiry_form(forms.ModelForm):
    class Meta:
        model=shiping_enquiry
        exclude=("user",)
        #fields='__all__'
        widgets = {
            "Product_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Product Name"}),
            
           "Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Name"}),
              "Carry_Load": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter load carry in Kg"}),
             "Email": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your email"}),
             "Mobile_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your contact no"}),
              "Comp_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Company Name"}),
            
            
             "Discription": forms.Textarea(attrs={'class': 'discription',"placeholder":"Enter discription","rows":5,"cols":20}),
            
        }          
        
        
        
        
class product_add_form(forms.ModelForm):
    class Meta:
        model=product_add
        exclude=("Post_Date",'Views','user',)
                 #("Product_Name","Product_Price","Product_Img","Product_Discription")
        widgets = {
           "Product_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Name",'name':'Product_Name'}),
            "Product_Category": forms.Select(attrs={'class': 'form-input',"placeholder":"",'name':'Product_Category'  }),
             "Product_Price": forms.TextInput(attrs={'class': 'form-input',"placeholder":"price(₹)/pice ", 'name':'Product_Price' }),
             
            
             "Product_Discription": forms.Textarea(attrs={'class': 'discription',"placeholder":"Enter discription","rows":5,"cols":20,'name':'Product_Discription' }),
              
             "Phone_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your contact no",'name':'Phone_No'   }),
              "Gst_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your gst no", 'name':'Gst_No' }),
             "Company_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your company name",'name':'Company_Name'  }),
             "Registration_Number": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your company registration no",'name':'Registration_Number'  }),
              "Founded_Year": forms.TextInput(attrs={'class': 'form-input',"placeholder":"DD/MM/YYY format",'name':'Founded_Year'  }),
             "Workers_Company": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter workers no", 'name':'Workers_Company' }),
           
              "Company_Founder": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter company founder name",'name':'Company_Founder'  }),
             "Company_Ceos": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter company ceos name",'name':'Company_Ceos'  }),
            "Youtube_Video_URL": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter product video url",'name':'Youtube_Video_URL'  }),
             "Address": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter company addres", 'name':'Address' }),
              
             
             
        }  
        
                
            

            
            
                
        
        
        
class manager_account_form(forms.ModelForm):
    class Meta:
        model=manager_account
        #fields="__all__"
        exclude=('user',)
        widgets = {
           "Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your Name"}),
         
           
             "Email": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your email"}),
             "Phone_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your contact no",   }),
              "Gst_No": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your gst no",   }),
             "Company_Name": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your company name",    }),
             "Registration_Number": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter your company registration Number" }),
              "Founded_Year": forms.TextInput(attrs={'class': 'form-input',"placeholder":"DD/MM/YYY format",  }),
             "Workers_Company": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter workers no", }),#'name':'Workers_Company' }),
           
              "Company_Founder": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter company founder name",}),#'name':'Company_Founder' }),
             "Company_Ceos": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter company ceos name", }),#'name':'Company_Ceos'   }),
             "Address": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter company addres",}),# 'name':'Address' }),
             "slug": forms.TextInput(attrs={'class': 'form-input',"placeholder":"Enter login Email",}) ,#'name':'slug' }),
              
             
             "Discription": forms.Textarea(attrs={'class': 'discription',"placeholder":"Enter discription","rows":5,"cols":35,}) # 'name':'Discription'}),
            
        }  
        
                
            

            