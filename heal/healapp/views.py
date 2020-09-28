from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import pymysql
import datetime
import os
from datetime import time
import time
from datetime import datetime 
from django.http import HttpResponseRedirect 
import simplejson as json
from pathlib import Path
import subprocess
con=pymysql.connect("localhost","root","","healonyou")
cur=con.cursor()

def profilee(request):
   
   USERNAME=request.session["uname"]
   
   n="select * from patient_reg where USERNAME='"+str(USERNAME)+"'"
   cur.execute(n)
   data=cur.fetchall()  

   return render(request,"profilee.html",{"data":data})
def source(request):
    return render(request,"source.html")
def regis(request):
   

    msg=""
    if 'sub' in request.POST:
        print("hiiiiiiiiiiiiiiiiiii")
        FIRSTNAME=request.POST.get("fname")
        
        SECONDNAME=request.POST.get("sname")
        
        USERNAME=request.POST.get("uname")
        PASSWORD=request.POST.get("password")
        CONFIRMPASSWORD=request.POST.get("cpasword")
        ADDRESS =request.POST.get("add")
        COUNTRY=request.POST.get("coun")
        CONTACTNO =request.POST.get("phno")
        EMAILID =request.POST.get("email")
        DOB =request.POST.get("db")
        GENDER=request.POST.get("gender")
        BLOODGROUP=request.POST.get("bloodgrp")  
        RELNAME=request.POST.get("rn") 
        RELPH=request.POST.get("rp") 

        if(PASSWORD==CONFIRMPASSWORD):

           d="insert into patient_reg(FIRSTNAME,SECONDNAME,USERNAME,PASSWORD,ADDRESS,COUNTRY,CONTACTNO,EMAILID,DOB,GENDER,BLOODGROUP,RELATIVESNAME,RELATIVESPHNO) values('"+FIRSTNAME+"','"+SECONDNAME+"','"+USERNAME+"','"+PASSWORD+"','"+ADDRESS+"','"+COUNTRY+"','"+CONTACTNO+"','"+EMAILID+"','"+DOB+"','"+GENDER+"','"+BLOODGROUP+"','"+RELNAME+"','"+RELPH+"')"
           cur.execute(d)
           con.commit()
           msg="REGISTRATION SUCCESSFULL"
          

        else:
         
           

           msg="PASSWORD MISMATCH FOUND"
   
           
    return render(request,"regis.html",{"data":msg})

def fingerpage(request):
     USERNAME=request.session["uname"]
     b="select * from patient_reg where USERNAME='"+str(USERNAME)+"' "
     cur.execute(b)
     data=cur.fetchall()
     if 'FINGER_ACCESS' in request.POST:
        print("hiiiiiiiiiiiiiiiiiii")
        os.startfile("C:\\Program Files (x86)\\BioEnable\\BioDesk\\BioDesk.exe")
        os.startfile("C:\\deek\\heal\\healapp\\static\\bin\\Debug\\ConsoleApplication1.exe")
     
     return render(request,"fingerpage.html",{"data":data})
     
def signinn(request):

   msg=""
   request.session["uname"]=""
   if(request.POST):
      USERNAME=request.POST.get("uname")
      request.session["uname"] = USERNAME
      PASSWORD=request.POST.get("password")
      e="select count(*) from patient_reg where USERNAME='"+str(USERNAME)+"' and PASSWORD='"+str(PASSWORD)+"'"
      cur.execute(e)
      data=cur.fetchall()
      
      if(data[0][0]==1):
         msg=""
         return HttpResponseRedirect("profilee")
      else:
         msg="MISTAKE FOUND"

   return render(request,"signinn.html",{"data":msg})

def headtail(request):
    return render(request,"headtail.html")

def pageallreg(request):
    return render(request,"pageallreg.html")
def pagealllogin(request):
    return render(request,"pagealllogin.html")

def hossignin(request):

   msg=""
   request.session["hname"]=""
   if(request.POST):
      HOSPITALNAME=request.POST.get("hname")
      request.session["hname"] = HOSPITALNAME
      PASSWORD=request.POST.get("hospword")
      e="select count(*) from hospital where HOSPITAL='"+str(HOSPITALNAME)+"' and PASSWORD='"+str(PASSWORD)+"'"
      cur.execute(e)
      data=cur.fetchall()
      
      if(data[0][0]==1):
         msg=""
         return HttpResponseRedirect("hospitalpage")
      else:
         msg="MISTAKE FOUND"

   return render(request,"hossignin.html",{"data":msg})

def header_footer1(request):
    return render(request,"header_footer1.html")

def success(request):
    return render(request,"success.html")
def formsb(request):
    return render(request,"formsb.html")


def myhistory(request):
    USERNAME=request.session["uname"]
    b="select * from fill_his where USERNAME='"+str(USERNAME)+"'"
    cur.execute(b)
    data=cur.fetchall()
    v="select * from testdatas where USERNAME='"+str(USERNAME)+"'"
    cur.execute(v)
    da=cur.fetchall()
    return render(request,"myhistory.html",{"data":data,"da":da})
def userhistory(request):
    DOCTORNAME=request.session["dname"]
    
    v="select * from fill_his where DOCTORNAME='"+str(DOCTORNAME)+"'"
    cur.execute(v)
    data=cur.fetchall()
    r="select * from testdatas where DOCTORNAME='"+str(DOCTORNAME)+"'"
    cur.execute(r)
    da=cur.fetchall()
    return render(request,"userhistory.html",{"data":data,"da":da})


    
def docpro(request):
   data=""
   dat=""
   if(request.session['uname']):
    
    cur.execute("select * from location")
    data=cur.fetchall()   
    if(request.POST):
      USERID=request.POST.get("uid")  
      USERNAME=request.POST.get("uname")
      category_name=request.POST.get("addcategory") 
      
      subcat_name=request.POST.get("hname")
      subsubcat_name=request.POST.get("depdoc")
      
        
     
      
      
      cur.execute("insert into docpro values('"+USERID +"','"+USERNAME +"','"+category_name +"','"+str(subcat_name)+"','"+str(subsubcat_name)+"')")
      dat=cur.fetchall()   
      con.commit()
      return HttpResponseRedirect("booke")

      
   return render(request,"docpro.html",{"cat":data,"lio":dat})
 
    

  
