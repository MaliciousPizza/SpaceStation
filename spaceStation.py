#!/usr/bin/env python3
import urllib.request
import json
import turtle
import time

#ISS Locatation url
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

staturl = 'http://api.open-notify.org/iss-now.json'
stresponse = urllib.request.urlopen(staturl)
stresult = json.loads(stresponse.read())

#ISS Location
location = stresult['iss_position']
lat = location['latitude']
lon = location['longitude']
#Space Center, Houston
mylat = 39.304900
mylon = -76.719280


#background image
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map2.gif')

#iss location
screen.register_shape('iss2.gif')
iss = turtle.Turtle()
iss.shape('iss2.gif')
iss.setheading(90)

iss.penup()
iss.goto(float(lon),float(lat))

#houston location
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(mylon,mylat)
mylocation.dot(5)
mylocation.hideturtle()

#url to determine the distance from houston
disturl = 'http://api.open-notify.org/iss-pass.json'
disturl = disturl + '?lat=' + str(lat) + '&lon=' + str(lon)
distresponse = urllib.request.urlopen(disturl)
distresult = json.loads(distresponse.read())

over = distresult['response'][1]['risetime']

style = ('Ariel', 6, 'bold')
mylocation.write(time.ctime(over), font=style)



#print('People in Space: ',result['number'])

#people = result['people']

#for p in people:
#    name = p['name']
#    craft = p['craft']
#    peeps = str(result['number']) + ' people in space ' + name + ' in ' + craft +'\r\n'
    
#print('latitude: ', lat)
#print('longitude: ', lon)

#loops terminal to keep it active. 
turtle.mainloop()