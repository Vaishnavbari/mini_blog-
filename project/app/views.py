from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.cache import cache
from django.shortcuts import get_object_or_404

# create session here

#404 page View

def errorpage404(request):
    return render(request,"app/404Errorpage.html")

# 500 page view

def errorpage500(request):
    return render(request,"app/500Errorpage.html")

#LOGIN page_view

def loginpageview(request):
    # cache.clear()
    try:
        if request.COOKIES.get("user_username") and request.COOKIES.get("user_password"):
            username=request.COOKIES.get("user_username")
            password=request.COOKIES.get("user_password")
            chk=request.COOKIES.get("user_chk")
            return render(request,"app/login.html",{"username":username,"password":password,"chk":chk})
        else:
            username=request.COOKIES.get("user\_username")
            password=request.COOKIES.get("user_password")
            return render(request,"app/login.html",{"username":username,"password":password})
    except:
       return redirect("error500") 

# RRGISTER USER
def registeruser(request):
        error={
                "firstname":[],
                "lastname":[],
                "username":[],
                "password":[],
                "email":[],
                "role":[]} 

        if request.method=="POST":
            role=request.POST['role']
            # validation for firstname
            firstname=request.POST['fname']
            
            if firstname=="":
                error["firstname"].append("First name not blank ")
               

            if not (len(firstname)>2 and len(firstname)<8):
                error["firstname"].append("Enter length 0f firstname beetween 2 and 8")
                
            
            # validation for lastname
            lastname=request.POST['lname']
            if lastname=="":
                error["lastname"].append("Lastname  not blank ")
               
            if not (len(lastname)>2 and len(lastname)<8):
                error["lastname"].append("Enter length 0f lastname beetween 2 and 8")
                
            
            # validation for username 
            username=request.POST['username']
            if username=="":
               error["username"].append("Username not blank ")
                
            if not (len(username)>2 and len(username)<15):
                error["username"].append("Enter length 0f username beetween  2 and 8")
                
            if not(username.isalnum()) :
                error["username"].append("username contain alphabets and numbers")
               
            # validation for email 
            email=request.POST['email']
            if email=="":
                error["email"].append("email not blank ")
                
            if not(email.endswith("@gmail.com")):
                error["email"].append( "Email ends with '@gmail.com'")
                
            # validation for password 
            password=request.POST['password']
    
            if password=="":
                error["password"].append("password not blank ")
                
            if not (len(password)>8):
                 error["password"].append("Enter length 0f password greater than 8")
            
            
             
            # If all data not valid return 
            if error["firstname"]!=[] or error["lastname"]!=[] or error["email"]!=[] or error["password"]!=[] or error["username"]!=[] :
                return render(request,"app/register.html",{"error":error,"data":{
                    "firstname": firstname,
                    "lastname": lastname,
                    "username": username,
                     "email": email,
                     "password":password
                }})
            
            if registration.objects.filter(username=username).exists():
               messages.info(request,f"user {username} {role} already exist")
               return render(request,"app/register.html")
            else:
                 user=registration.objects.create(
                 first_name=firstname,
                 last_name=lastname,
                 username=username,
                 email=email,
                 password=make_password(password),
                 role=role
            )
                 messages.success(request,f"User {username} {role} registered succesfully !!!")
                 return render(request,"app/register.html")
        else:
            return render(request,"app/register.html")
  
#HOME PAGE
@login_required
def home(request):
    # try:
        blog=cache.get("blog")
        print(blog)
        # for i in blog:
        #     print(i)
        # for cache 
        if blog is None:
            blogs = addblog.objects.all().order_by('-id')
            cache.set("blog",blogs,60*60*24)
            blog=cache.get("blog")
            return render(request,"app/home.html",{"blogs":blog})
        else:
            return render(request,"app/home.html",{"blogs":blog})
         
        # for signals
        # ip=request.session.get('ip',None)

        # # for session 
        # count=0
        # for i in  blogs:
                                                                                
        #     if i.user_id_id==request.user.id:
        #         count+=1
        #     request.session['count']=count
        
        
        # blog=cache.get("blog")
        
        # return render(request,"app/home.html",{"blogs":blog,"ip":ip,"count":request.session['count']})
    # except:
    #    return redirect("error500") 
     

# ABOUT PAGE
@login_required    
def about(request):
     try:
        # return render(request,"app/about.html",{"count":request.session['count']})
         return render(request,"app/about.html")
     except:
        return redirect("error500") 
     

