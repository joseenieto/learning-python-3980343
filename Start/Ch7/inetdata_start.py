# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#

import urllib.request

# open a connection to a URL using urllib2
web_url = urllib.request.urlopen("https://empresite.eleconomista.es/REPSOL-COMERCIALIZADORA-ELECTRICIDAD-GAS.html")

# get the result code and print it
print ("Result code:", web_url.getcode())

# read the data from the URL and print it
data = web_url.read()
print(data)

sample_file = open("empresite-example.html","w+")
sample_file.write(data.decode('utf-8'))
sample_file.close()