from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+200+200")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    city=textfield.get()
    
    geolocator= Nominatim(user_agent="geoapi")
    location= geolocator.geocode(city)
    obj= TimezoneFinder()
    
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    
    #weather
    url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"

    querystring = {"lat":location.latitude,"lon":location.longitude,"timezone":"auto","language":"en","units":"auto"}

    headers = {
	    "X-RapidAPI-Key": "0adfec26a1msh228ed72d7b5fd9ep107c77jsn04f45e6c7431",
	    "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
    }

    json_data = requests.get(url, headers=headers, params=querystring).json()

    
    #current
    temp=json_data['current']['temperature']
    humidity=json_data['current']['humidity']
    pressure=json_data['current']['pressure']
    wind=json_data['current']['wind']['speed']
    description = json_data['current']['summary']
    
    t.config(text=(temp,"°C"))
    h.config(text=(humidity,"%"))
    p.config(text=(pressure,"hpa"))
    w.config(text=(wind,"m/s"))
    d.config(text=description)
    
#hours
local_time=datetime.now()
time=local_time.strftime("%H")
time=int(time)
print(type(time))
    
## icon
image_icon=PhotoImage(file="logo/icon.png")
root.iconphoto(False,image_icon)

round_box=PhotoImage(file="logo/images(1).png")
Label(root,image=round_box,bg="white").place(x=30,y=110)

#label
label1=Label(root,text="Temperature : ",font=('Helvetica',11),fg="white",bg="black")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity : ",font=('Helvetica',11),fg="white",bg="black")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure : ",font=('Helvetica',11),fg="white",bg="black")
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed : ",font=('Helvetica',11),fg="white",bg="black")
label4.place(x=50,y=180)

label5=Label(root,text="Description : ",font=('Helvetica',11),fg="white",bg="black")
label5.place(x=50,y=200)

##search box
search_img=PhotoImage(file="logo/img2.png")
myimage=Label(image=search_img,bg="#00FFFF")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="logo/weather.png")
weatherimage=Label(root,image=weat_image,bg="black")
weatherimage.place(x=280,y=127)

textfield=tk.Entry(root,justify="center",width=13,font=("poppins",25,"bold"),bg="white",border=2,fg="black")
textfield.place(x=360,y=130)
textfield.focus()

search_icon=PhotoImage(file="logo/srch1.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="white",command=getWeather)
myimage_icon.place(x=615,y=125)

##bottom box
frame=Frame(root,width=900,height=180,bg="#FFF8DC")
frame.pack(side=BOTTOM)

#images in the bottom

if time>=19 and time<=5 :
    erly_mrng=PhotoImage(file="icons/7-5.png")
    erlymrng=Label(image=erly_mrng,bg="black",height=150,width=150)
    erlymrng.place(x=700,y=300)
    if time<24 and time>19:
        label6=Label(root,text="Good Night",font=('Helvetica',90),fg="LightGreen")
        label6.place(x=50,y=300)
    else:
        label6=Label(root,text="Good Morning",font=('Helvetica',90),fg="LightGreen")
        label6.place(x=50,y=300)
elif time>=5 and time <= 10 :
    img=PhotoImage(file="icons/5-10.png")
    image=Label(image=img,bg="black",height=150,width=150)
    image.place(x=700,y=300)
    if time<24 :
        label6=Label(root,text="Good Morning",font=('Helvetica',70),fg="LightGreen")
        label6.place(x=50,y=300)
elif time>=10 and time <=14 :
    img=PhotoImage(file="icons/10-2.png")
    image=Label(image=img,bg="black",height=150,width=150)
    image.place(x=700,y=300)
    if time<24 :
        label6=Label(root,text="Good Noon",font=('Helvetica',90),fg="LightGreen")
        label6.place(x=50,y=300)
elif time>=14 and time <=17 :
    img=PhotoImage(file="icons/2-5.png")
    image=Label(image=img,bg="black",height=150,width=150)
    image.place(x=700,y=300)
    if time<24 :
        label6=Label(root,text="Good After Noon",font=('Helvetica',90),fg="LightGreen")
        label6.place(x=50,y=300)
else:
    img=PhotoImage(file="icons/5-7.png")
    image=Label(image=img,bg="black",height=150,width=150)
    image.place(x=700,y=300)
    if time<24 :
        label6=Label(root,text="Good Evening",font=('Helvetica',90),fg="LightGreen")
        label6.place(x=50,y=300)

#clock(here we will place time)
clock=Label(root,font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

#timezone
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

#thpwd
t=Label(root,font=("Helvetica",11),fg="white",bg="black")
t.place(x=150,y=120)
h=Label(root,font=("Helvetica",11),fg="white",bg="black")
h.place(x=150,y=140)
p=Label(root,font=("Helvetica",11),fg="white",bg="black")
p.place(x=150,y=160)
w=Label(root,font=("Helvetica",11),fg="white",bg="black")
w.place(x=150,y=180)
d=Label(root,font=("Helvetica",11),fg="white",bg="black")
d.place(x=150,y=200)

root.mainloop()