def booke(request):

    
    if(request.session["uname"]==""):
        return HttpResponseRedirect("signinn")
    
    USERNAME=request.session["uname"]
    
    print(USERNAME)
    s="select * from docpro where USERNAME='"+USERNAME+"'"
    cur.execute(s)
    data=cur.fetchall()
    if(request.POST):
        DOCTORNAME=request.POST.get("depdoc")
        DOCTOR=request.POST.get("doc")
        HOSPITALNAME=request.POST.get("hosname")
        
        LOCATION =request.POST.get("loccategory")
        
        username =request.POST.get("livename")
        USERID =request.POST.get("uid")
        DOV =request.POST.get("db")
        ATTEND=request.POST.get("experience")
        CONDITION=request.POST.get("msg")
        
        TIME =request.POST.get("time")
        STATUS = "Pending "
        f="insert into book values('"+str(DOCTORNAME)+"','"+str(DOCTOR)+"','"+str(HOSPITALNAME)+"','"+str(LOCATION)+"','"+str(username)+"','"+str(USERID)+"','"+str(DOV)+"','"+str(ATTEND)+"','"+str(CONDITION)+"','"+str(TIME)+"','"+str(STATUS)+"')"
        cur.execute(f)
        con.commit()
        d="delete  from docpro where USERNAME='"+str(USERNAME)+"'"
        cur.execute(d)
        con.commit() 
        return HttpResponseRedirect("viewbook")
    return render(request,"booke.html",{"data":data})
    print(data)
def feed(request):
    msg=""
    if(request.POST):

       USERNAME=request.POST.get("uname")
       EMAIL=request.POST.get("email")
       RATING=request.POST.get("experience")
       DELRATING=request.POST.get("experi")
       COMMENTS=request.POST.get("msg")
       f="insert into feedback values('"+str(USERNAME)+"','"+str(EMAIL)+"','"+str(RATING)+"','"+str(DELRATING)+"','"+str(COMMENTS)+"')"
       cur.execute(f)
       con.commit()
       msg="Thank you for your feedback!"
    return render(request,"feed.html",{"data":msg})

def viewfeedback(request):
  
  b="select * from feedback "
  cur.execute(b)
  da=cur.fetchall()
  return render(request,"viewfeedback.html",{"da":da})
     

def fillhis(request):

    if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"
       filetype=request.POST.get("file_type")
       USERID=request.POST.get("uid")
       USERNAME=request.POST.get("uname")
       DOCTORNAME=request.POST.get("doc")
       HOSPITALNAME=request.POST.get("hos")
       FILETYPE=request.POST.get("file_type")
       BROWSE=request.POST.get("bro")
       MESSAGE=request.POST.get("msge")
       s="insert into fill_his values('"+str(USERID)+"','"+str(USERNAME)+"','"+str(DOCTORNAME)+"','"+str(HOSPITALNAME)+"','"+str(FILETYPE)+"','"+str(filename)+"','"+str(MESSAGE)+"')"
       cur.execute(s)
       con.commit()    
       return HttpResponseRedirect("myhistory")
    return render(request,"fillhis.html")

def dfillhis(request):

    if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"
       filetype=request.POST.get("file_type")

       USERID=request.POST.get("uid")
       USERNAME=request.POST.get("uname")
       DOCTORNAME=request.POST.get("doc")
       HOSPITALNAME=request.POST.get("hos")
       FILETYPE=request.POST.get("file_type")
       BROWSE=request.POST.get("bro")
       MESSAGE=request.POST.get("msge")
       s="insert into fill_his values('"+str(USERID)+"','"+str(USERNAME)+"','"+str(DOCTORNAME)+"','"+str(HOSPITALNAME)+"','"+str(FILETYPE)+"','"+str(filename)+"','"+str(MESSAGE)+"')"
       cur.execute(s)
       con.commit()    
       
    return render(request,"dfillhis.html")


def adminviewmedi(request):
    
    b="select * from cart "
    cur.execute(b)
    data=cur.fetchall()
    return render(request,"adminviewmedi.html",{"data":data})   

def tabtopat(request):
     
    
     ADMINNAME=request.session["aname"]
     s="select USERNAME,sum(PRICE) from cart  group by USERNAME "
     cur.execute(s)
     data=cur.fetchall()
     if(request.POST):
       USERNAME=request.POST.get("uname")
       BOOKID=request.POST.get("book")
       DELIVERYON=request.POST.get("del")
       
       MEDICINES=request.POST.get("delm")
       TOTAL=request.POST.get("total")
       
       PAYMODE=request.POST.get("pay")
       STATUS="ARRIVING"
       s="insert into meditopat values('"+str(USERNAME)+"','"+str(BOOKID)+"','"+str(DELIVERYON)+"','"+str(MEDICINES)+"','"+str(TOTAL)+"','"+str(PAYMODE)+"','"+str(STATUS)+"')"
       cur.execute(s)
       con.commit()    
       
     return render(request,"tabtopat.html",{"data":data}) 

def medibookdetails(request):
    USERNAME=request.session["uname"]
    b="select * from meditopat where USERNAME='"+str(USERNAME)+"'"
    cur.execute(b)
    data=cur.fetchall()
    d="delete  from cart where USERNAME='"+str(USERNAME)+"'"
    cur.execute(d)
    con.commit() 
    return render(request,"medibookdetails.html",{"data":data})

def updatemedibook(request):
    if(request.POST):
     USERNAME=request.POST.get("uname")
     BOOKID=request.POST.get("book")
     DELIVERYON=request.POST.get("del")
     STATUS=request.POST.get("staa")
     f="insert into cache values('"+str(USERNAME) +"','"+str(BOOKID) +"','"+str(DELIVERYON) +"','"+str(STATUS) +"')"
     cur.execute(f)
     con.commit()
     w="update meditopat set STATUS= 'ARRIVED'"
     print(w)
     cur.execute(w)
     con.commit()
     data=cur.fetchall()
     return HttpResponseRedirect("medibookdetails",{"data":data})
    return render(request,"updatemedibook.html")   

def healthierfoods(request):
    return render(request,"healthierfoods.html")    
