from netmiko import ConnectHandler


router = {
    'device_type':'cisco_ios',
    'ip':'172.16.1.101',
    'username':'automation',
    'password':'automation',
    'secret':'cisco'
    }

conn = ConnectHandler(**router)
#user exec mode
print(conn.send_command('sh ip int brief'))
#privilege exec mode
print(conn.enable())
#global config mode

def Convert(string): 
    li = list(string.split("-")) 
    return li
sample=0
mystr = ""
for sample in range(1,100):
    mystr += "int loopback {0}-ip address 10.1.1.{0} 255.255.255.255-".format(str(sample))

cmd = Convert(mystr)
print(conn.send_config_set(cmd))
print(conn.send_command('sh ip int brief'))
print("Selamat anda sudah berhasil membuat Loopback")
