import urllib.request
url = input("Please enter the desired website URL: ")
print("Source Code:")
print(urllib.request.urlopen(url).read())
