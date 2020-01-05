#importoidaan ruuvitag_sensor
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag
#importoidaan datetime että nähdään aika
from datetime import datetime

counter = 1 #laskuri
run_flag = RunFlag()

def handle_data(found_data):

    mac = found_data[0] #ruuvitagin mac-osoite
    data = found_data[1]

    #ruuvitagin datan sensorit joista halutaan tietoa
    temp = data['temperature']
    hum = data['humidity']
    press = data['pressure']
    battery = data['battery']

    time = datetime.now() #aika

    #data stringinä
    tiedot = time.strftime('%d %m %Y, %H:%M'), 'lämpötila: ', temp, 'kosteus: ', hum, 'paine: ',press, 'akku: ', battery

    #saadun datan kirjoittaminen tekstitiedostoon
    with open('ruuvit.txt', 'a') as myfile:
        myfile.write( str(mac) + '\n' )
        myfile.write( str(tiedot) + '\n' )

    #printtaus konsoliin
    print('ruuvitag mac: ' + mac)
    print(tiedot)

    #get_data:n suorittamisen lopetus
    global counter
    counter = counter -1
    if counter < 0:
        run_flag.running = False

macs = ['111', '11']

# callback (macs-muuttujan ruuvitageille, run_flag laskurille) että saadaan get_datan suoritus
# pysäytettyä halutun ajan päästä (tässä tapauksessa kun ollaan saatu 1 kerran molemmilta
# ruuvitageilta datat)

RuuviTagSensor.get_datas(handle_data, macs, run_flag)