def adminsign(request):
   msg=""
   request.session["aname"] =""
   if(request.POST):
      ADMINNAME=request.POST.get("aname")
      
      request.session["aname"] = ADMINNAME
      PASSWORD=request.POST.get("password")
      q="select count(*) from adminreg where ADMINNAME='"+str(ADMINNAME)+"' and PASSWORD='"+str(PASSWORD)+"'" 
      cur.execute(q)
      data=cur.fetchall()
      
      if(data[0][0]==1):
         msg=""
         return HttpResponseRedirect("adminreal")
      else:
         msg="MISTAKE FOUND"

   return render(request,"adminsign.html",{"data":msg})
def adminreg(request):
    msg=""
    ms=""
    if(request.POST):
      
      ADMINNAME=request.POST.get("aname")
      PASSWORD=request.POST.get("password")
      CONFIRMPASSWORD=request.POST.get("cpasword")
      EMAILID=request.POST.get("email")
      UNIQUEIDNO=request.POST.get("no")
      if(PASSWORD==CONFIRMPASSWORD):


         if(UNIQUEIDNO=="4444"):
          a="insert into adminreg(ADMINNAME,PASSWORD,EMAILID,UNIQUEIDNO) values('"+str(ADMINNAME)+"','"+str(PASSWORD)+"','"+str(EMAILID)+"','"+str(UNIQUEIDNO)+"')"
          cur.execute(a)
          con.commit()    
          msg="successful"
          
          return HttpResponseRedirect("adminsign")
         else:
          ms="wrong unique id registered"
      else:
         msg="password mismatch found"

    return render(request,"adminreg.html",{"data":msg,"da":ms})    

def adminstaffsign(request):
   msg=""
   request.session["stname"] =""
   if(request.POST):
      STAFFNAME=request.POST.get("stname")
      
      request.session["stname"] = STAFFNAME
      PASSWORD=request.POST.get("password")
      q="select count(*) from streg where STAFFNAME='"+str(STAFFNAME)+"' and PASSWORD='"+str(PASSWORD)+"'" 
      cur.execute(q)
      data=cur.fetchall()
      
      if(data[0][0]==1):
         msg=""
         return HttpResponseRedirect("adminpage")
      else:
         msg="MISTAKE FOUND"

   return render(request,"adminstaffsign.html",{"data":msg})
def adminstaffreg(request):
    msg=""
    ms=""
    if(request.POST):
      
      STAFFNAME=request.POST.get("stname")
      PASSWORD=request.POST.get("password")
      CONFIRMPASSWORD=request.POST.get("cpasword")
      PLACE=request.POST.get("pla")
      EMAILID=request.POST.get("email")
      
      if(PASSWORD==CONFIRMPASSWORD):


         
          a="insert into streg(STAFFNAME,PASSWORD,PLACE,EMAILID) values('"+str(STAFFNAME)+"','"+str(PASSWORD)+"','"+str(PLACE)+"','"+str(EMAILID)+"')"
          cur.execute(a)
          con.commit()    
          msg="successful"
          
          return HttpResponseRedirect("adminstaffsign")
         
      else:
         msg="password mismatch found"

    return render(request,"adminstaffreg.html",{"data":msg,"da":ms})    
   
def adminpage(request):
   STAFFNAME=request.session["stname"]
   
   n="select * from streg where STAFFNAME='"+str(STAFFNAME)+"'"
   cur.execute(n)
   data=cur.fetchall()  
   return render(request,"adminpage.html",{"data":data}) 

def adminreal(request):
   ADMINNAME=request.session["aname"]
   
   n="select * from adminreg where ADMINNAME='"+str(ADMINNAME)+"'"
   cur.execute(n)
   data=cur.fetchall()  
   return render(request,"adminreal.html",{"data":data}) 

def viewadmstaff(request):
    
    b="select * from streg "
    cur.execute(b)
    data=cur.fetchall()
    return render(request,"viewadmstaff.html",{"data":data})  

def viewbook(request):
  
  if(request.session["uname"]==""):
        return HttpResponseRedirect("signinn")
    
  USERNAME=request.session["uname"]
    
  u="select * from book where STATUS = 'Pending' and USERNAME= '"+str(USERNAME)+ "'"
  cur.execute(u)
  data=cur.fetchall()
  
  return render(request,"viewbook.html",{"data":data}) 
def viewdocbook(request):
  
  DOCTORNAME=request.session["dname"]
  v="select * from book where DOCTOR='"+str(DOCTORNAME)+"'"

  cur.execute(v)
  data=cur.fetchall()

  return render(request,"viewdocbook.html",{"data":data})

def viewadbook(request):
  
  
    
  u="select * from book where STATUS = 'Pending' "
  cur.execute(u)
  data=cur.fetchall()
  
  return render(request,"viewadbook.html",{"data":data}) 
  
  

def rejapp(request):
   HOSPITALNAME=request.session["hname"]
    
   u="select * from docconhos where  HOSPITALNAME= '"+str(HOSPITALNAME)+ "'"
   cur.execute(u)
   data=cur.fetchall()
   d="delete  from docconhos where HOSPITALNAME='"+str(HOSPITALNAME)+"'"
   cur.execute(d)
   con.commit() 
   if(request.POST):
      

       PRO=request.POST.get("pro")
      
       HOSPITALNAME=request.POST.get("hname")
       DOCTORNAME=request.POST.get("dname")
       DEPARTMENT=request.POST.get("depname")
       USERNAME=request.POST.get("uname")
       BOOKINGSTATUS=request.POST.get("bname")
       DOV=request.POST.get("db")
       TIME=request.POST.get("time")
       TOKEN=request.POST.get("tok")
       BOOKDETAILS=request.POST.get("msge")
       s="insert into rejapp values('"+str(PRO)+"','"+str(HOSPITALNAME)+"','"+str(DOCTORNAME)+"','"+str(DEPARTMENT)+"','"+str(USERNAME)+"','"+str(BOOKINGSTATUS)+"','"+str(DOV)+"','"+str(TIME)+"','"+str(TOKEN)+"','"+str(BOOKDETAILS)+"')"
       cur.execute(s)
       con.commit()    
      
    
   return render(request,"rejapp.html",{"data":data})  
