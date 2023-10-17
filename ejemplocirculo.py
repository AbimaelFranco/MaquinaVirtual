import sim
import numpy as np
def connect(port):
# Establece la conexión a VREP
# port debe coincidir con el puerto de conexión en VREP
# retorna el número de cliente o -1 si no puede establecer conexión
    sim.simxFinish(-1) # just in case, close all opened connections
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) # Conectarse
    if clientID == 0: print("conectado a", port)
    else: print("no se pudo conectar")
    return clientID
# Ponemos todo el código junto
# conectamos
clientID = connect(19997)
# obtenemos los manejadores
returnCode,handle=sim.simxGetObjectHandle(clientID,'Dummy',sim.simx_opmode_blocking)
dummy = handle
ret,joint3=sim.simxGetObjectHandle(clientID,'joint3',sim.simx_opmode_blocking)
print ("ret", ret, "handle", joint3)
ret,joint4=sim.simxGetObjectHandle(clientID,'joint4',sim.simx_opmode_blocking)
print ("ret", ret, "handle", joint4)

#objeto paint
#ret,nozzle=sim.simxGetObjectHandle(clientID,'PaintNozzle',sim.simx_opmode_blocking)
print ("ret", ret, "handle", joint4)


#enciendo paintnozzle


ret,outi,outf,outs,outb=sim.simxCallScriptFunction(clientID, 'PaintNozzle', sim.sim_scripttype_childscript, 'updatePainting', [], [], [], bytearray(), sim.simx_opmode_blocking);

#movemos


rango=np.arange(-30,30,0.5)
for x in rango:
    q3 = x* np.pi/180
    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_blocking)
    #print("code1",returnCode)
    q4 = (np.sqrt(900-(x*x)))*np.pi/180
    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4  , sim.simx_opmode_blocking)
    #print("code2",returnCode)
    print(x,q3,q4)
rango=np.arange(-30,30,0.5)
for x in rango:
    q3 = -x* np.pi/180
    returnCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_blocking)
    #print("code1",returnCode)
    q4 = -(np.sqrt(900-(x*x)))*np.pi/180
    returnCode = sim.simxSetJointTargetPosition(clientID, joint4, q4  , sim.simx_opmode_blocking)
    #print("code2",returnCode)
    print(x,q3,q4)