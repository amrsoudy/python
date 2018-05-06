#ex4
import requests
url = "http://www.androidquebec.com/wp-content/uploads/2010/11/contacts.json"
respnse = requests.get(url)
data=respnse.json()
print(data)