def doctorregis(request):
    msg=""
    HOSPITALNAME=""
   
     
    cur.execute("select * from hospital")
    data=cur.fetchall()
    if(request.POST):
        DOCTORNAME=request.POST.get("dname")
        
        DEPARTMENT=request.POST.get("cname")
        HOSPITALNAME=request.POST.get("hname")
        
        PASSWORD=request.POST.get("dpword")
        CONFIRMPASSWORD=request.POST.get("cdpword")
        
        CONTACTNO =request.POST.get("phno")
        EMAILID =request.POST.get("email")
        
        GENDER=request.POST.get("gender")
        
        
        if(PASSWORD==CONFIRMPASSWORD):

           o="insert into doctor_reg(DOCTORNAME,DEPARTMENT,HOSPITALNAME,PASSWORD,CONTACTNO,EMAILID,GENDER) values('"+str(DOCTORNAME)+"','"+str(DEPARTMENT)+"','"+str(HOSPITALNAME)+"','"+str(PASSWORD)+"','"+str(CONTACTNO)+"','"+str(EMAILID)+"','"+str(GENDER)+"')"
           cur.execute(o)
           con.commit()
           msg="REGISTRATION SUCCESSFULL"
          

        else:
         
           

           msg="PASSWORD MISMATCH FOUND"
           
    return render(request,"doctorregis.html",{"data":msg,"cat":HOSPITALNAME})  

def docsignin(request):

   msg=""
   request.session["dname"]=""
   if(request.POST):
      DOCTORNAME=request.POST.get("dname")
      print(DOCTORNAME)
      request.session["dname"] = DOCTORNAME
      PASSWORD=request.POST.get("dpword")
      e="select count(*) from doctor_reg where DOCTORNAME='"+str(DOCTORNAME)+"' and PASSWORD='"+str(PASSWORD)+"'"
      cur.execute(e)
      data=cur.fetchall()
      
      if(data[0][0]==1):
         msg=""
         return HttpResponseRedirect("doctorpage")
      else:
         msg="MISTAKE FOUND"
       

   return render(request,"docsignin.html",{"data":msg})

def doctorpage(request):
     DOC=request.session["dname"]
   
     n="select * from doctor_reg where DOCTORNAME='"+str(DOC)+"'"
     cur.execute(n)
     data=cur.fetchall()  
     return render(request,"doctorpage.html",{"data":data}) 
def hospitalreg(request):
 msg=""
 LOCATION=""
 
    
 cur.execute("select * from location")
 data=cur.fetchall()
 if(request.POST):
        PRO=request.POST.get("pro")
        
        
        
        HOSPITALNAME=request.POST.get("hname")
        LOCATION=request.POST.get("addcategory")
        PASSWORD=request.POST.get("hospword")
        CONFIRMPASSWORD=request.POST.get("cdpword")
        
        CONTACTNO =request.POST.get("phno")
        EMAILID =request.POST.get("email")
        
        
        
        if(PASSWORD==CONFIRMPASSWORD):

           h="insert into hospital(pro,hospital,location,password,contactno,email) values('"+str(PRO)+"','"+str(HOSPITALNAME)+"','"+str(LOCATION)+"','"+str(PASSWORD)+"','"+str(CONTACTNO)+"','"+str(EMAILID)+"')"
           cur.execute(h)
           con.commit()
           data=cur.fetchall()
           msg="REGISTRATION SUCCESSFULL"
           

        else:
         
           

           msg="PASSWORD MISMATCH FOUND"
 return render(request,"hospitalreg.html",{"data":msg ,"cat":LOCATION})       


def subcat(request):
  sublist=[]
  catid=request.GET.get("dataid")
  
  cur.execute("select * from hospital where location='"+str(catid)+"'")
  
  data2=cur.fetchall()
  for d in data2:
    sublist.append(d[1])
  return HttpResponse(json.dumps(sublist),content_type="application/json")





def departmentcreate(request):
  if(request.POST):
     category_name=request.POST.get("hname")
     depdoc=request.POST.get("depdoc")
    
     cur.execute("insert into department(HOSPITALNAME,DEPDOC) values('"+str(category_name) +"','"+str(depdoc) +"')")
     con.commit()
 
     
  return render(request,"departmentcreate.html")

def depdoc(request):
  sublist=[]
  catid=request.GET.get("deid") 
  print(catid)
  cur.execute("select * from department where HOSPITALNAME='"+str(catid)+"'")
  data2=cur.fetchall()
  for d in data2:
    sublist.append(d[2])
  return HttpResponse(json.dumps(sublist),content_type="application/json")

def addlocation(request):
 
  if(request.POST):
     category_name=request.POST.get("addcategory")
     cur.execute("insert into location(loc) values('"+str(category_name) +"')")
     con.commit()
 
     
  return render(request,"addlocation.html")


def hospitalpage(request):
   HOSNAME=request.session["hname"]
   
   n="select * from hospital where hospital='"+str(HOSNAME)+"'"
   cur.execute(n)
   data=cur.fetchall() 
   return render(request,"hospitalpage.html",{"data":data}) 


def billing(request):
  if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"
       filetype=request.POST.get("file_type")
       billingid=request.POST.get("bid")
       billing=request.POST.get("tname")
       STAFF=request.POST.get("addstaffs")
       USERNAME=request.POST.get("uname")
       doctor=request.POST.get("doc")
       filetype=request.POST.get("file_type")
       browse=request.POST.get("bro")
       AMOUNT=request.POST.get("amount")
       STATUS=request.POST.get("sta")
      
       s="insert into bill values('"+str(billingid)+"','"+str(billing)+"','"+str(STAFF)+"','"+str(USERNAME)+"','"+str(doctor)+"','"+str(filetype)+"','"+str(filename)+"','"+str(AMOUNT)+"','"+str(STATUS)+"')"
       cur.execute(s)
       con.commit()    
       
    
  
  return render(request,"billing.html")

def billingst(request):
  if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"
       filetype=request.POST.get("file_type")
       billingid=request.POST.get("bid")
       billing=request.POST.get("tname")
       STAFF=request.POST.get("addstaffs")
       USERNAME=request.POST.get("uname")
       doctor=request.POST.get("doc")
       filetype=request.POST.get("file_type")
       browse=request.POST.get("bro")
       AMOUNT=request.POST.get("amount")
       STATUS=request.POST.get("sta")
      
       s="insert into bill values('"+str(billingid)+"','"+str(billing)+"','"+str(STAFF)+"','"+str(USERNAME)+"','"+str(doctor)+"','"+str(filetype)+"','"+str(filename)+"','"+str(AMOUNT)+"','"+str(STATUS)+"')"
       cur.execute(s)
       con.commit()    
       
    
  
  return render(request,"billingst.html")


