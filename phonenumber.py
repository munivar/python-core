import phonenumbers 
from phonenumbers import timezone, geocoder, carrier

number = "+916353007994"
phone_number = phonenumbers.parse(number)
print("Country: " + geocoder.description_for_number(phone_number, "en"))
print("Carrier: " + carrier.name_for_number(phone_number,"en"))
print("Timezone: ", timezone.time_zones_for_number(phone_number))