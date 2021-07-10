from netmiko import ConnectHandler
import os
import re

#masukkan semua list ip yang konfigurasi nya ingin di export 
#semua device harus memiliki username dan password yang sama
#jika ada lebih dari 1 ip . maka pisahkan dengan tanda , (koma)
listip = ["172.16.1.101"]

for ip in listip:
    print(ip)
    router = {
        'device_type':'cisco_ios',
        'ip':ip,
        'username':'automation', # isi username untuk login ssh
        'password':'automation', # isi password untuk login ssh 
        'secret':'cisco' # secret harus di inputkan , kecuali jika user privilege level 15 maka tidak perlu memasukkan secret lagi 
        }

    conn = ConnectHandler(**router)
    try:
        enable = conn.enable()
        print("Succesfully Connect")
        run_conf = conn.send_command('show running-config')
        # you can define path for saving file manually, or automatic select path
    
        hostname = re.search("hostname(.*)\s",run_conf).group(0).split(" ")
        namefile = ("exp_cfg-{}.txt".format(hostname[1].replace("\n","")))
        path = os.path.join(os.getcwd(), namefile)
        # path = os.path.join("C:\Python\Python37\myscipt", namefile) # jika ingin path penyimpanannya ditentukan sendiri bisa enable command ini 
        file = open(path, "w")
        file.write(run_conf)
        print(f"Succesfully Export Configuration, File already saved in {path}")

    except Exception as Err:
        print(Err)