def mybill(request):
  USERNAME=request.session["uname"]
  b="select * from bill where USERNAME='"+str(USERNAME)+"'"
  cur.execute(b)
  data=cur.fetchall()
  return render(request,"mybill.html",{"data":data})
def docconhos(request):
  DOCTORNAME=request.session["dname"]
  v="select * from book where DOCTOR='"+str(DOCTORNAME)+"'"

  cur.execute(v)
  data=cur.fetchall()
  if(request.POST):

       
       DOCTORNAME=request.POST.get("dname")
       HOSPITALNAME=request.POST.get("hname")
       DEPARTMENTNAME=request.POST.get("depname")
       USERNAME=request.POST.get("livename")
       DOV=request.POST.get("db")
       CONDITION=request.POST.get("con")
       TIME=request.POST.get("time")
       MESSAGE=request.POST.get("msge")
       s="insert into docconhos values('"+str(DOCTORNAME)+"','"+str(HOSPITALNAME)+"','"+str(DEPARTMENTNAME)+"','"+str(USERNAME)+"','"+str(DOV)+"','"+str(CONDITION)+"','"+str(TIME)+"','"+str(MESSAGE)+"')"
       cur.execute(s)
       con.commit()    
       
    
  return render(request,"docconhos.html",{"data":data})  

def hoscon(request):
  if(request.session["hname"]==""):
        return HttpResponseRedirect("hossignin")
    
  HOSPITALNAME=request.session["hname"]
    
  u="select * from docconhos where  HOSPITALNAME= '"+str(HOSPITALNAME)+ "'"
  cur.execute(u)
  data=cur.fetchall()
 
  
  return render(request,"hoscon.html",{"data":data})

def hospitalbookingcon(request): 
   DOCTORNAME=request.session["dname"]
   b="select * from rejapp where DOCTORNAME='"+str(DOCTORNAME)+"'"
   cur.execute(b)
   data=cur.fetchall()  

   return render(request,"hospitalbookingcon.html",{"data":data})

def booktopatient(request):

   DOCTORNAME=request.session["dname"]
   b="select * from rejapp where DOCTORNAME='"+str(DOCTORNAME)+"'"
   cur.execute(b)
   data=cur.fetchall()  
   if(request.POST):
       

       
      
       HOSPITALNAME=request.POST.get("hname")
       DOCTORNAME=request.POST.get("dname")
       DEPARTMENT=request.POST.get("depname")
       USERNAME=request.POST.get("uname")
       BOOKINGSTATUS=request.POST.get("bname")
       
       DATE=request.POST.get("db")
       TIME=request.POST.get("time")
       TOKEN=request.POST.get("tok")
       BOOKDETAILS=request.POST.get("msge")
       s="insert into bookshowtopat values('"+str(HOSPITALNAME)+"','"+str(DOCTORNAME)+"','"+str(DEPARTMENT)+"','"+str(USERNAME)+"','"+str(BOOKINGSTATUS)+"','"+str(DATE)+"','"+str(TIME)+"','"+str(TOKEN)+"','"+str(BOOKDETAILS)+"')"
       cur.execute(s)
       con.commit()  
       d="delete  from rejapp where DOCTORNAME='"+str(DOCTORNAME)+"'"
       cur.execute(d)
       con.commit()   
      
    
   return render(request,"booktopatient.html",{"data":data})

def finalbook(request):
    USERNAME=request.session["uname"]
    b="select * from bookshowtopat where USERNAME='"+str(USERNAME)+"'"
    cur.execute(b)
    data=cur.fetchall()
    return render(request,"finalbook.html",{"data":data})
 
def staffreg(request): 
   if(request.POST):  
     STAFF=request.POST.get("addstaffs")
     HOSPITALNAME=request.POST.get("addhos")
     PASSWORD=request.POST.get("password")
     f="insert into addstaffs values('"+str(STAFF) +"','"+str(HOSPITALNAME) +"','"+str(PASSWORD) +"')"
     cur.execute(f)
     con.commit()
   return render(request,"staffreg.html")

def viewstaff(request):
    HOSPITALNAME=request.session["hname"]
    b="select * from addstaffs where HOSPITALNAME='"+str(HOSPITALNAME)+"'"
    cur.execute(b)
    data=cur.fetchall()
    return render(request,"viewstaff.html",{"data":data})
def staffpage(request):
   STAFFNAME=request.session["addstaffs"]
   
   n="select * from addstaffs where STAFF='"+str(STAFFNAME)+"'"
   cur.execute(n)
   data=cur.fetchall() 
   return render(request,"staffpage.html",{"data":data}) 
    
    

def staffsignin(request):

   msg=""
   request.session["addstaffs"]=""
   if(request.POST):
      STAFF=request.POST.get("addstaffs")
      request.session["addstaffs"] = STAFF
      PASSWORD=request.POST.get("password")
      e="select count(*) from addstaffs where STAFF='"+str(STAFF)+"' and PASSWORD='"+str(PASSWORD)+"'"
      cur.execute(e)
      data=cur.fetchall()
      
      if(data[0][0]==1):
         msg=""
         return HttpResponseRedirect("staffpage")
      else:
         msg="MISTAKE FOUND"

   return render(request,"staffsignin.html",{"data":msg})

def testupload(request):
   if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"
       filetype=request.POST.get("file_type")

       USERNAME=request.POST.get("uname")
       DOCTORNAME=request.POST.get("doc")
       HOSPITALNAME=request.POST.get("hos")
       TYPEOFTEST=request.POST.get("test")
       FILETYPE=request.POST.get("file_type")
       BROWSE=request.POST.get("bro")
       MESSAGE=request.POST.get("msge")
       s="insert into testdatas values('"+str(USERNAME)+"','"+str(DOCTORNAME)+"','"+str(HOSPITALNAME)+"','"+str(TYPEOFTEST)+"','"+str(FILETYPE)+"','"+str(filename)+"','"+str(MESSAGE)+"')"
       cur.execute(s)
       con.commit()    
       return HttpResponseRedirect("testhistory")
    
   return render(request,"testupload.html")

