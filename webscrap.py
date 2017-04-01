import requests
import re
from urlparse import urlparse
from bs4 import BeautifulSoup
from bs4 import NavigableString


url = raw_input("Enter All submissions page Url of Codechef problem ")

host = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(url))

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html,"html.parser")
print url

filehandling = open("codechefSolutions.txt","w")

rowEntries = soup.find(class_='dataTable').tbody.find_all("tr")

count = 0
for eachRow in rowEntries:
	criteria = eachRow.find("td",{"width" : "51"})
	if  criteria.img.contents and (criteria.img.contents[1]=="100"):
		count+=1
		filehandling.write(str(count)+":\n")
		filehandling.write(host+eachRow.find("a",{"href":re.compile("^/viewsolution/"),"target":"_blank"})["href"]+"\n")


td = soup.find('td',align='right')

while ((td is not None) and (td.a is not None) and (td.a['href'] is not None)):
	currentURL  = host+td.a['href']
	print currentURL
	newRespone = requests.get(currentURL)
	soup = BeautifulSoup(newRespone.content,"html.parser")
	td = soup.find('td',align='right')
	rowEntries = soup.find(class_='dataTable').tbody.find_all("tr")
	for eachRow in rowEntries:
		criteria = eachRow.find("td",{"width" : "51"})
		if  criteria.img.contents and (criteria.img.contents[1]=="100"):
			count+=1
			filehandling.write(str(count)+":\n")
			filehandling.write(host+eachRow.find("a",{"href":re.compile("^/viewsolution/"),"target":"_blank"})["href"]+"\n")
else:
	print "END"

filehandling.close()