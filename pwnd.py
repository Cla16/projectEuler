import hashlib
import sys
import requests
# Take in the password
user_input = str(sys.argv[1])
# Hash the password with sha1, the same as the database
password = hashlib.sha1(user_input.encode("utf-8")).hexdigest().upper()
# The API's endpoint
api_ep = "https://api.pwnedpasswords.com/range/"
# Make a request to the API
r = requests.get(api_ep + password[0:5])
# Split up the requests
hashes = r.text.split("\r\n")
found = False
# Let's clean up the hashes and get rid of extra \r's
for i in range(len(hashes)):
    hashes[i] = hashes[i].split(":")
    if password[0:5] + hashes[i][0] == password:
        print(user_input + " was found " + hashes[i][1] + " time(s).")
        found = True
if not found:
    print(user_input + " was not found in the database.")
