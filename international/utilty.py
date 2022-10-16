from . import currencies
from coin.models import Coin
from .models import *
from django.db.models import Q # new






def addAirport():

    inputFile = open( 'international/airport-codes.csv','r',encoding='utf-8')
    import csv
    coutries  = Country.objects.all()
    cities  = City.objects.all()
    coutriesList = {}
    for country in coutries:
        coutriesList[country.Alpha_2] = country
    city_list = {}
    for city in cities:
        city_list[city.city] = city
    csv_data=csv.reader(inputFile, delimiter=',')
    next(csv_data)  # skip header
    #OSDI,large_airport,Damascus International Airport,2020,AS,SY,SY-DI,Damascus,OSDI,DAM,,"36.51559829711914, 33.4114990234375"

    for line in csv_data:
        try:


            ident          = line[0]


            airport_type   = line[1]
            name           = line[2]
            # elevation_ft   = line[3]
            # continent      = line[4]
            country = coutriesList.get(line[5].strip(),None)
            # print("country",country.id)
            if not country:
                country =Country(name_ar='',name_en='',Alpha_2=line[5].strip(),Alpha_3='',
                                        currency_alphabetic='',currency_name='',
                                        Arabic_Formal='')
                print("create objects " , country ,   line[2])
                country.save()
            iso_country    = country
            iso_region     = line[6]
            city           = city_list.get(line[7].strip(),None)
            if not city :
                city = City.objects.filter(city_ascii = line[7].strip()).first()
            if not city :
                city = City(city=line[7].strip(),city_ascii=line[7].strip(),
                    country=country,iso2="",
                    iso3=line[9].strip(),id =City.objects.all().count() )
                print("city objects " , country.name_en ,   line[7])
                city.save()
            municipality  = city

            # gps_code       = line[8]
            iata_code      = line[9]
            # local_code     = line[10]
            # coordinates    = line[11]
        except Exception as e:
            continue
        try:
            airPort = AirPort(ident=ident,airport_type=airport_type,name=name,
                                iso_country=iso_country,
                                iso_region=iso_region,municipality=municipality,iata_code=iata_code)
            airPort.save()
        except Exception as e:
            print("ERROR ",line,e)
            break
    inputFile.close()


def addCountryfromWorldcities():
    inputFile = open( 'international/worldcities.csv','r',encoding='utf-8')
    import csv

    csv_data=csv.reader(inputFile, delimiter=',')
    next(csv_data)  # skip header
    coutries  = Country.objects.all()
    coutriesList = []
    for country in coutries:
        coutriesList.append(country.name_en)
    for line in csv_data:
        if not line[5].strip() in coutriesList:
            coutriesList.append(line[5].strip())
            name_ar             = ''
            name_en             = line[5].strip()
            Alpha_2             = line[6].strip()
            Alpha_3             = line[7].strip()
            currency_alphabetic = ''
            currency_name       = ''
            Arabic_Formal       = ''
            # Capital             = ''
            # Dial                = ''
            try:
                country = Country(name_ar=name_ar,name_en=name_en,Alpha_2=Alpha_2,Alpha_3=Alpha_3,
                                    currency_alphabetic=currency_alphabetic,currency_name=currency_name,
                                    Arabic_Formal=Arabic_Formal)
                country.save()
            except Exception as e:
                print("ERROR",line,e)
    inputFile.close()





def AddCountrydetails():
    inputFile = open('international/country-codes.txt','r',encoding='utf-16')
    import csv

    #name_en             = line[5].strip()
    #Alpha_2             = line[6].strip()
    #Alpha_3             = line[7].strip()

    csv_data=csv.reader(inputFile, delimiter=',')
    next(csv_data)  # skip header
    for line in csv_data:
        country = Country.objects.filter(Q(name_en=line[1].strip())|Q(Alpha_3=line[3].strip())).first()
        if country :
            country.name_ar             = line[0]
            country.name_en             = line[1]
            country.Alpha_2             = line[2]
            country.Alpha_3             = line[3]
            country.currency_alphabetic = line[4]
            country.currency_name       = line[5]
            country.Arabic_Formal       = line[6]
            # country.Capital             = line[7]
            # country.Dial                = line[8]
            country.save()
    inputFile.close()




def addCities():

    inputFile = open( 'international/worldcities.csv','r',encoding='utf-8')
    import csv
    coutries  = Country.objects.all()
    coutriesList = {}
    for country in coutries:
        coutriesList[country.Alpha_3]= country
    csv_data=csv.reader(inputFile, delimiter=',')
    next(csv_data)  # skip header
    for line in csv_data:
        id         =  line[0]
        city       = line[1]
        city_ascii = line[2]
        # lat        = line[3]
        # lng        = line[4]
        country = coutriesList.get(line[7].strip(),None)
        iso2       = line[6]
        iso3       = line[7]
        # admin_name = line[8]
        # capital    = line[9]
        # population = line[10]

        try:
            city = City(city=city,city_ascii=city_ascii,country=country,iso2=iso2,
                iso3=iso3,id =id )
            city.save()
        except Exception as e:
            print(line)
    inputFile.close()


def AddCurrency():
    for item in currencies.ISO_4217_CURRENCIES:#(932, 'ZWL Zimbabwean dollar A/10')
        id = item[0]
        short_title = item[1][:3]
        long_title = item[1][4:]
        try:
            cc =Coin(id=id,short_title=short_title,long_title=long_title)
            cc.save()
        except Exception as e:
            print(item)



if __name__ == '__main__':
    pass