# ADD BLOG PAGE VIEW URL 
@login_required
def add(request):
     try:
        #  blogs = addblog.objects.all().order_by('-id')
        #  count=0
        #  for i in  blogs:
        #         if i.user_id_id==request.user.id:
        #             count+=1
        #         request.session['count']=count   
        #  return render(request,"app/addblog.html",{"count":request.session['count']})
         return render(request,"app/addblog.html")

     except:
          return redirect("error500") 
    
     

# LOGIN VALIDATION  

def loginview(request):     
    
    try:
        error={
            "username":[],
            "password":[]
        }
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            # validation for username 
            if username=="":
                error["username"].append("username not blank")
            if password=="":
                error["password"].append("password not blank")
            if error["username"]!=[] or error["password"]!=[]:
                return render(request,"app/login.html",{"error":error,"data":{
                    "username": username,
                     "password":password
                }})
        
            user=authenticate(request,username=username,password=password)
         
            if user:
                login(request,user)
            
                if request.POST.get("chk"):
                    reponse=redirect("home")
                    reponse.set_cookie("user_username",user.username,max_age=60*60*24)
                    reponse.set_cookie("user_password",password,max_age=60*60*24)
                    reponse.set_cookie("user_chk","checked",max_age=60*60*24)
                    print("cookie set succesfully")
                    return reponse
                else:
                    reponse=redirect("home")
                    reponse.delete_cookie("user_username")
                    reponse.delete_cookie("user_password")
                    reponse.delete_cookie("user_chk")
                    return reponse
                
            else:
                 
                 messages.error(request,"invalid credentials")
                 return render(request,"app/login.html",{"data":{
                    "username": username,
                     "password":password
                }})

        else:
            return redirect("login")
    except:
        return redirect("error400") 

               
 # LOGOUT VIEW
@login_required        
def logout_view(request):
    logout(request)
    return redirect("login")

# BLOG POSTING URL 
@login_required
def blogs(request):
    try:
        if request.method=="POST": 
            title=request.POST['tittle']
            name=request.POST['name']
            location=request.POST['location']
            meassage=request.POST['meassage']  
            addblog.objects.create(
                    user_id= request.user,
                    title=title,
                    name=name,
                    location=location,
                    meassage=meassage ,  
            )
            cache.set("blog", addblog.objects.all().order_by('-id'),60*60*24)
            messages.success(request, "Blog Posted succesfully !!!")
            
            return redirect("add")
        else:
            return redirect("error404")
    except:
        return redirect("error500") 


# Update blog details 
@login_required
def updateview(request,pk):
    # blog=addblog.objects.get(id=pk)
    blog = get_object_or_404(addblog, id=pk)
    try:
        if request.method=="POST":
            if request.user.id == blog.user_id_id or request.user.role == "admin": 
                    blog.title=request.POST['tittle']
                    blog.name=request.POST['name']
                    blog.location=request.POST['location']
                    blog.meassage=request.POST['meassage'] 
                    blog.save()
                    cache.set("blog", addblog.objects.all().order_by('-id'),60*60*24) 
                    return redirect("/")
            else:
                return redirect("error404")
            
        else:
            if request.user.id == blog.user_id_id or request.user.role == "admin":
                return render(request,"app/edit_blog.html",{"blog":blog})
            else:
                return redirect("error404")
    except:
        return redirect("error400") 
              
         
# cancel update 
@login_required
def cancel(request):
     try:
         return redirect("/")  
     except:
         return redirect("error500")
     
# DELETE BLOG URL
@login_required 
def delete_blog(request,id):
    try:
        if request.method=="POST":
            blog=addblog.objects.get(pk=id) 
            if request.user.id == blog.user_id_id or request.user.role == "admin":
                blog.delete()
                cache.clear()
                cache.set("blog", addblog.objects.all().order_by('-id'),60*60*24) 
                messages.success(request,"Blog delete successfully !!!!")
                return redirect("home")
            else:
                return redirect("error404")
        else:
            return redirect("error404")
    except:
         return redirect("error400")
      



@receiver(user_logged_in,sender=registration)
def l_view(sender,request,user,**kwargs):
    ip=request.META.get('REMOTE_ADDR')
    request.session['ip']=ip
# user_logged_in.connect(login_view,sender=registration)