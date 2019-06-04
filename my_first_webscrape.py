# Get the library and html
from urllib.request import urlopen as uReq
# Lib to pass HTML text in python
from bs4 import BeautifulSoup as soup

# webscrape graphics cards off new egg or any website and is like having an online batabase/set
my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'
# open a connection, grab the web page and download import
uClient = uReq(my_url)
# dump the whole html page, offload the content into a variable
page_html = uClient.read()
# close connection
uClient.close()
# parse as html
page_soup = soup(page_html, "html.parser")
# see the header of the page example can traverse the html)
page_soup.h1
# find div with class called item-container (Grabs each product)
containers = page_soup.findAll("div", {"class" : "item-container"})
# find the length of the containers
len(containers)
# find the 1st one, save it in a variable to loop through common product properties 
# container = containers[0]
# example to get the first element as expected
# container.a
# get the image element in the form of a dictonary(my working example)
# container.img["title"]
# same but from the tutorial for the loop
for container in containers:
# save it in varable brand
   # brand = container.div.div.a.img["title"]
    # data structure of the object for title container 
    title_container = container.findAll("a", {"class":"item-title"})
    # inside an array of objects to get the text
    product_name = title_container[0].text
    # shipping, with the findAll function to get the class 
    shipping_container = container.findAll("li", {"class":"price-ship"})
    # strip() function to rid of all the spaces, new lines etc in the text
    shipping = shipping_container[0].text.strip()

    #print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)