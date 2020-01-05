from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
from datetime import datetime
import requests

counter = 1
run_flag = RunFlag()

def handledata(found_data):

    mac = found_data[0]

#   mulla on kaks ruuvitagia niin ne tulee sit erikseen tässä
#
#   if found_data[0] == '00:00:00:00:00:00':
#       mac = 1
#   elif found_data[0] == '11:11:11:11:11:11':
#       mac = 2

    data = found_data[1]

    url = "/iot/sensordata.php"
    info = {'user': 'oma_käyttis', 'pass': 'oma_salasana', 'deviceid': mac, 'temperature': data['temperature'], 'humidity': data['humidity'], 'pressure': data['pressure']}
    r = requests.post(url=url, data=info)

    print(info)  # lähtevät tiedot
    print(r.text, r.status_code, r.reason)  # serverin vastaus

    global counter
    counter = counter - 1
    if counter <= 0:
        run_flag.running = False


mac = '22:22:22:22:22:22' #tähän oma ruuvitag mac-osoite

#macs = ['11:11:11:11:11:11','00:00:00:00:00:00']
RuuviTagSensor.get_datas(handledata, mac, run_flag) # jos 2 > niin tähän mac:n tilalle macs
