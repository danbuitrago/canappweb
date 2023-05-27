import serial.tools.list_ports

ports=serial.tools.list_ports.comports()

serialInst=serial.Serial()

portList=[]

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

val=input('Select Port: COM')
print(val)

for x in range (0,len(portList)):
    if portList[x].startswith('COM'+str(val)):
        portVar='COM'+str(val)
        print(portList[x])

serialInst.baudrate=115200
serialInst.port=portVar
serialInst.open()

while True:
    if serialInst.in_waiting:
        packet=serialInst.readline()
        #capturar()  # capturar datos para poner en archivo txt
        #mostrar los datos del archivo
        print(packet.decode('utf-8'))