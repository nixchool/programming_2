#Subdomain Finder
import requests

''' The function takes website name from user then 
    check availability (status_code) of the subdomain  '''

def req_res(url):
    try:
        return requests.get("https://"+url)
    except requests.exceptions.ConnectionError as conn_error:
        pass
    

#input() takes target name from user
target = input("Enter the url of the website: ") 

#giving path to the filename in read mode
with open("C:\\Users\\Nischal KC\\Desktop\\programming02\\sub_domain.txt",'r') as sub_domains:
    for sub_domain in sub_domains:
        domain = sub_domain.strip()
        full_url = domain + '.' + target
        res =  req_res(full_url)

        if res:
            print("Subdomains {} exits".format(full_url))

