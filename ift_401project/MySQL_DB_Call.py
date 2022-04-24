
import mysql.connector
from shodan import Shodan
import json, sys, socket, hashlib

mydb = mysql.connector.connect(
  host="ift401-database.cdsmd9gvxogj.us-east-2.rds.amazonaws.com",
  user="IFT401Lead",
  password="ASUCapStone!",
  database="ApplicationDB"
)

print(mydb)

APIKEY = "DYHEiYQK5lcJvOxGQbsOD26F9QxjkoPY"

ShodanAPI = Shodan(APIKEY)

mycursor = mydb.cursor()


Host = socket.gethostbyname(sys.argv[2])
Results = ShodanAPI.host(Host)

UserEmail = sys.argv[1]
query = sys.argv[2]
hostnames = str(Results['hostnames'])
ip_str = str(Results['ip_str'])
org = str(Results['org'])
ports = str(Results['ports'])
last_update = str(Results['last_update'])

#Create ID hash
HashString = UserEmail + query
ID = hashlib.md5(HashString.encode()).hexdigest()

data = (ID, UserEmail, query, hostnames, ip_str, org, ports, last_update)


sql = (
    "INSERT INTO HostTest (ID, UserEmail, query, hostnames, ip_str, org, ports, last_update) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
)

mycursor.execute(sql, data)
#OR

#val = [(Data1-1, Data1-2),(Data2-1, Data2-2)]
#mycursor.executemany(sql, val)

mydb.commit()