def testhistory(request):
    USERNAME=request.session["uname"]
    
    v="select * from testdatas where USERNAME='"+str(USERNAME)+"'"
    cur.execute(v)
    data=cur.fetchall()
    return render(request,"testhistory.html",{"data":data})

def dissym(request):
    data=""
    msg=""
    if(request.POST):  
     USERNAME=request.POST.get("uname")
     SYMPTOM=request.POST.get("sim")
     u="select * from addsymptoms where  SYMPTOMS= '"+str(SYMPTOM)+ "'"
    
     cur.execute(u)
     data=cur.fetchall()
     
     if(data):
      msg="Symptoms Match,See our 'SEARCH DOCTORS PAGE' to consult"
     else:
      msg="Symptoms not Match"
    return render(request,"dissym.html",{"data":data,"msg":msg})



def payscan(request):
   return render(request,"payscan.html")

def billsta(request):
    STAFF=request.session["addstaffs"]
    b="select * from billpaystatus where STAFF='"+str(STAFF)+"'" 
    cur.execute(b)
    data=cur.fetchall()
    return render(request,"billsta.html",{"data":data})
def uploadbillpaidcopy(request):
    if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"
      
       billingid=request.POST.get("bid")
       billing=request.POST.get("tname")
       STAFF=request.POST.get("addstaffs")
       USERNAME=request.POST.get("uname")
       HOSPITAL=request.POST.get("hos")
       
       browse=request.POST.get("bro")
      
      
       s="insert into billpaystatus values('"+str(billingid)+"','"+str(billing)+"','"+str(STAFF)+"','"+str(USERNAME)+"','"+str(HOSPITAL)+"','"+str(filename)+"')"
       cur.execute(s)
       con.commit()    
    return render(request,"uploadbillpaidcopy.html")





def bankpage2(request):
    
    
   USERNAME=request.POST.get("uname")
   STATUS=request.POST.get("staa")
   f="insert into status values('"+str(USERNAME) +"','"+str(STATUS) +"')"
   cur.execute(f)
   con.commit()
   w="update bill set STATUS= 'paid'"
   print(w)
   cur.execute(w)
   con.commit()
   data=cur.fetchall()

   

  
   return render(request,"bankpage2.html")
   
def useredit(request):
  

    msg=""
    if(request.session["uname"]==""):
        return HttpResponseRedirect("signinn")
    
    USERNAME=request.session["uname"]
    
    
    s="select * from patient_reg where USERNAME='"+str(USERNAME)+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"useredit.html",{"data":data})
    print(data)

def editfname(request):
    data=""
    finame=request.GET.get("finame")
    uid=request.GET.get("uid") 
    FIRSTNAME=request.POST.get("nfiname")
    if(request.POST):

        w="update patient_reg set FIRSTNAME='"+str(FIRSTNAME)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newprofile")

    return render(request,"editfname.html",{"finame":finame,"data":data})

def editsname(request):
    data=""
    sename=request.GET.get("sename")
    uid=request.GET.get("uid")
    SECONDNAME=request.POST.get("nsename")
    if(request.POST):

        w="update patient_reg set SECONDNAME='"+str(SECONDNAME)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newprofile")

    return render(request,"editsname.html",{"sename":sename,"data":data})

def edituname(request):
    data=""
    uname=request.GET.get("uname")
    uid=request.GET.get("uid")
    USERNAME=request.POST.get("nuname")
    if(request.POST):

        w="update patient_reg set USERNAME='"+str(USERNAME)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("signinn")

    return render(request,"edituname.html",{"uname":uname,"data":data})

def editpass(request):
    data=""
    password=request.GET.get("password")
    uid=request.GET.get("uid")
    PASSWORD=request.POST.get("npassword")
    if(request.POST):

        w="update patient_reg set PASSWORD='"+str(PASSWORD)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newprofile")

    return render(request,"editpass.html",{"password":password,"data":data})

def editaddressname(request):
    data=""
    add=request.GET.get("add")
    uid=request.GET.get("uid") 
    ADDRESS=request.POST.get("nadd")
    if(request.POST):

        w="update patient_reg set ADDRESS='"+str(ADDRESS)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newprofile")

    return render(request,"editaddressname.html",{"add":add,"data":data})

def editphnum(request):
    data=""
    phno=request.GET.get("phno")
    uid=request.GET.get("uid")
    CONTACTNO=request.POST.get("nphno")
    if(request.POST):

        w="update patient_reg set CONTACTNO='"+str(CONTACTNO)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newprofile")

    return render(request,"editphnum.html",{"phno":phno,"data":data})

def editrelname(request):
    data=""
    rn=request.GET.get("rn")
    uid=request.GET.get("uid")
    RELATIVESNAME=request.POST.get("nrn")
    if(request.POST):

        w="update patient_reg set RELATIVESNAME='"+str(RELATIVESNAME)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("signinn")

    return render(request,"editrelname.html",{"rn":rn,"data":data})

def editrelph(request):
    data=""
    rp=request.GET.get("rp")
    uid=request.GET.get("uid")
    RELATIVESPHNO=request.POST.get("nrp")
    if(request.POST):

        w="update patient_reg set RELATIVESPHNO='"+str(RELATIVESPHNO)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newprofile")

    return render(request,"editrelph.html",{"rp":rp,"data":data})
   
def newprofile(request):

    msg=""
    if(request.session["uname"]==""):
        return HttpResponseRedirect("signinn")
    
    USERNAME=request.session["uname"]
  
   
    s="select * from patient_reg where USERNAME='"+USERNAME+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"newprofile.html",{"data":data})
       

def adminedit(request):
  

       data=""
    

    
       ADMINNAME=request.session["aname"]
     
    
       s="select * from adminreg where ADMINNAME='"+str(ADMINNAME)+"' "
       cur.execute(s)
       data=cur.fetchall()
       return render(request,"adminedit.html",{"data":data})
      



def editaname(request):
    data=""
    aname=request.GET.get("aname")
    uid=request.GET.get("uid")
    ADMINNAME=request.POST.get("naname")
    if(request.POST):

        w="update adminreg set ADMINNAME='"+str(ADMINNAME)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("adminsign")

    return render(request,"editaname.html",{"aname":aname,"data":data})
       
