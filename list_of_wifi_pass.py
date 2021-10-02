"""
Hossein JALILI
List of WiFi and their passwords  
mehr 1400
list_of_wifi_pass.py
ver 1.0
"""
import subprocess
import platform
import getpass
import socket

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)
print("\nDeveloped by #ho3j ")
print("____________________________________")
try:
    print("os : \t\t\t",platform.system())
    print("Windows version : \t",platform.release())
    print("Windows 32/64bit : \t",platform.machine())
    print("Windows User : \t\t",getpass.getuser())
    print ("Host Name: \t\t {0}".format(host_name))
    print ("IP Address: \t\t {0}".format(ip_addr))
except:
    print("can not print Information of windows ")
print("____________________________________\n\n")
print("List of WiFi and their passwords \nthat are connected to your system  ")
print("***********************************")
try:
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

            try:
                print ("{:<20}   {:<}".format(i, results[0]))
            except IndexError:
                print ("{:<20}   {:<}".format(i, ""))

        except subprocess.CalledProcessError:
            print ("{:<20}   {:<}".format(i, "ENCODING ERROR"))
except:
    print("can not print Information of wifi and pass ")
print("***********************************")
i=input("'enter' for exit")