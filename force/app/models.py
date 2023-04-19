from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.utils.timezone import now
# Create your models here.
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from django.conf import settings
import uuid 
from django.core.validators import MinLengthValidator    

#user=User.objects.get(name,useremail)

class userprofile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,related_name="userprofile",on_delete=models.PROTECT,null=True,blank=True)
    User_Stetus=models.CharField(max_length=30, null=True,blank=True,default='')
    User_Bio=models.CharField(max_length=100, null=True,blank=True ,default='')
    Profile_Img=models.ImageField(upload_to="product_img/" ,null=True,blank=True,default='/storage/emulated/0/Download/Fill (6).png')
    
    
    User_Location=models.CharField(max_length=100,  null=True,blank=True,default='' )
    User_Company=models.CharField(max_length=100,null=True,blank=True ,default='')
    User_Website=models.CharField(max_length=100, null=True,blank=True , default='')
    
    User_Twitter=models.CharField(max_length=100, null=True,blank=True ,default='')
    
   
 

   
                 

class requirement(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True,blank=True)
    
    Product_Name=models.CharField(max_length=200, )
    Post_Date=models.DateTimeField(null=True,blank=True,default=now)
            
          
    Product_Category=models.CharField(max_length=200,)

    
    
    #slug=models.EmailField(max_length=200,)
    
    slug=AutoSlugField(populate_from=('user','Post_Date'))#unique=True,blank=True,default=None ,null=True)
   
    
   
    
    Comp_Name=models.CharField(max_length=200)
    
                           
    
                              
    Mobile_No=models.IntegerField( ) 
    Discription=models.TextField(max_length=2000)
            
         
    
    def __str__(self):
        return self.Product_Name

    

    
    
    
    
    
class product_enquiry(models.Model):
    Sender_user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='sender_user',null=True,blank=True)
    Product_user=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='product_enquiry',on_delete=models.PROTECT,null=True,blank=True)
    Mobile_No=models.IntegerField()
    Post_Date=models.DateTimeField(null=True,blank=True,default=now)
    
    Product_Name=models.CharField(max_length=300)
    
    slug=AutoSlugField(populate_from=['Product_user','Mobile_No'])#unique=True,null=True,default=None )
    
   
    Discription=models.TextField(max_length=2000)
     
    
            
       
    
   
    
    
    
class shiping_enquiry(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True,blank=True)
    
    slug=AutoSlugField(populate_from=['Product_Name','Email'],)
    Post_Date=models.DateTimeField(null=True,blank=True,default=now)
    Name=models.CharField(max_length=200)
    Email=models.EmailField(max_length=200)
   
    Product_Name=models.CharField(max_length=200)
    Carry_Load=models.IntegerField()
    Comp_Name=models.CharField(max_length=200)
    Discription=models.TextField(max_length=1000,)
    Mobile_No=models.IntegerField()  
    
    
    
class product_add(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,null=True,blank=True)
    
    Post_Date=models.DateTimeField(null=True,blank=True,default=now)
    
   
    Product_Name=models.CharField(max_length=400,)
    
    
    
    
    Choices=[
        ('1','Agriculture goods and searvices '),
        ('2',' Industrial searvices'),
        ('3','Industerial Plant,Machinery,Equipment'),
       ( '4','Consumer Electronics and House Hold Equipment'),
        ('5','Packaging Material suplies and machinery'),
        ('6','Industrial and Enginearing Products sparce '),
        ('7', 'Building Construct Material, Equipment,Civil Enginearing and Real Estate'),
        ('8','Apperal Clothings and Germent '),
        ('9','Vagitable,Fruits, Grain,Dairy Products and other Grosery Products'),
        ('10','Medical Equipment'),
        ('11','Cemical Dyes and Allied Products'),
        ('12','Macanical Component or Parts '),
        
        ('13','Scientific,Measuring, Laboratory Products'),
        ('14','Furniture,Furniture Suplies,Furniture Hardware'),
        ('15','Ayurvedic and Herbal Products  '),
        ('16','Sequrity Devices,Safety System and Sequrity Services'),
        ('17',' Sports Goods,Games,Toys ,Accessories'),
        ('18','Telecom Products Equipement and Supplies '),
        ('19',' Stationary and Paper Products '),
        ('18',' Bags,Belts ,Wallets and Accesories '),
        ('20','Stone Marble and Granite Suplies  '),
        ('21','Trade Event Organiser,Event Planner  '),
        ('22','Fertilisers,seeds,plant, Agro Machines'),
        ('23','Polatry and Animal Husbendry  '),
        ('24','Automobile Spare Parts and Accessories'),
        ('25','Computer Softwar,IT Support and Solutions '),
        ('26','Tool,mashine Tool '),
    ]
    Product_Category=models.CharField(max_length=500, choices=Choices  ,)
    Product_Price=models.CharField(max_length=500)
    Product_Img=models.ImageField(upload_to="product_img/" ,null=True,blank=True,default='/storage/emulated/0/Download/Fill (6).png')
    
    
    Phone_No=models.IntegerField(null=True,blank=True)
    Views=models.IntegerField(default=0)
    
    Gst_No=models.CharField(max_length=500 ,null=True,blank=True)
    Company_Name=models.CharField(max_length=100, null=True,blank=True)
    Registration_Number=models.CharField(max_length=500,null=True,blank=True)
    
    Founded_Year=models.CharField(max_length=100,null=True,blank=True)
    Workers_Company=models.IntegerField(null=True,blank=True )
    Company_Img=models.ImageField( upload_to="image/",null=True,blank=True ,default='/storage/emulated/0/Download/Fill (6).png')
    Company_Founder=models.CharField(max_length=30 ,null=True,blank=True)
    Company_Ceos=models.CharField(max_length=300, null=True,blank=True)
    Address=models.CharField(max_length=40,)
   
    Company_Logo=models.ImageField(  upload_to="image/" ,null=True,blank=True,default='/storage/emulated/0/Download/Fill (6).png')
    
    
    
   # Slug_Company=models.SlugField()
    slug=AutoSlugField(populate_from=['Product_Name','Company_Name','Gst_No'],unique=True,null=True,default=None)
    Youtube_Video_URL=models.URLField(max_length=4000)
    
    Product_Discription=models.TextField(max_length=1000, null=True )
   
    

            
