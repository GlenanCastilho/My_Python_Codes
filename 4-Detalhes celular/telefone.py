import phonenumbers
from phonenumbers import geocoder, carrier

phoneNumer = phonenumbers.parse("+5555555555555")

Carrier = carrier.name_for_number(phoneNumer, 'pt-br')

Region = geocoder.description_for_number(phoneNumer, 'pt-br')

print("A operadora é: " + Carrier)
print("O estado é: " + Region)
