from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from compare_cars.models import *
from selenium import webdriver
import time
# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

class CartradeTest(TestCase):
    def test_cartrade(self):
        master_data_store = cartrade_masterdata.objects.create(
            website_name= "cartrade",
            city="Hyderabad", 
            city_name="Hyderabad",
            make_id ="hvmodelsMaruti-Suzuki",
            make_name = "Maruti Suzuki",
            model_id = "mod_800",
            model_name = "800")

        master_data_retrive = cartrade_masterdata.objects.all()
        for master in master_data_retrive:
            print master.city
            print master.make_id
            print master.model_id
            driver = webdriver.Firefox()
            driver.get('http://www.cartrade.com/buy-used-cars')
            close_popup = driver.find_element_by_css_selector('div#selectcityfilm a.closebtn')
            time.sleep(1)
            close_popup.click()
            select_city = driver.find_element_by_css_selector('div.leftbar select#sortcity  option[value^="%s"]'%master.city)
            select_city.click()
            time.sleep(1)
            select_model = driver.find_element_by_css_selector('li#%s div.spclass span.rcircle'%master.make_id)
            select_model.click()
            time.sleep(1)
            model_select =driver.find_element_by_css_selector('ul#mklist.features li#hvmodelsMaruti-Suzuki.hvchild.open ul#chmodelsMaruti-Suzuki li label input#%s'%master.model_id)
            model_select.click()
            time.sleep(1)
            car_data_list_total_div = [element for element in driver.find_elements_by_css_selector('div#searchFilters div.btmMrg.carlistblk div.widgetBox1 div.titleblk div.pull-left.carlistcont ')]

            for data in car_data_list_total_div:
                href = data.find_element_by_tag_name('a').get_attribute("href").encode("utf-8")
                price_car= data.find_element_by_tag_name('strong').text.encode("utf-8")
                title = data.find_element_by_tag_name('a').text
            
            print '***************'
            print "website name:www.cartrade.com"
            print '***************'
            print "title is:",title            
            print '***************'
            print "make name is :",master.make_name
            print '***************'
            print "model name is :",master.model_name
            print '***************'
            print "city name is :",master.city
            print '***************'
            print "link is:",href
            print '***************'
            print "price is:",price_car
            

            CarDetails(
            website_name=driver.title,
            city=master.city,
            makes=master.make_name,
            car_model= master.model_name,
            price = price_car,
            car_title =title,
            car_href = href,
                    ).save()

            details = CarDetails.objects.all()
            self.assertEqual(details.count(), 1)



'''
Run test case by using follwoing commands

python manage.py test

python manage.py test scrapcars.tests.CartradeTest.test_cartrade


'''