# BOUSSOURA Mohamed Cherif , Boufarik-Blida-ALGERIA , 11:24 pm 04-12-2020

# This code run with Python2

import requests
import argparse
import json

    
parser = argparse.ArgumentParser()
parser.add_argument("-i","--ipaddress",help="IP address to track")
args = parser.parse_args()
ip = args.ipaddress
url = "http://ip-api.com/json/"+ip
response = requests.get(url)
data = json.loads(response.content)

#print(data)

print("\t[*] IP\t\t",data["query"])
print("\t[*] CITY\t\t",data["city"])
print("\t[*] ISP\t\t",data["isp"])
print("\t[*] LOC\t\t",data["country"])
print("\t[*] REG\t\t",data["regionName"])
print("\t[*] TIME\t\t",data["timezone"])
print("\t[*] ZIP\t\t",data["zip"])
print("\t[*] LAT\t\t",data["lat"])
print("\t[*] LON\t\t",data["lon"])


# Test : python ip-geo.py -i google.com