def editapass(request):
    data=""
    password=request.GET.get("password")
    uid=request.GET.get("uid")
    PASSWORD=request.POST.get("npassword")
    if(request.POST):

        w="update adminreg set PASSWORD='"+str(PASSWORD)+"' where uid='"+str(uid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("adminsign")

    return render(request,"editapass.html",{"password":password,"data":data})      

def admstaffedit(request):
  

       data=""
    

    
       STAFFNAME=request.session["stname"]
     
    
       s="select * from streg where STAFFNAME='"+str(STAFFNAME)+"' "
       cur.execute(s)
       data=cur.fetchall()
       return render(request,"admstaffedit.html",{"data":data})
      



def editstnname(request):
    data=""
    stname=request.GET.get("stname")
    stid=request.GET.get("stid")
    STAFFNAME=request.POST.get("nstname")
    if(request.POST):

        w="update streg set STAFFNAME='"+str(STAFFNAME)+"' where stid='"+str(stid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("adminstaffsign")

    return render(request,"editstnname.html",{"stname":stname,"data":data})
       
def editstpass(request):
    data=""
    password=request.GET.get("password")
    stid=request.GET.get("stid")
    PASSWORD=request.POST.get("npassword")
    if(request.POST):

        w="update adminreg set PASSWORD='"+str(PASSWORD)+"' where stid='"+str(stid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("adminstaffsign")

    return render(request,"editstpass.html",{"password":password,"data":data})      



def newad(request):

    data=""
    if(request.POST):
     USERNAME=request.session["aname"]
  
   
     s="select * from adminreg where ADMINNAME='"+USERNAME+"' "
     cur.execute(s)
     data=cur.fetchall()
    return render(request,"newad.html",{"data":data})



def doctoredit(request):
  

    msg=""
    
    
    DOCTORNAME=request.session["dname"]
    
    
    s="select * from doctor_reg where DOCTORNAME='"+str(DOCTORNAME)+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"doctoredit.html",{"data":data})

def editdname(request):
    data=""
    dname=request.GET.get("dname")
    did=request.GET.get("did")
    DOCTORNAME=request.POST.get("ndname")
    if(request.POST):

        w="update doctor_reg set DOCTORNAME='"+str(DOCTORNAME)+"' where did='"+str(did)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("docsignin")

    return render(request,"editdname.html",{"dname":dname,"data":data})

def editdpass(request):
    data=""
    password=request.GET.get("password")
    did=request.GET.get("did")
    PASSWORD=request.POST.get("npassword")
    if(request.POST):

        w="update doctor_reg set PASSWORD='"+str(PASSWORD)+"' where did='"+str(did)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("docsignin")

    return render(request,"editdpass.html",{"password":password,"data":data})

def editdhos(request):
    data=""
    hname=request.GET.get("hname")
    did=request.GET.get("did")
    HOSPITALNAME=request.POST.get("ndname")
    if(request.POST):

        w="update doctor_reg set HOSPITALNAME='"+str(HOSPITALNAME)+"' where did='"+str(did)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("docsignin")

    return render(request,"editdhos.html",{"hname":hname,"data":data})

def editdphno(request):
    data=""
    phno=request.GET.get("phno")
    did=request.GET.get("did")
    CONTACTNO=request.POST.get("nphno")
    if(request.POST):

        w="update doctor_reg set CONTACTNO='"+str(CONTACTNO)+"' where did='"+str(did)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("docsignin")

    return render(request,"editdphno.html",{"phno":phno,"data":data})


def newdoc(request):

    msg=""
    if(request.session["dname"]==""):
        return HttpResponseRedirect("docsignin")
    
    DOCTORNAME=request.session["dname"]
  
   
    s="select * from doctor_reg where DOCTORNAME='"+DOCTORNAME+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"newdoc.html",{"data":data})

def hospitaledit(request):
  

    msg=""
    
    
    hospital=request.session["hname"]
    
    
    s="select * from hospital where hospital='"+str(hospital)+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"hospitaledit.html",{"data":data})

