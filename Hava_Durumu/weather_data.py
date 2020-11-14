from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
def find_country(location,link):
    spot = link
    time.sleep(1)
    driver.get(spot)
    tablo = driver.find_element_by_class_name('result-container')
    Country = driver.find_elements_by_class_name('search-result')

    for j in range(1,len(Country)-1):
        Country = driver.find_elements_by_class_name('search-result')

        time.sleep(1)
        print(Country[j].text)
        name_of_country = Country[j].text
        link_of_country = Country[j].find_element_by_xpath('/ html / body / div / div[5] / div[1] / div[1] / div[2] / a['+str(j+1)+']').get_attribute('href')
        print(name_of_country + " == " + link_of_country)
        cities_of_country(name_of_country,link_of_country)
        driver.get(spot)
        time.sleep(1)

def cities_of_country(city_name,link):
    new_spot = link
    time.sleep(1)
    driver.get(link)
    cities = driver.find_elements_by_class_name('search-result')
    for i in range(2,len(cities)):
        cities = driver.find_elements_by_class_name('search-result')
        city = cities[i].text
        link_of_city = cities[i].find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[2]/a['+str(i-1)+']').get_attribute('href')
        print(city + " == " + link_of_city)
        ilceler(city,link_of_city)
        driver.get(new_spot)
        time.sleep(1)
def ilceler(city_name,link):
    n_n_spot = link
    time.sleep(1)
    driver.get(link)
    ilceler_name = driver.find_elements_by_class_name('search-result')
    print("ilceler kısmı")
    for i in range(1,len(ilceler_name)):
        ilceler_name = driver.find_elements_by_class_name('search-result')
        ilce = ilceler_name[i].text
        link_of_ilce = ilceler_name[i].find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[2]/a['+str(i)+']').get_attribute('href')
        print("*"*30)
        print(ilce + " == " + link_of_ilce)
        Learn_Weather(city_name,ilce,link)
        driver.get(n_n_spot)

class Learn_Weather:
    def __init__(self,country,ilce,link):
        self.link = link
        pass
    def general_info(self):
        driver.get(self.link)
        time.sleep(1)
        main_card = driver.find_element_by_class_name('current-weather-details')
        info_of_left = main_card.find_elements_by_class_name('detail-item.spaced-content')
        for i in range(0,len(info_of_left)):
            text = str(info_of_left[i].text)
            text = text.split("\n")
            print(text[0] + " == " + text[1])
#            print("Derece == ",derece)

#            print("AIR_QUALITY == ",air_quality)
#            print("WIND == ",wind)
           # print("WIND GUSTS == ",wind_gusts)

    def hourly(self):
        linkler = driver.find_elements_by_class_name('more-cta-links ')
        linkler = linkler[1].find_elements_by_class_name('cta-link')
        hour_link = linkler[0].get_attribute('href')
        driver.get(hour_link)
        zaman = driver.find_element_by_class_name('hourly-wrapper.content-module')
        zaman = zaman.find_elements_by_class_name('accordion-item.hourly-card-nfl.hour.non-ad')
        print(len(zaman))

        for i in range(0,len(zaman)):
            if i==-1:
                click_button=zaman[i].find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[1]/div['+str(i+1)+']/div[1]')
                click_button.click()
            time.sleep(1)
            information_top= zaman[i].find_element_by_class_name('accordion-item-header-container ')
            information_bottom = zaman[i].find_element_by_class_name('accordion-item-content ')
            saat_ve_gun = information_top.find_element_by_class_name('date').text
            hava_derecesi = information_top.find_element_by_class_name('temp.metric').text
            hissedilen = information_top.find_element_by_class_name('real-feel').text
            durum = information_bottom.find_element_by_class_name('mobile-phrase').text
            information_bottom = information_bottom.find_element_by_class_name('hourly-content-container')
            information_bottom = information_bottom.find_elements_by_tag_name('p')
            print("*"*20)
            print(saat_ve_gun)
            print(len(information_bottom))
            print(information_bottom[8].text)
            for j in range(len(information_bottom)):
                if i==0:
                    degerin_adı = information_bottom[j].find_element_by_class_name('value')

                    card = str(information_bottom[j].text).split("\n")
                    degerin_adı = card[0]
                    deger = card[1]

                    print(degerin_adı,"==",deger)
                else:
                    click = zaman[i].find_element_by_class_name('icon-chevron.arrow.js-dropdown-toggle')
                    click.click()
            time.sleep(1)

                #print(degerin_adı.text, " == ", str(information_bottom[i].text).replace(str(degerin_adı.text),""))

    def daily(self):
        driver.get(self.link)
        hour_button = driver.find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div[8]/a[2]')
        hour_button.click()

def information_weather_of_city():
    pass

location = {'Africa':'https://www.accuweather.com/en/browse-locations/afr',
           'Antarctica':'https://www.accuweather.com/en/browse-locations/ant',
            'Arctic':'https://www.accuweather.com/en/browse-locations/arc',
            'Asia':'https://www.accuweather.com/en/browse-locations/asi',
            'Central America':'https://www.accuweather.com/en/browse-locations/cac',
            'Europe':'https://www.accuweather.com/en/browse-locations/eur',
            'Middle East':'https://www.accuweather.com/en/browse-locations/mea',
            'North America':'https://www.accuweather.com/en/browse-locations/nam',
            'Oceania':'https://www.accuweather.com/en/browse-locations/ocn',
            'South America':'https://www.accuweather.com/en/browse-locations/sam'
           }

url = "https://www.accuweather.com/en/browse-locations"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
istanbul = Learn_Weather("Turkey","istanbul",'https://www.accuweather.com/en/tn/mahdia/1-1314967_1_al/current-weather/1-1314967_1_al')
istanbul.general_info()
time.sleep(2)
istanbul.hourly()

def dene():
    location_of_world = driver.find_elements_by_class_name('search-result')
    print(location_of_world[0].text)
    print(len(location_of_world))

    y = [x for x in location_of_world]
    print(y)

    for j in range(0,len(location_of_world)):
        time.sleep(1)
        print(url)
        driver.get(url)
        country_of_location = driver.find_elements_by_class_name('search-result')
        name_of_location = country_of_location[j].text
        link = country_of_location[j].find_element_by_xpath('/html/body/div/div[5]/div[1]/div[1]/div/a['+str(j+1)+']').get_attribute('href')
        print(name_of_location + '=' + link)
        find_country(name_of_location,link)

#print(tablo[0].find_element_by_xpath("/html/body/div/div[5]/div[1]/div[1]/div/a[1]").get_attribute('href'))

