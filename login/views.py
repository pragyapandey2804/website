from django.shortcuts import render
import mysql.connector as sql
ti=''
pwd=''
# Create your views here.
def loginaction(request):
    global ti,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="admin123",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="tenement_id":
                ti=value
            if key=="password":
                pwd=value
        
        c="select * from users where tenement_id='{}' and password='{}' ".format(ti,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')

