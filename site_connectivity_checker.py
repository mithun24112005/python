# use urllib.request to get the data from the url
# write a function that take url and returns responce

import urllib.request as urllib

def main(url):
    print("checking conectivity  ")
    response=urllib.urlopen(url)
    print(f"connected to {url} ")
    print("the responce code was: ",response.getcode())

print("this is a site connectivity checker program")
inp_url=input("input the url of the site u want to check: ")

main(inp_url)
