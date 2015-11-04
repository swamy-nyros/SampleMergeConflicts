from django.shortcuts import render
<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.http import HttpResponse

from compare_cars.models import Car_Master_Data,CarDetails

def master_data(request):

    city_id = ['105','2','12','3000','176','198','128','10','224','244']
    cities=['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'Delhi','Noida','Chandigarh']
    city_name = dict(zip(city_id,cities))

    make_id = ['10','8','20','16','17','7','5','2','9','15']
    makes=['Maruti Suzuki','Hyundai','Volkswagen','Tata','Toyota','Honda','Ford','Chevrolet','Mahindra','Skoda']
    makes_name = dict(zip(make_id,makes))

    Maruti_models_id = ['10.24','10.41','10.35','10.288','10.332']
    Maruti_models_name=['800','A-Star','Alto','Swift','Zen']
    Maruti = dict(zip(Maruti_models_id,Maruti_models_name))

    Hyundai_models_id=['8.307','8.31','8.113','8.261','8.278']
    Hyundai_models_name=['Verna','Accent','Elantra','Santro','Sonata']
    Hyundai = dict(zip(Hyundai_models_id,Hyundai_models_name))

    Volkswagen_models_id=['20.304','20.227','20.177','20.224']
    Volkswagen_models_name=['Vento','Polo','Jetta,Passat']
    Volkswagen = dict(zip(Volkswagen_models_id,Volkswagen_models_name))

    Tata_models_id=['16.169','16.169','16.257','16.213','16.193']
    Tata_models_name = ["Indica","Indigo","Safari","Nano","Manza"]
    Tata = dict(zip(Tata_models_id,Tata_models_name))

    Toyota_models_id=['17.172','17.135','17.88','17.353','17.58']
    Toyota_models_name = ['Innova','Fortuner','Corolla','Corolla Altis','Camry']
    Toyota = dict(zip(Toyota_models_id,Toyota_models_name))

    Honda_models_id=['7.32','7.36','7.74','7.75','7.98']
    Honda_models_name=['Accord','Amaze','City','Civic','CR-V']
    Honda = dict(zip(Honda_models_id,Honda_models_name))

    Ford_models_id=['5.111','5.114','5.128','5.166','5.141']
    Ford_models_name=['Ecosport','Endeavour','Fiesta','Ikon','Fusion']
    Ford = dict(zip(Ford_models_id,Ford_models_name))

    Chevrolet_models_id=['2.46','2.299','2.60','2.115','2.279']
    Chevrolet_models_name=['Aveo','Aveo U-Va','Captiva','Enjoy','Spark']
    Chevrolet = dict(zip(Chevrolet_models_id,Chevrolet_models_name))

    Mahindra_models_id=['9.53','9.174','9.266','9.236','9.328']
    Mahindra_models_name=['Bolero','Jeep','Scorpio','Quanto','Xylo']
    Mahindra = dict(zip(Mahindra_models_id,Mahindra_models_name))

    Skoda_models_id=['15.126','15.184','15.215','15.287','15.241']
    Skoda_models_name=['Fabia','Laura','Octavia','Superb','Rapid']
    Skoda = dict(zip(Skoda_models_id,Skoda_models_name))

    for key,values in city_name.items():
        city_id=key
        city_name=values
        print city_name
        for key,values in makes_name.items():
            make_id=key
            make_name=values
            print make_name
            if make_name == "Maruti Suzuki":
                for key,values in Maruti.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Hyundai":
                for key,values in Hyundai.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Volkswagen":
                for key,values in Volkswagen.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Tata":
                for key,values in Tata.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Toyota":
                for key,values in Toyota.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Honda":
                for key,values in Honda.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Ford":
                for key,values in Ford.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Chevrolet":
                for key,values in Chevrolet.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Mahindra":
                for key,values in Mahindra.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()
            elif make_name == "Skoda":
                for key,values in Skoda.items():
                    data=Car_Master_Data(website_name="www.carwale.com",city_id=city_id,city_name=city_name,make_id=make_id,make_name=make_name,model_id=key,model_name=values).save()

    return HttpResponse("master data of carwale stored into the database successfully")

def scrollDown(driver, numberOfScrollDowns):
    body = driver.find_element_by_tag_name("body")
    while numberOfScrollDowns >=0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
    return driver



def carwale(request):
    driver = webdriver.Firefox()
    all_cars = Car_Master_Data.objects.all()
    for car in all_cars:
        driver.get("http://www.carwale.com/used/cars-for-sale/")
        print driver.title
        time.sleep(2)
        car_city = car.city_id
        car_make = car.make_id
        car_model = car.model_id
        city_name=car.city_name
        make_name=car.make_name
        model_name=car.model_name
        city = driver.find_element_by_css_selector('select#drpCity.form-control option[value="%s"]'%car_city)
        city.click()
        print city_name
        time.sleep(2)
        make = driver.find_element_by_css_selector("ul#makesList.ul-makes li.us-sprite.makeLi[carfilterid='%s']"%car_make) 
        make.click()
        print make_name
        time.sleep(10)
        model = driver.find_element_by_css_selector('ul#makesList.ul-makes li.us-sprite.makeLi div.list-points-models ul.rootUl li.us-sprite.rootLi[carfilterid="%s"]'%car_model)
        model.click()
        print model_name
        time.sleep(2)
        print '********cardata****'
        driver = scrollDown(driver, 2)
        car_data_list = [element for element in driver.find_elements_by_css_selector('div.stock-list ul#listing1.ko-listing li.listing-adv.listingContent.padding-top10.padding-bottom10.cur-pointer div.stock-detail')]        
        print "*********"*12
        print city_name
        time.sleep(2)
        for data in car_data_list:
            price = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 span.rupee-lac.slprice.font20').text
            print price
            time.sleep(2)

            title= data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').text
            print title

            href = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 h2.listingTitle.font18 a').get_attribute("href")
            print href
            time.sleep(5)

            driver = scrollDown(driver, 2)
            print"scroll"

            image = data.find_element_by_css_selector('div.leftfloat.thumb-div div.thumb-area div.img-placer a.slideShow img').get_attribute("src")
            print image

            year = data.find_element_by_css_selector('div.leftfloat.table-div.margin-left20 a.text-grey p.listingItemKms.font14.text-light-grey.margin-top5 span:nth-of-type(7)').text
            print year

            time.sleep(2)
            CarDetails(website_name="www.carwale.com",
                city=city_name,
                car_make=make_name,
                car_model=model_name,
                price=price,
                model_year=year,
                car_title=title,
                car_href=href,
                car_image =image,
                ).save()
                        

    return HttpResponse("carwale data stored into the database successfully")

    
def masterdata_cartrade(request):
    city_list =['Hyderabad', 'Bangalore' , 'Pune', 'Mumbai','Chennai' ,'Kolkata', 'Ahmedabad', 'New Delhi','Noida','chandigarh']
    
    make_name= ['Maruthi suziki', ]   

    make_list = ["hvmodelsMaruti-Suzuki","hvmodelsHyundai","hvmodelsVolkswagen","hvmodelsTata",
                 "hvmodelsToyota","hvmodelsHonda","hvmodelsFord","hvmodelsChevrolet","hvmodelsMahindra",
                    "hvmodelsSkoda"]

    model_maruthi_list = ["mod_800","mod_A-Star","mod_Alto","mod_Swift","mod_Zen"]

    model_hyundai_list = ["mod_Verna","mod_Accent","mod_Elantra","mod_Santro","mod_Sonata"]
    
    model_volks_list = ["mod_Vento","mod_Beetle","mod_Passat","mod_Polo","mod_Jetta"]

    model_tata_list = ["mod_Safari","mod_Indigo","mod_Nano","mod_Manza","mod_Indica"]

    model_tayota_list = ["mod_Innova","mod_Fortuner","mod_Corolla","mod_Altis","mod_Camry"]

    model_honda_list = ["mod_Accord","mod_Amaze","mod_Civic","mod_City","mod_CR-V"]  

    model_ford_list = ["mod_Fusion","mod_EcoSport","mod_Endeavour","mod_Ikon","mod_Fiesta"]  

    model_chevro_list = ["mod_Aveo","mod_Aveo-Old","mod_Aveo-U-VA","mod_Captiva","mod_Enjoy"]

    model_mahindra_list = ["mod_Scorpio","mod_Bolero","mod_Xylo","mod_Jeep","mod_Quanto"]  

    model_skoda_list = ["mod_Fabia","mod_Laura","mod_Superb","mod_Octavia","mod_Rapid"]  

    for city in city_list:
        for make in make_list:
            makename = make.split("hvmodels")[1]
            if  make == "hvmodelsMaruti-Suzuki":
                for model in model_maruthi_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsHyundai":
                for model in model_hyundai_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsVolkswagen":
                for model in model_volks_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsTata":
                for model in model_tata_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsToyota":
                for model in model_tayota_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsHonda":
                for model in model_honda_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsFord":
                for model in model_ford_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsChevrolet":
                for model in model_chevro_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsMahindra":
                for model in model_mahindra_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()
            elif  make == "hvmodelsSkoda":
                for model in model_skoda_list:
                    modelname= model.split('mod_')[1]
                    data=Car_Master_Data(website_name="www.cartrade.com",city_id=city,city_name=city,make_id=make,make_name=makename,model_id=model,model_name=modelname).save()

    return HttpResponse("successfully created master data for cartrade website")


def cartrade_scrap(request):
    driver = webdriver.Firefox()
    master_data = Car_Master_Data.objects.all()
    for master in master_data:
        print master.city_id
        print master.make_id
        print master.model_id
        
        driver.get('http://www.cartrade.com/buy-used-cars')
        try:
            close_popup = driver.find_element_by_css_selector('div#selectcityfilm a.closebtn')
            time.sleep(1)
            close_popup.click()
        except:
            pass
        select_city = driver.find_element_by_css_selector('div.leftbar select#sortcity  option[value^="%s"]'%master.city_id)
        select_city.click()
        time.sleep(1)
        select_model = driver.find_element_by_css_selector('li#%s div.spclass span.rcircle'%master.make_id)
        select_model.click()
        time.sleep(1)
        model_select =driver.find_element_by_css_selector('ul#mklist.features li#hvmodelsMaruti-Suzuki.hvchild.open ul#chmodelsMaruti-Suzuki li label input#%s'%master.model_id)
        model_select.click()
        time.sleep(1)
        car_data_list_total_div = [element for element in driver.find_elements_by_css_selector('div#searchFilters div.btmMrg.carlistblk div.widgetBox1 ')]
        for data in car_data_list_total_div:
            try:
                title = data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.h2heading').text
                print title
            except:
                title = "Default Title"
                print title

            try:
                href = data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.h2heading a').get_attribute("href")
                print href
            except:
                href = "http://www.chevrolet.co.in/trailblazer-powerful-suv.html?cmp=4456906_9138324_1673028_124445889_296988365_0"

            try:
                price_car= price=data.find_element_by_css_selector('div.titleblk div.pull-left.carlistcont div.price div.pull-left strong.pull-left').text
                

                price_car_1 = int(price_car.replace(",",""))
                print price_car
                
                print 'price_car_1'
                print price_car_1
                print type(price_car_1)

            except:
                price_car = "3,50,000"
                
            scrollDown(driver, 1)
            time.sleep(3)
            try:
                image = data.find_element_by_css_selector('div.carimgblk a img').get_attribute("src")
                print image
            except:
                image = "http://imagecdn5.cartrade.com/img/300x225/lis/Maruti-Suzuki_A-Star_491097_20983_1_1435575807451.jpg"
                print image         
            year = title.split("(")[1].split(")")[0]
            print year
            time.sleep(1)
            CarDetails.objects.update_or_create(
                website_name="www.cartrade.com",
                city=master.city_id,
                car_make=master.make_name,
                car_model= master.model_name,
                price = price_car,
                model_year=year,
                car_title =title,
                car_href = href,
                car_image =image,
                )

    return HttpResponse("successfully scrapped cartrade")
=======

# Create your views here.
>>>>>>> master-dev
