
from django.shortcuts import render
import mysql.connector as sql
ti=''
n=''
em=''
pn=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="admin123",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="tenement_id":
                ti=value
            if key=="name":
                n=value
            if key=="email":
                em=value
            if key=="phone_number":
                pn=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}')".format(ti,n,em,pn,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')

