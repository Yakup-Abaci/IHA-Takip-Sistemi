import socket, cv2, pickle, struct
from threading import Thread
from pymavlink import mavutil
import time
from math import radians, sin, cos, sqrt, atan2,asin,atan,degrees
#import RPi.GPIO as GPIO
class anten:
    def __init__(self):
        self.servoPIN = 17
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(servoPIN, GPIO.OUT)
        #self.pwm = GPIO.PWM(self.servoPIN, 50)
        #self.pwm.start(0)
        self.yer_istasyonu = {"lat":-35.3632604,"lon":149.1652399,"alt":1,"heading":33}
        self.aci=90
        self.servo(self.aci)

    def servo(self,aci):
        self.aci += aci
        x=(33/90)*self.aci + 33
        #self.pwm.ChangeDutyCycle(duty)
        #time.sleep(0.2)
        #self.pwm.stop()


    def haversine(self,lat1, lon1, lat2, lon2):
        # Radyan cinsinden koordinatları al
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        # Haversine formülü
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        # Dünya yarıçapı (ortalama)
        R = 6371.0  # Dünya yarıçapı kilometre cinsinden

        # Gerçek uzaklık hesaplama
        distance = R * c * 1000  # Metre cinsinden

        return distance
    

    def hesapla(self,lat,lon,alt): # aracın konum bilgileri
        #Yer İstasyonu konumu
        
        lat_u = self.haversine(lat, self.yer_istasyonu["lon"], self.yer_istasyonu["lat"], self.yer_istasyonu["lon"])
        lon_u = self.haversine(self.yer_istasyonu["lat"], lon, self.yer_istasyonu["lat"], self.yer_istasyonu["lon"])
        #self.yer_istasyonu["heading"] %=360
        if int(lat_u) == 0 and int(lon_u) == 0:
            yatay_aci = 0
     
        else:
            yatay_aci = degrees(atan(lon_u/lat_u))
            hipotenüs = sqrt(pow(lat_u,2)+pow(lon_u,2))
            dikey_aci = degrees(atan((alt-self.yer_istasyonu["alt"])/hipotenüs))
            k1,k2=1,1
            if 0<=self.yer_istasyonu["heading"]<90:
                if lon < self.yer_istasyonu["lon"]:
                    k1=-1
                if lat < self.yer_istasyonu["lat"]:
                    k2=-1
                if k1+k2 <0:
                    yatay_aci *=-1
                elif k1+k2 > 0:
                    yatay_aci*=-1
                    yatay_aci +=180
          
                yatay_aci -= self.yer_istasyonu["heading"]
                self.yer_istasyonu["heading"] +=  yatay_aci
                self.yer_istasyonu["heading"] %= 360

            elif 90<=self.yer_istasyonu["heading"]<180:
                if lon < self.yer_istasyonu["lon"]:
                    k1 = -1
                if abs(lat) < abs(self.yer_istasyonu["lat"]):
                    k2=-1

                if k1>0 and k2<0:
                    yatay_aci -= self.yer_istasyonu["heading"]
                    
                else:
                    if k1<0 and k2>0:
                        pass
                    else:
                        yatay_aci *= -1
                    yatay_aci +=180 -self.yer_istasyonu["heading"]
                self.yer_istasyonu["heading"] +=  yatay_aci
                self.yer_istasyonu["heading"] %= 360

            elif 180<=self.yer_istasyonu["heading"]<270:
                if lon < self.yer_istasyonu["lon"]:
                    k1 = -1
                if abs(lat) < abs(self.yer_istasyonu["lat"]):
                    k2=-1
                if k1+k2 == 0:
                    yatay_aci += 180-self.yer_istasyonu["heading"]
                elif k1+k2<0:
                    yatay_aci *=-1
                    yatay_aci += 360-self.yer_istasyonu["heading"]
                else:
                    yatay_aci += self.yer_istasyonu["heading"] -180
                    yatay_aci *=-1

                self.yer_istasyonu["heading"] +=  yatay_aci
                self.yer_istasyonu["heading"] %= 360

            else:
                if lon < self.yer_istasyonu["lon"]:
                    k1 = -1
                if abs(lat) < abs(self.yer_istasyonu["lat"]):
                    k2=-1
                    
                if k1>0 and k2<0:
                    yatay_aci += 360-self.yer_istasyonu["heading"]

                elif k1<0 and k2>0:
                    yatay_aci +=180-self.yer_istasyonu["heading"]

                else:
                    yatay_aci -= 360
                    yatay_aci *= -1
                    yatay_aci -= self.yer_istasyonu["heading"]
                self.yer_istasyonu["heading"] +=  yatay_aci
                self.yer_istasyonu["heading"] %= 360
            

        return yatay_aci
    
    def gonder(self):
    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.167", 9999))
        while True:
            msg = pickle.loads(s.recv(1024))
            
            #message = {"lat":a[0],"lon":a[1],"alt":a[2]}
            #message = pickle.dumps(message)

            #c.send(message)
            #time.sleep(0.05)
            aci = self.hesapla(msg["lat"],msg["lon"],msg["alt"])
            #self.servo(aci)
        #message = {"aci":aci}
        #data = pickle.dumps(message)
        #client.send(data)
        time.sleep(0.5)

anten=anten()
anten.gonder()

