import phonenumbers

number1 ="+916385331701"
number ="+971507914424"
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number1, "CH")
print(geocoder.description_for_number(ch_number,"en"))