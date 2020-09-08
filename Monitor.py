from PatientMonitor.dataToPyFile import getData
from PatientMonitor.PyToFireBase import update
from time import sleep
print('Imported Functions Successfully..!!')

# Static IP should be used to nodemcu's
ip1 = '10.24.63.48'  # input('Enter Patient - 1 IP adress : ')
ip2 = '10.24.61.74'  # input('Enter Patient - 2 IP adress : ')
url1 = 'http://' + ip1 + '/'
url2 = 'http://' + ip2 + '/'

while True:
    pt1 = getData(url1)
    pt2 = getData(url2)
    print(f'Patient 1 : {pt1}')
#     update(pt1)
    print(f'Patient 2 : {pt2}')
    update(pt1, pt2) # To update more sensor readings increase parameters and also make suitable changes in imported file
    sleep(1)
    

#http://10.24.59.18/
#http://10.24.61.74/
