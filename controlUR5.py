# URSoftware 5.1.1

# Echo client program
import socket
import time
#HOST = "169.254.52.193"    # The remote host
# HOST = "192.168.0.1"
HOST = "192.168.137.193"
PORT = 30002              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


# s.send (“set_digital_out(2,True)”.encode() + “\n”.encode())
# data = s.recv(1024)
# s.close()
# print (“Received”, repr(data))

time.sleep(0.05)
s.send ("set_digital_out(2,True)".encode() + "\n".encode())
time.sleep(0.1)

#movel(pose, a=1.2, v=0.25, t=0, r=0)
#s.send("movel([0.7,-0.9,1.4,0,0,3.14], a=1.2, v=0.25, t=0, r=0)".encode()+ "\n".encode())

time.sleep(2)

# s.send("movel([0.16,-0.9,1.4,0,0,3.14], a=1.2, v=0.25, t=0, r=0)".encode()+ "\n".encode())
# time.sleep(2)


#s.send("movel([0.2,0.3,0.5,0,0,3.14], a=1.2, v=0.25, t=0, r=0)".encode()+ "\n".encode())
s.send ("movej([-0.5405182705025187, -2.350330184112267, -1.316631037266588, -2.2775736604458237, 3.3528323423665642, -1.2291967454894914], a=1.3962634015954636, v=1.0471975511965976)".encode() + "\n".encode())

# s.send("get_actual_joint_positions()".encode()+ "\n".encode())
# #print(s.recvfrom(65565))
#
# # Trying to make sense of data I'm receiving
# bytes, addr = s.recvfrom(50)
# print(list(bytes))

time.sleep(2)
s.close()
