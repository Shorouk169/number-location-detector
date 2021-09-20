import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier



number = "(add your phone number here in this string)" 
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))
