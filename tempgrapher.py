import time
import readxbee

print ('Starting Up Temperature Monitor')
temp_file = open('temp_graph.csv', 'a')

while True:
    try:
        ts = time.time()
        ts = int(ts * 1000)
        voltage = readxbee.get_voltage() 
        temp_file.write("{},{}\n".format(ts, voltage))
        print("{},{}".format(ts, voltage))
    except KeyboardInterrupt:
        break
    except:
        continue

temp_file.close()
print("Exiting")
