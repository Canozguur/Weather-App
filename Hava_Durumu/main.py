import requests
from bs4 import BeautifulSoup
from kivymd.uix.selectioncontrol import MDSwitch,MDCheckbox
from kivymd.uix.textfield import MDTextFieldRect
from selenium import webdriver
from kivymd.uix.label import MDLabel
import selenium
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import Button, MDFloatingActionButton
from kivymd.uix.card import MDCard
from kivymd.uix.card import MDSeparator
import time
from kivy.uix.modalview import ModalView
from kivy.uix.scrollview import ScrollView
from webdriver_manager.chrome import ChromeDriverManager
from kivymd.uix.boxlayout import BoxLayout
import scrapy
from kivy.properties import StringProperty,BoundedNumericProperty,BooleanProperty
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
city = "bursa"
url = 'https://www.timeanddate.com/weather/turkey/'+city
print(url)
hourly_url = url+"/hourly"
daily_url = url+"/ext"
from kivy.core.window import Window
Window.size = (350, 625)
class de(BoxLayout):
    pass


class card_of_today(MDCard):
    sunrise = StringProperty()
    sunset = StringProperty()
    wind = StringProperty()
    feels_like = StringProperty()
    status = StringProperty()

class card_of_hours(MDCard):
    hour = StringProperty()
    status_of_weather = StringProperty()
    temp_of_hour = StringProperty()
    bc_color = BooleanProperty()
    text_color = BooleanProperty()

class card_of_daily(MDCard):
    day = StringProperty()
    temperature = StringProperty()
    image = StringProperty()
    color = BooleanProperty()
    text_color = BooleanProperty()
class search(ModalView):
    pass
days = {"Pzt":"Monday",
        "Sal":"Tuesday",
        "Çar":"Wednesday",
        "Per":"Thursday",
        "Cum":"Friday",
        "Cmt":"Saturday",
        "Paz":"Sunday"}
class MainScreen(MDScreen):
    pass

class NewScreen(MDScreen):
    pass
from kivymd.uix.label import Label
from kivymd.uix.taptargetview import MDTapTargetView

class ImageButton(ButtonBehavior, Image):
    pass
