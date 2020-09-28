"""heal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from healapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static
urlpatterns = [
    path('admin', admin.site.urls),
    path('regis', views.regis, name='regis'),
    path('profilee', views.profilee, name='profilee'),
    path('source', views.source, name='source'),
    path('headtail', views.headtail, name='headtail'),
    path('fingerpage', views.fingerpage, name='fingerpage'),
    path('signinn', views.signinn, name='signinn'),
    path('pageallreg', views.pageallreg, name='pageallreg'),
    path('pagealllogin', views.pagealllogin, name='pagealllogin'),
    path('success', views.success, name='success'),
    path('formsb', views.formsb, name='formsb'),
    path('billingst', views.billingst, name='billingst'),
    
    path('myhistory', views.myhistory, name='myhistory'),
    path('docpro', views.docpro, name='docpro'),
    path('booke', views.booke, name='booke'),
    path('feed', views.feed, name='feed'),
    path('rejapp', views.rejapp, name='rejapp'),
    path('viewfeedback', views.viewfeedback, name='viewfeedback'),
    path('healthierfoods', views.healthierfoods, name='healthierfoods'),
    path('healthtips', views.healthtips, name='healthtips'),
    path('adminsign', views.adminsign, name='adminsign'),
    path('adminreg', views.adminreg, name='adminreg'),
    path('adminpage', views.adminpage, name='adminpage'),
    path('adminstaffsign', views.adminstaffsign, name='adminstaffsign'),
    path('adminstaffreg', views.adminstaffreg, name='adminstaffreg'),
    path('adminreal', views.adminreal, name='adminreal'),
    path('viewbook', views.viewbook, name='viewbook'),
    path('viewadbook', views.viewadbook, name='viewadbook'),
    path('viewdocbook', views.viewdocbook, name='viewdocbook'),
    path('doctorregis', views.doctorregis, name='doctorregis'),
    path('doctorpage', views.doctorpage, name='doctorpage'),
    path('docsignin', views.docsignin, name='docsignin'),
    path('subcat/',views.subcat,name="subcat"),
    path('depdoc/',views.depdoc,name="depdoc"),
    path('userhistory', views.userhistory, name='userhistory'),
    path('hospitalreg', views.hospitalreg, name='hospitalreg'),
    path('hossignin', views.hossignin, name='hossignin'),
    path('departmentcreate',views.departmentcreate,name="departmentcreate"),
    path('header_footer1', views.header_footer1, name='header_footer1'),
    path('addlocation', views.addlocation, name='addlocation'),
    path('hospitalpage', views.hospitalpage, name='hospitalpage'),
    path('billing', views.billing, name='billing'),
    path('mybill', views.mybill, name='mybill'),
    path('rejapp', views.rejapp, name='rejapp'),
    path('fillhis', views.fillhis, name='fillhis'),
    path('dfillhis', views.dfillhis, name='dfillhis'),
    path('docconhos', views.docconhos, name='docconhos'),
    path('hoscon', views.hoscon, name='hoscon'),
    path('hospitalbookingcon', views.hospitalbookingcon, name='hospitalbookingcon'),
    path('booktopatient', views.booktopatient, name='booktopatient'),
    path('finalbook', views.finalbook, name='finalbook'),
    path('staffreg', views.staffreg, name='staffreg'),
    path('staffsignin', views.staffsignin, name='staffsignin'),
    path('staffpage', views.staffpage, name='staffpage'),
    path('viewstaff', views.viewstaff, name='viewstaff'),
    path('viewadmstaff', views.viewadmstaff, name='viewadmstaff'),

    path('testhistory', views.testhistory, name='testhistory'),
    path('testupload', views.testupload, name='testupload'),
    path('dissym', views.dissym, name='dissym'),
    path('addsymptoms', views.addsymptoms, name='addsymptoms'),
    path('addsymptomsd', views.addsymptomsd, name='addsymptomsd'),
   
    path('payscan', views.payscan, name='payscan'),
   
    path('bankpage2', views.bankpage2, name='bankpage2'),
    path('billsta', views.billsta, name='billsta'),
    path('uploadbillpaidcopy', views.uploadbillpaidcopy, name='uploadbillpaidcopy'),
    
    path('useredit', views.useredit, name='useredit'),
    path('editfname', views.editfname, name='editfname'),
    path('editsname', views.editsname, name='editsname'),
    path('edituname', views.edituname, name='edituname'),
    path('editpass', views.editpass, name='editpass'),
    path('editaddressname', views.editaddressname, name='editaddressname'),
    path('editphnum', views.editphnum, name='editphnum'),
    path('editrelname', views.editrelname, name='editrelname'),
    path('editrelph', views.editrelph, name='editrelph'),
    path('newprofile', views.newprofile, name='newprofile'),
    path('adminedit', views.adminedit, name='adminedit'),
    path('editaname', views.editaname, name='editaname'),
    path('editapass', views.editapass, name='editapass'),
    path('admstaffedit', views.admstaffedit, name='admstaffedit'),
    path('editstnname', views.editstnname, name='editstnname'),
    path('editstpass', views.editstpass, name='editstpass'),
    path('newad', views.newad, name='newad'),
    path('doctoredit', views.doctoredit, name='doctoredit'),
    path('editdname', views.editdname, name='editdname'),
    path('editdpass', views.editdpass, name='editdpass'),
    path('editdhos', views.editdhos, name='editdhos'),
    path('editdphno', views.editdphno, name='editdphno'),
    path('newdoc', views.newdoc, name='newdoc'),
    path('hospitaledit', views.hospitaledit, name='hospitaledit'),
    path('editpro', views.editpro, name='editpro'),
    path('edithname', views.edithname, name='edithname'),
    path('edithpass', views.edithpass, name='edithpass'),
    path('newhos', views.newhos, name='newhos'),
    path('staffedit', views.staffedit, name='staffedit'),
    
    path('editsttna', views.editsttna, name='editsttna'),
    path('editsttp', views.editsttp, name='editsttp'),
    path('newstaff', views.newstaff, name='newstaff'),
    path('adminviewmedi', views.adminviewmedi, name='adminviewmedi'),
    path('tabtopat', views.tabtopat, name='tabtopat'),
    path('medibookdetails', views.medibookdetails, name='medibookdetails'),
    path('familyhea', views.familyhea, name='familyhea'),
    path('familyex', views.familyex, name='familyex'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('addmedicines', views.addmedicines, name='addmedicines'),
    path('addprice', views.addprice, name='addprice'),
    path('addmedicinesstaff', views.addmedicinesstaff, name='addmedicinesstaff'),
    path('addpricestaff', views.addpricestaff, name='addpricestaff'),
    path('selectmed', views.selectmed, name='selectmed'),
    path('subprice/', views.subprice, name='subprice'),
    path('cart', views.cart, name='cart'),
    path('patient_relativesview', views.patient_relativesview, name='patient_relativesview'),
    

    

   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

