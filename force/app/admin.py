from django.contrib import admin
from app.models import requirement,product_enquiry,manager_account,product_add,shiping_enquiry,UserVisit,userprofile,user_explore_list
from simple_history.admin import SimpleHistoryAdmin



from simple_history import register
from django.contrib.auth.models import User



    


# Register your models here.
admin.site.register(UserVisit)

@admin.register(userprofile)
class userprofile_admin(admin.ModelAdmin):
    list_display=['id',"User_Company","user"]
    
    
    
@admin.register( user_explore_list )
class userprofile_admin(admin.ModelAdmin):
    list_display=('slug','Email','Post_Date')

@admin.register(requirement )
class requirementa_admin(admin.ModelAdmin):
    list_display=["id","Product_Name","Product_Category","Comp_Name","Mobile_No","Post_Date"]
 
    
@admin.register(product_enquiry )
class enquiry_admin(admin.ModelAdmin):
    list_display=["id","Product_Name","Mobile_No"]
    
    
    
@admin.register(shiping_enquiry)
class shiping_enquiry_admin(admin.ModelAdmin):
    list_display=["id","Comp_Name","Mobile_No"]
        
    
@admin.register(manager_account)
class manager_account_admin(admin.ModelAdmin):
    list_display=["id",'user',"Company_Name","Company_Ceos","Email","Gst_No","Phone_No","Address",'user']  
    
@admin.register(product_add)
class product_add_admin(admin.ModelAdmin):
    list_display=["id","Product_Name","Product_Price",'slug',"Post_Date",'Views']      
    