def editpro(request):
    data=""
    pro=request.GET.get("pro")
    hid=request.GET.get("hid")
    PRO=request.POST.get("npro")
    if(request.POST):

        w="update hospital set pro='"+str(PRO)+"' where hid='"+str(hid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("newhos")

    return render(request,"editpro.html",{"pro":pro,"data":data})

def edithname(request):
    data=""
    hname=request.GET.get("hname")
    hid=request.GET.get("hid")
    hospital=request.POST.get("nhname")
    if(request.POST):

        w="update hospital set hospital='"+str(hospital)+"' where hid='"+str(hid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("hossignin")

    return render(request,"edithname.html",{"hname":hname,"data":data})

def edithpass(request):
    data=""
    password=request.GET.get("password")
    hid=request.GET.get("hid")
    Password=request.POST.get("npassword")
    if(request.POST):

        w="update hospital set password='"+str(Password)+"' where hid='"+str(hid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("hossignin")

    return render(request,"edithpass.html",{"password":password,"data":data})

def newhos(request):

    msg=""
    if(request.session["hname"]==""):
        return HttpResponseRedirect("hossignin")
    
    HOSPITALNAME=request.session["hname"]
  
   
    s="select * from hospital where hospital='"+HOSPITALNAME+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"newhos.html",{"data":data})

def staffedit(request):
  

    msg=""
    
    
    ADDST=request.session["addstaffs"]
    
    
    s="select * from addstaffs where STAFF='"+str(ADDST)+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"staffedit.html",{"data":data})



def editsttna(request):
    data=""
    addstaffs=request.GET.get("addstaffs")
    sid=request.GET.get("sid")
    naddstaffs=request.POST.get("naddstaffs")
    if(request.POST):

        w="update addstaffs set STAFF='"+str(naddstaffs)+"' where sid='"+str(sid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("staffsignin")

    return render(request,"editsttna.html",{"addstaffs":addstaffs,"data":data})

def editsttp(request):
    data=""
    password=request.GET.get("password")
    sid=request.GET.get("sid")
    Password=request.POST.get("npassword")
    if(request.POST):

        w="update addstaffs set password='"+str(Password)+"' where sid='"+str(sid)+"'"
        print(w)
        cur.execute(w)
        con.commit()
        data=cur.fetchall()

        return HttpResponseRedirect("staffsignin")

    return render(request,"editsttp.html",{"password":password,"data":data})

def newstaff(request):

    msg=""
    if(request.session["addstaffs"]==""):
        return HttpResponseRedirect("staffsignin")
    
    STAFFNAME=request.session["addstaffs"]
  
   
    s="select * from addstaffs where STAFF='"+STAFFNAME+"' "
    cur.execute(s)
    data=cur.fetchall()
    return render(request,"newstaff.html",{"data":data})

def addsymptoms(request):
    if(request.POST):
     DISEASE=request.POST.get("dis")
     SYMPTOMS=request.POST.get("sym")
     
     f="insert into addsymptoms(DISEASE,SYMPTOMS) values('"+str(DISEASE) +"','"+str(SYMPTOMS) +"')"
     cur.execute(f)
     con.commit()
     
    return render(request,"addsymptoms.html")



def addsymptomsd(request):
    if(request.POST):
     DISEASE=request.POST.get("dis")
     SYMPTOMS=request.POST.get("sym")
     
     f="insert into addsymptoms(DISEASE,SYMPTOMS) values('"+str(DISEASE) +"','"+str(SYMPTOMS) +"')"
     cur.execute(f)
     con.commit()
     
    return render(request,"addsymptomsd.html")


def healthtips(request):
    return render(request,"healthtips.html")

def familyex(request):
    return render(request,"familyex.html")
def familyhea(request):
    return render(request,"familyhea.html")
def lifestyle(request):
    return render(request,"lifestyle.html")


def selectmed(request):
     data=""
     dat=""
     msg=""
     if(request.session['uname']):
    
      cur.execute("select * from addmedi")
      data=cur.fetchall()   
      if(request.POST):
       filename=request.POST.get("bro")
       if(request.FILES.get('bro')):
            myfile=request.FILES['bro']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            fileurl=fs.url(filename)
       else:
            fileurl="/static/de.jpg"   
       USERNAME=request.POST.get("uname") 
       category_name=request.POST.get("addcategory") 
      
       subcat_name=request.POST.get("hname")
       BROWSE=request.POST.get("bro")
      
       ADDRESS=request.POST.get("addd")
       PINCODE=request.POST.get("pin") 
      
       COUNTRY=request.POST.get("coun")
       CONTACT=request.POST.get("ph")
        
     
      
      
       cur.execute("insert into cart(USERNAME,MEDICINES,PRICE,BROWSE,ADDRESS,PINCODE,COUNTRY,CONTACT) values('"+str(USERNAME)+"','"+category_name +"','"+str(subcat_name)+"','"+str(filename)+"','"+str(ADDRESS)+"','"+str(PINCODE)+"','"+str(COUNTRY)+"','"+str(CONTACT)+"')")
       dat=cur.fetchall()   
       con.commit()
       msg="CART SUCCESSFULLY ADDED"
       return HttpResponseRedirect("cart")

      
  
     return render(request,"selectmed.html",{"cat":data,"lio":dat,"msg":msg})
def addmedicines(request):
    if(request.POST):
     category_name=request.POST.get("addcategory")
     cur.execute("insert into addmedi(MEDICINES) values('"+str(category_name) +"')")
     con.commit()
    return render(request,"addmedicines.html")
def addprice(request):
     if(request.POST):
      PRICE=request.POST.get("hname")
      MEDICINES=request.POST.get("addcategory")
      cur.execute("insert into addprice(PRICE,MEDICINES) values('"+str(PRICE) +"','"+str(MEDICINES) +"')")
      con.commit()
    
     return render(request,"addprice.html")

def addmedicinesstaff(request):
    if(request.POST):
     category_name=request.POST.get("addcategory")
     cur.execute("insert into addmedi(MEDICINES) values('"+str(category_name) +"')")
     con.commit()
    return render(request,"addmedicinesstaff.html")
def addpricestaff(request):
     if(request.POST):
      PRICE=request.POST.get("hname")
      MEDICINES=request.POST.get("addcategory")
      cur.execute("insert into addprice(PRICE,MEDICINES) values('"+str(PRICE) +"','"+str(MEDICINES) +"')")
      con.commit()
    
     return render(request,"addpricestaff.html")

def subprice(request):
  sublist=[]
  catid=request.GET.get("mid")
  
  cur.execute("select * from addprice where MEDICINES='"+str(catid)+"'")
  
  data2=cur.fetchall()
  for d in data2:
    sublist.append(d[1])
  return HttpResponse(json.dumps(sublist),content_type="application/json")

def cart(request):
    USERNAME=request.session["uname"]
    
    
    s="select USERNAME,group_concat(MEDICINES SEPARATOR ', ') ,sum(PRICE) from cart where USERNAME='"+str(USERNAME)+"' group by USERNAME "
    cur.execute(s)
    data=cur.fetchall()
    msg="successfully ordered"

    return render(request,"cart.html",{"data":data,"msg":msg})


def patient_relativesview(request):
    print("hiiiiiiiiiiiiiiiii")
    os.startfile("C:\\Program Files (x86)\\BioEnable\\BioDesk\\BioDesk.exe")
    if(request.POST):
        
        print("helloooooooooooooooooo")
        t=0
        my_file = Path("C:\\t.txt")
        # if my_file.is_file():
        #     os.remove("C:\\t.txt")
        while t==0:
            time.sleep(15)
            
            os.startfile("C:\\Debug\\ConsoleApplication1.exe")
            
            t=1
    

    # my_file = Path("C:\\t.txt")
    # if my_file.is_file():

    #     file1 = open("C:\\t.txt","r+")  
    #     data=file1.read()
    #     ss="select * from relative where g_id='"+data+"'"   
    #     print(ss)  
    #     c.execute(ss)
    #     d=c.fetchall()
    #     print(d)
    #     return render(request,"patient_relatives.html",{"data":d}) 
    # else:
        a=0
        while a==0:
            time.sleep(15)
            file1 = open("C:\\t.txt","r+")  
            data1=file1.read()
            
            
            ss="select * from patient_reg where uid='"+str(int(data1))+"'"   
            print(ss)  
            cur.execute(ss)
            data=cur.fetchall()
            print(data)
            print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
            s="select * from fill_his where uid='"+str(int(data1))+"'"   
            print(s)  
            cur.execute(s)
            da=cur.fetchall()
            print(da)
            a=1
            return render(request,"patient_relativesview.html",{"data":data,"da":da}) 


    return render(request,"patient_relativesview.html")

