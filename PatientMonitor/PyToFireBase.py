import urllib.request
import urllib.error
import json

def update(pt1 , pt2):
    Patient = {
    "patient1" : pt1 ,
    "patient2" : pt2
    # add patients here and change the number of parameters
        }
    json_data = json.dumps(Patient).encode()
##    "https://computernetworkproject-e3955.firebaseio.com/"  Firebase Node Url
    request = urllib.request.Request("https://computernetworkproject-e3955.firebaseio.com/Patient.json", data=json_data, method="PATCH")
    
    try:
        loader = urllib.request.urlopen(request)
    except Exception as e:
        print(e)
    else:
        print(loader.read())
   