class MainApp(MDApp):

    def change_screen(self,text,situation):
        print(situation)
        if situation== True:
            self.country_of_search = "usa"
        else:
            self.country_of_search = "turkey"
        try:
            self.screen_text = 'new_city_name_of_'+text

            screen_of_new_city = MDScreen(name=f'new_city_name_of_{text}')

            self.new_screen = de()
            self.root.ids['screen_manager'].add_widget(screen_of_new_city)

            screen_of_new_city.add_widget(self.new_screen)



            city = str(text).lower()
            url = 'https://www.timeanddate.com/weather/'+self.country_of_search +'/' + city
            if requests.get(url).ok:
                print(url)
                self.hourly_url = url + "/hourly"
                self.daily_url = url + "/ext"
                self.new_screen.ids.city_name.text = city.title()
                self.new_daily(self.daily_url)
                self.background_time()
                self.root.ids['new_screen'].ids.city.text = city.title()
                self.root.ids['screen_manager'].current = self.screen_text
                self.sea.dismiss()
            else:
                self.sea.ids['spot'].add_widget(Label(text="Not Founded",pos_hint={"center_x":.5,"center_y":.45},color=(0,122,122,1),font_size="22sp"))
        except Exception:
            self.sea.ids['spot'].add_widget(
                Label(text="Not Founded", pos_hint={"center_x": .5, "center_y": .45}, color=(0, 0, 0, 1),font_size="22sp" ))

    def new_daily(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        tablo = soup.find(class_='tb-scroll')
        img = tablo.find_all('img')

        data = tablo.find_all('tr')
        full_text = data[2].get_text()
        #######
        #####
        ###
        ##
        sunset = full_text[-1:-6:-1][::-1]
        sunrise = full_text[-6:-11:-1][::-1]
        print(sunrise, sunset)
        texts = str(full_text).split(" ")
        # print(texts)
        # print(full_text)
        situation = str(full_text).split("°C")
        # print(situation)
        wind = situation[2][0:7]
        day_name = texts[0][0:3]
        day_num = texts[0].replace(day_name[0:3], "")
        day = day_num + texts[1][0:3]
        second = texts[3].replace("xa", " ")
        second = situation[0].split(" ")
        # print(second)
        temp = str(texts[1][3:]) + "/" + str(second[3].replace("\xa0", "") + " °C")
        day_name = days[day_name]

        print("day name ==", day_name)
        print("day ==", day)
        print("temperature ==", temp)
        situation = situation[1].split(".")
        # print(situation)
        if situation[1][0:2].isdigit() == True:
            situation_of_weather = situation[0]
            print("situation of weather ==", situation_of_weather)
            feels_like = str(situation[1]) + " °C"
            print("feels like ==", feels_like)
            print("wind speed ==", wind)
            print("*" * 40)
            # self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
            source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
            source = "weather_images/" + source + ".png"
            status = "Today: " + situation_of_weather + " and weather is between " + temp.replace("/",
                                                                                                  " / ") + " temperature"
            print(status)

            # self.root.ids['main_screen'].today.add_widget(card_of_today(sunrise=sunrise,sunset=sunset,wind=wind,feels_like=feels_like,status=situation_of_weather))
            self.new_screen.ids.feels_like.text = feels_like
            self.new_screen.ids.sunrise.text = sunrise
            self.new_screen.ids.sunset.text = sunset
            self.new_screen.ids.wind.text = wind
            self.new_screen.ids.today_info.text = status
            self.sunrise = sunrise
            self.sunset = sunset
        elif situation[1][0:1].isdigit() == True:
            situation_of_weather = situation[0]
            print("situation of weather ==", situation_of_weather)
            feels_like = str(situation[1]) + " °C"
            print("feels like ==", feels_like)
            print("wind speed ==", wind)
            print("*" * 40)
            source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
            source = "weather_images/" + source + ".png"
            status = "Today: " + situation_of_weather + " and weather is between " + temp.replace("/",
                                                                                                  " / ") + " temperature"
            # self.root.ids['main_screen'].today.add_widget(card_of_today(sunrise=sunrise,sunset=sunset,wind=wind,feels_like=feels_like,status=situation_of_weather))
            self.new_screen.ids.feels_like.text = feels_like
            self.new_screen.ids.sunrise.text = sunrise
            self.new_screen.ids.sunset.text = sunset
            self.new_screen.ids.wind.text = wind
            self.new_screen.ids.today_info.text = status
            self.sunrise = sunrise
            self.sunset = sunset
        else:
            situation_of_weather = str(situation[0]) + str(situation[1])
            print("situation of weather ==", situation_of_weather)
            feels_like = str(situation[2]) + " °C"
            print("feels like ==", feels_like)
            print("wind speed ==", wind)
            print("*" * 40)
            source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
            source = "weather_images/" + source + ".png"
            status = "Today: " + situation_of_weather + " and weather is between " + temp.replace("/",
                                                                                                  " / ") + " temperature"
            print(status)
            # self.root.ids['main_screen'].today.add_widget(card_of_today(sunrise=sunrise,sunset=sunset,wind=wind,feels_like=feels_like,status=situation_of_weather))
            self.new_screen.ids.feels_like.text = feels_like
            self.new_screen.ids.sunrise.text = sunrise
            self.new_screen.ids.sunset.text = sunset
            self.new_screen.ids.wind.text = wind
            self.new_screen.ids.today_info.text = status
            self.sunrise = sunrise
            self.sunset = sunset
            ####
            ###
            ###
            ###
            ###
        self.new_hourly(self.hourly_url)  ##### This code suppose to be here cause of i little bit comlicated the code
        #######
        ####
        ###

        for i in range(2, len(data) - 3):
            j = i - 2
            src = str(img[j]).split("src")
            src = src[1].split(" ")[0].replace("=", "")[1:][:-1][24:].replace(".svg", "") + ".png"

            print(src)
            full_text = data[i].get_text()
            sunset = full_text[-1:-6:-1][::-1]
            sunrise = full_text[-6:-11:-1][::-1]
            print(sunrise, sunset)
            texts = str(full_text).split(" ")
            # print(texts)
            # print(full_text)
            situation = str(full_text).split("°C")
            # print(situation)
            wind = situation[2][0:7]
            day_name = texts[0][0:3]
            day_num = texts[0].replace(day_name[0:3], "")
            day = day_num + texts[1][0:3]
            second = texts[3].replace("xa", " ")
            second = situation[0].split(" ")
            # print(second)
            temp = str(texts[1][3:]) + "/" + str(second[3].replace("\xa0", "") + " °C")
            day_name = days[day_name]
            if i == 2:
                print(full_text)
                sunset = full_text[-1:-6:-1][::-1]
                sunrise = full_text[-6:-11:-1][::-1]
            print("day name ==", day_name)
            print("day ==", day)
            print("temperature ==", temp)
            situation = situation[1].split(".")
            # print(situation)
            if situation[1][0:2].isdigit() == True:
                situation_of_weather = situation[0]
                print("situation of weather ==", situation_of_weather)
                feels_like = str(situation[1]) + " °C"
                print("feels like ==", feels_like)
                print("wind speed ==", wind)
                print("*" * 40)
                # self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
                source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
                src = "weather_images/" + src
                print(source)
                self.new_screen.ids.daily.add_widget(
                    card_of_daily(day=day_name, temperature=temp, image=src, color=self.bc_color,
                                  text_color=self.text_color))
            elif situation[1][0:1].isdigit() == True:
                situation_of_weather = situation[0]
                print("situation of weather ==", situation_of_weather)
                feels_like = str(situation[1]) + " °C"
                print("feels like ==", feels_like)
                print("wind speed ==", wind)
                print("*" * 40)
                source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
                src = "weather_images/" + src
                print(source)
                # self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
                self.new_screen.ids.daily.add_widget(
                    card_of_daily(day=day_name, temperature=temp, image=src, color=self.bc_color,
                                  text_color=self.text_color))
            else:
                denemelik = situation[0]
                situation_of_weather = str(situation[0]) + str(situation[1])
                print("situation of weather ==", situation_of_weather)
                feels_like = str(situation[2]) + " °C"
                print("feels like ==", feels_like)
                print("wind speed ==", wind)
                print("*" * 40)
                # source = str(denemelik).replace(" ", "_").replace(".", "").lower()
                src = "weather_images/" + src
                # self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
                self.new_screen.ids.daily.add_widget(
                    card_of_daily(day=day_name, temperature=temp, image=src, color=self.bc_color,
                                  text_color=self.text_color))

        pass

    def new_hourly(self,url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        tablo = soup.find(class_='tb-scroll')
        data = tablo.find_all('tr')
        img = tablo.find_all('img')
        self.time = data[2].get_text()[:5]
        self.background_time()
        for i in range(3, len(data) - 1):
            full_text = data[i].get_text()
            hour = full_text[:5]
  # here is gonna be as a different splitting cause of day
            j = i - 2
            src = str(img[j]).split("src")
            src = src[1].split(" ")[0].replace("=", "")[1:][:-1][24:].replace(".svg", "") + ".png"

            temp_of_hour = full_text[5:10]
            new_text = full_text[10:]
            new_text = str(new_text).split("°C")
            feels_like = new_text[0]
            feels_like = feels_like[:-4:-1]
            status = new_text[0]
            status = status[:-3]
            wind = new_text[1]
            wind = wind[0:7]
            feels_like = feels_like[::-1]
            new_temp = str(full_text).split("°C")[1].split(".")[-1].replace(" ","")+"°C"

            print("time == ", hour)
            print("Temperature of hour == ", new_temp)
            print("situation of weather == ", status)
            print("Feels like == ", feels_like)
            print("Wind == ", wind)
            print("*" * 40)
            status = str(status).replace(" ", "_").replace(".", "").lower()

            if int(str(hour)[0:2]) < 6 or int(str(hour)[0:2]) > 21:
                morning = True
                night = False

                if str(hour[0:2]) == "00":  # i am gonna put here png which is gonna be This New Day text thing
                    status = "weather_images/" +"new_day.png"
                    print("newday")
                    self.new_screen.ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=full_text[5:11],
                                      bc_color=self.bc_color, text_color=self.text_color))

                else:
                    src = "weather_images/" + src
                    self.new_screen.ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(src), temp_of_hour=new_temp,
                                      bc_color=self.bc_color, text_color=self.text_color))


            else:
                night = True
                morning = False
                print(status)
                if status == "sprinkles_more_sun_than_clouds":
                    status = "rainy"
                    status = "weather_images/" + src
                    self.new_screen.ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=new_temp,
                                      bc_color=self.bc_color, text_color=self.text_color))
                elif status == "sprinkles_partly_cloudy":
                    status = "rainy"
                    status = "weather_images/" + src
                    self.new_screen.ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=new_temp,
                                      bc_color=self.bc_color, text_color=self.text_color))

                else:
                    status = "weather_images/" + src
                    self.new_screen.ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=new_temp,
                                      bc_color=self.bc_color, text_color=self.text_color))

        pass

    def new_one(self):
        self.sea = search()
        self.sea.open()



    def background_time(self):
        print(self.time)
        print(self.sunrise)
        print(self.sunset)
        if int(self.time[0:2]) > int(self.sunrise[0:2]) and int(self.time[0:2])<= int(self.sunset[0:2]):
            print("öğlen")
            self.bc_color =(.1098, .650, .99215, 1)
            self.text_color = (1,1,1,1)
        else:
            print("akşam")
            self.bc_color =(.019,.11,.47 ,1)
            self.text_color = (1,1,1,1)

    def on_start(self):
        self.daily(daily_url)
        self.background_time()


    def daily(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        tablo = soup.find(class_='tb-scroll')
        img = tablo.find_all('img')

        data = tablo.find_all('tr')
        full_text = data[2].get_text()
        #######
        #####
        ###
        ##
        sunset = full_text[-1:-6:-1][::-1]
        sunrise = full_text[-6:-11:-1][::-1]
        print(sunrise, sunset)
        texts = str(full_text).split(" ")
        # print(texts)
        # print(full_text)
        situation = str(full_text).split("°C")
        # print(situation)
        wind = situation[2][0:7]
        day_name = texts[0][0:3]
        day_num = texts[0].replace(day_name[0:3], "")
        day = day_num + texts[1][0:3]
        second = texts[3].replace("xa", " ")
        second = situation[0].split(" ")
        # print(second)
        temp = str(texts[1][3:]) + "/" + str(second[3].replace("\xa0", "") + " °C")
        day_name = days[day_name]

        print("day name ==", day_name)
        print("day ==", day)
        print("temperature ==", temp)
        situation = situation[1].split(".")
        # print(situation)
        if situation[1][0:2].isdigit() == True:
            situation_of_weather = situation[0]
            print("situation of weather ==", situation_of_weather)
            feels_like = str(situation[1]) + " °C"
            print("feels like ==", feels_like)
            print("wind speed ==", wind)
            print("*" * 40)
            # self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
            source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
            source = "weather_images/" + source + ".png"
            status = "Today: "+ situation_of_weather +" and weather is between " +temp.replace("/"," / ")+" temperature"
            print(status)
            #self.root.ids['main_screen'].today.add_widget(card_of_today(sunrise=sunrise,sunset=sunset,wind=wind,feels_like=feels_like,status=situation_of_weather))
            self.root.ids['main_screen'].ids.feels_like.text = feels_like
            self.root.ids['main_screen'].ids.sunrise.text = sunrise
            self.root.ids['main_screen'].ids.sunset.text = sunset
            self.root.ids['main_screen'].ids.wind.text = wind
            self.root.ids['main_screen'].ids.today_info.text = status
            self.sunrise = sunrise
            self.sunset = sunset
        elif situation[1][0:1].isdigit() == True:
            situation_of_weather = situation[0]
            print("situation of weather ==", situation_of_weather)
            feels_like = str(situation[1]) + " °C"
            print("feels like ==", feels_like)
            print("wind speed ==", wind)
            print("*" * 40)
            source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
            source = "weather_images/" + source + ".png"
            status = "Today: "+ situation_of_weather +" and weather is between " +temp.replace("/"," / ")+" temperature"
            #self.root.ids['main_screen'].today.add_widget(card_of_today(sunrise=sunrise,sunset=sunset,wind=wind,feels_like=feels_like,status=situation_of_weather))
            self.root.ids['main_screen'].ids.feels_like.text = feels_like
            self.root.ids['main_screen'].ids.sunrise.text = sunrise
            self.root.ids['main_screen'].ids.sunset.text = sunset
            self.root.ids['main_screen'].ids.wind.text = wind
            self.root.ids['main_screen'].ids.today_info.text = status
            self.sunrise = sunrise
            self.sunset = sunset
        else:
            situation_of_weather = str(situation[0]) + str(situation[1])
            print("situation of weather ==", situation_of_weather)
            feels_like = str(situation[2]) + " °C"
            print("feels like ==", feels_like)
            print("wind speed ==", wind)
            print("*" * 40)
            source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
            source = "weather_images/" + source + ".png"
            status = "Today: "+ situation_of_weather +" and weather is between " +temp.replace("/"," / ")+" temperature"
            print(status)
            #self.root.ids['main_screen'].today.add_widget(card_of_today(sunrise=sunrise,sunset=sunset,wind=wind,feels_like=feels_like,status=situation_of_weather))
            self.root.ids['main_screen'].ids.feels_like.text = feels_like
            self.root.ids['main_screen'].ids.sunrise.text = sunrise
            self.root.ids['main_screen'].ids.sunset.text = sunset
            self.root.ids['main_screen'].ids.wind.text = wind
            self.root.ids['main_screen'].ids.today_info.text = status
            self.sunrise = sunrise
            self.sunset = sunset
            ####
            ###
            ###
            ###
            ###
        self.hourly(hourly_url) ##### This code suppose to be here cause of i little bit comlicated the code
        #######
        ####
        ###
        for i in range(2, len(data) - 3):
            j = i-2
            src = str(img[j]).split("src")
            src = src[1].split(" ")[0].replace("=", "")[1:][:-1][24:].replace(".svg","") +".png"

            print(src)
            full_text = data[i].get_text()
            sunset =full_text[-1:-6:-1][::-1]
            sunrise = full_text[-6:-11:-1][::-1]
            print(sunrise,sunset)
            texts = str(full_text).split(" ")
            # print(texts)
            # print(full_text)
            situation = str(full_text).split("°C")
            # print(situation)
            wind = situation[2][0:7]
            day_name = texts[0][0:3]
            day_num = texts[0].replace(day_name[0:3], "")
            day = day_num + texts[1][0:3]
            second = texts[3].replace("xa", " ")
            second = situation[0].split(" ")
            # print(second)
            temp = str(texts[1][3:]) + "/" + str(second[3].replace("\xa0", "") + " °C")
            day_name = days[day_name]
            if i == 2:
                print(full_text)
                sunset = full_text[-1:-6:-1][::-1]
                sunrise = full_text[-6:-11:-1][::-1]
            print("day name ==", day_name)
            print("day ==", day)
            print("temperature ==", temp)
            situation = situation[1].split(".")
            # print(situation)
            if situation[1][0:2].isdigit() == True:
                situation_of_weather = situation[0]
                print("situation of weather ==", situation_of_weather)
                feels_like = str(situation[1]) + " °C"
                print("feels like ==", feels_like)
                print("wind speed ==", wind)
                print("*" * 40)
                #self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
                source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
                src = "weather_images/" + src
                print(source)
                self.root.ids['main_screen'].ids.daily.add_widget(card_of_daily(day=day_name,temperature=temp,image=src,color=self.bc_color,text_color=self.text_color))
            elif situation[1][0:1].isdigit() == True:
                situation_of_weather = situation[0]
                print("situation of weather ==", situation_of_weather)
                feels_like = str(situation[1]) + " °C"
                print("feels like ==", feels_like)
                print("wind speed ==", wind)
                print("*" * 40)
                source = str(situation_of_weather).replace(" ", "_").replace(".", "").lower()
                src = "weather_images/" + src
                print(source)
                #self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
                self.root.ids['main_screen'].ids.daily.add_widget(card_of_daily(day=day_name,temperature=temp,image=src,color=self.bc_color,text_color=self.text_color))
            else:
                denemelik = situation[0]
                situation_of_weather = str(situation[0]) + str(situation[1])
                print("situation of weather ==", situation_of_weather)
                feels_like = str(situation[2]) + " °C"
                print("feels like ==", feels_like)
                print("wind speed ==", wind)
                print("*" * 40)
                #source = str(denemelik).replace(" ", "_").replace(".", "").lower()
                src = "weather_images/" + src
                #self.root.ids['main_screen'].ids.day.add_widget(card(hour=))
                self.root.ids['main_screen'].ids.daily.add_widget(card_of_daily(day=day_name,temperature=temp,image=src,color=self.bc_color,text_color=self.text_color))

        ############
        ###########
        #########
        #######




    ##############
    ###########
    #########
    ##########
    #######
    def hourly(self,url):  # This is literally good for now without png spots
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        tablo = soup.find(class_='tb-scroll')
        data = tablo.find_all('tr')
        img = tablo.find_all('img')
        self.time = data[2].get_text()[:5]
        self.background_time()
        for i in range(3, len(data) - 1):
            full_text = data[i].get_text()
            hour = full_text[:5]
            print(full_text)
            new_temp = str(full_text).split("°C")[1].split(".")[-1].replace(" ","")+"°C"


            j = i - 2
            src = str(img[j]).split("src")
            src = src[1].split(" ")[0].replace("=", "")[1:][:-1][24:].replace(".svg", "") + ".png"

            temp_of_hour = full_text[5:10]
            new_text = full_text[10:]
            new_text = str(new_text).split("°C")
            feels_like = new_text[0]
            feels_like = feels_like[:-4:-1]
            status = new_text[0]
            status = status[:-3]
            wind = new_text[1]
            wind = wind[0:7]
            feels_like = feels_like[::-1]
            print("time == ", hour)
            print("Temperature of hour == ", new_temp)
            print("situation of weather == ", status)
            print("Feels like == ", feels_like)
            print("Wind == ", wind)
            print("*" * 40)
            status = str(status).replace(" ", "_").replace(".", "").lower()

            if int(str(hour)[0:2])<6 or int(str(hour)[0:2])>21 :
                morning = True
                night = False

                if str(hour[0:2]) == "00":  # i am gonna put here png which is gonna be This New Day text thing
                    status = "weather_images/" "new_day.png"
                    print("newday")
                    self.root.ids['main_screen'].ids.hour.add_widget(card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=full_text[5:11],bc_color=self.bc_color,text_color=self.text_color))

                else:
                    src = src = "weather_images/" + src
                    self.root.ids['main_screen'].ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(src), temp_of_hour=new_temp,bc_color=self.bc_color,text_color=self.text_color))


            else:
                night = True
                morning = False
                print(status)
                if status == "sprinkles_more_sun_than_clouds":
                    status = "rainy"
                    status = "weather_images/" + src
                    self.root.ids['main_screen'].ids.hour.add_widget(
                        card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=new_temp,bc_color=self.bc_color,text_color=self.text_color))
                elif status == "sprinkles_partly_cloudy":
                    status = "rainy"
                    status = "weather_images/" + src
                    self.root.ids['main_screen'].ids.hour.add_widget(card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=new_temp,bc_color=self.bc_color,text_color=self.text_color))

                else:
                    status = "weather_images/" + src
                    self.root.ids['main_screen'].ids.hour.add_widget(card_of_hours(hour=hour, status_of_weather=str(status), temp_of_hour=new_temp,bc_color=self.bc_color,text_color=self.text_color))


MainApp().run()
