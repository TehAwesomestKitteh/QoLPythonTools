from colorama import Fore
import urllib3
import re
import os

os.system('color')

print(Fore.YELLOW)
print("Imgur Link Bruteforcer by TehAwesomestKitteh")
print(Fore.CYAN + "Bruteforce an image code and find which ones are valid. Supports one unknown (because if you need more than one, then it's better to just get a better data scraper than this script I made)")
print(Fore.GREEN)
to_test = input("Enter the image code. _ for the unknown symbol: ")

valid_charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

hits = 0

# Error catching block for debugging
try:
  if len(re.findall(r"[^a-zA-Z0-9]_", to_test)) > 0:
    print(Fore.RED)
    print("Invalid image code!")

  if len(re.findall(r"_", to_test)) != 1:
    print(Fore.RED)
    print("Only one unknown is allowed!")
  
  http = urllib3.PoolManager()
  
  print(Fore.CYAN + "Bruteforcing https://i.imgur.com/" + to_test + ".png")
  for valid_char in valid_charset:
    test_url = re.sub(r"_", valid_char, to_test)
    test_url = "https://i.imgur.com/" + str(test_url) + ".png"
    WebObject = http.request("GET", test_url);
    if WebObject.geturl() != test_url:
      print(Fore.YELLOW + "Redirected. Got: " + WebObject.geturl())
    elif WebObject.status == 200 or WebObject.status == 304 or WebObject.status == 302:
      print(Fore.GREEN + str(test_url) + " is valid [" + str(WebObject.status) + "]")
      hits += 1
    else:
      print(Fore.RED + str(test_url) + " is invalid [" + str(WebObject.status) + "]")
    
except Exception as e:
    print(Fore.RED)
    print(str(e))

print(Fore.YELLOW)
input("Bruteforcer done, Press Enter to Continue")