class manager_account(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name="manager_account",null=True,blank=True)
    Name=models.CharField(max_length=100,null=True,blank=True)
    
    #Adhar_Number=models.IntegerField(   null=True,blank=True)
   
    
   
   
    Email=models.EmailField(max_length=100,null=True,blank=True)                      
    Phone_No=models.IntegerField(null=True,blank=True )
    Gst_No=models.CharField(max_length=500 ,null=True,blank=True)
    Company_Name=models.CharField(max_length=100,null=True,blank=True)
    Registration_Number=models.CharField(max_length=500,null=True,blank=True)
    
    Founded_Year=models.CharField(max_length=100,null=True,blank=True)
    Workers_Company=models.IntegerField( )
    Company_Img=models.ImageField( upload_to="image/",null=True,blank=True)
    Company_Founder=models.CharField(max_length=30 ,null=True,blank=True ,default=None )
    Company_Ceos=models.CharField(max_length=300,null=True,blank=True,default=None)
    Address=models.CharField(max_length=40, null=True,blank=True, default=None )
   
    
    
    slug=AutoSlugField(populate_from=['user','Email'],unique=True,null=True,default=None)
   
    Company_Logo=models.ImageField(  upload_to="image/"  , null=True,blank=True, default=None)
    
    
    Discription=models.TextField(  null=True,blank=True,default=None, help_text="give product name with short use and type of product"   )
    
    

    
    
class user_explore_list(models.Model):
    Email=models.EmailField(max_length=100,null=True,blank=True)
    
    slug=models.SlugField()
    Post_Date=models.DateTimeField(null=True,blank=True,default=now)
    
    

    
import datetime  
import hashlib
import user_agents




class UserVisit(models.Model):
    """
    Record of a user visiting the site on a given day.
    This is used for tracking and reporting - knowing the volume of visitors
    to the site, and being able to report on someone's interaction with the site.
    We record minimal info required to identify user sessions, plus changes in
    IP and device. This is useful in identifying suspicious activity (multiple
    logins from different locations).
    Also helpful in identifying support issues (as getting useful browser data
    out of users can be very difficult over live chat).
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="user_visits", on_delete=models.CASCADE
    )
    timestamp = models.DateTimeField(
        help_text="The time at which the first visit of the day was recorded",
        default= now,
    )
    session_key = models.CharField(help_text="Django session identifier", max_length=40)
    remote_addr = models.CharField(
        help_text=(
            "Client IP address (from X-Forwarded-For HTTP header, "
            "or REMOTE_ADDR request property)"
        ),
        max_length=100,
        blank=True,
    )
    ua_string = models.TextField(
        "User agent (raw)", help_text="Client User-Agent HTTP header", blank=True,
    )
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    hash = models.CharField(
        max_length=32,
        help_text="MD5 hash generated from request properties",
        
    )
    created_at = models.DateTimeField(
        help_text="The time at which the database record was created (!=timestamp)",
        auto_now_add=True,
    )
    
    #objects = UserVisitManager()

    class Meta:
        get_latest_by = "timestamp"

    def __str__(self) -> str:
        return f"{self.user} visited the site on {self.timestamp}"

    def __repr__(self) -> str:
        return f"<UserVisit id={self.id} user_id={self.user_id} date='{self.date}'>"

    ''''def save(self, *args: Any, **kwargs: Any) -> None:
        """Set hash property and save object."""
        self.hash = self.md5().hexdigest()
        super().save(*args, **kwargs)'''

    @property
    def user_agent(self) -> user_agents.parsers.UserAgent:
        """Return UserAgent object from the raw user_agent string."""
        return user_agents.parsers.parse(self.ua_string)

    @property
    def date(self) -> datetime.date:
        """Extract the date of the visit from the timestamp."""
        return self.datetime()
    

    

    
    
    
    
    

    

    
    
    
    