# Site connectivity checker program

import urllib.request as urllib


def check_connection(url):
    print("Check Connection !!!")

    response = urllib.urlopen(url)
    print("Connection", url, "Successful")
    print("The response code was: ", response)


print("!! Check your desired site connection !!")
url = input("Enter the URL: ")

check_connection(url)
