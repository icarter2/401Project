from shodan import Shodan
import requests
import sys
import json

APIKEY = "DYHEiYQK5lcJvOxGQbsOD26F9QxjkoPY"

ShodanAPI = Shodan(APIKEY)


#Dns Method Functions

def DomainInfo(Hostnames, Pages):
    results = {}
    for Host in Hostnames.split(','):
        r = requests.get("https://api.shodan.io/dns/domain/" + Host + "?key=" + APIKEY)
        results[Host] = r.text

    return results


def DNSResolve(Hostnames):
    r = requests.get("https://api.shodan.io/dns/resolve?hostnames=" + Hostnames + "&key=" + APIKEY)

    return json.loads(r.text)


def DNSReverse(IPs):
    r = requests.get("https://api.shodan.io/dns/reverse?ips=" + IPs + "&key=" + APIKEY)

    return json.loads(r.text)


# Shodan Scan Functions

def Ports():
    #returns ports searched by Shodan
    r = requests.get("https://api.shodan.io/shodan/ports?key=" + APIKEY)
    return r.text


def Protocols():
    #returns protocols used when searching by Shodan
    r = requests.get("https://api.shodan.io/shodan/protocols?key=" + APIKEY)
    return r.text


def BeginScan(IPs):
    response = ShodanAPI.scan(ips=IPs, force=False)
    return response


def ScanStatus(Pages):

    response = ShodanAPI.scans(page=Pages)
    return response


def ScanResults(ScanId):
    results = []
    for banner in ShodanAPI.search_cursor('scan:' + ScanId):
        results.append(banner)
        print(banner)
    return results

def QueryList():
    results = ShodanAPI.queries()
    return results

def HostInfo(IP):
    results = ShodanAPI.host(IP)
    return results


def Main():

    # Main Program options

    if sys.argv[1] == "DomainInfo":
        #Example here
        results = DomainInfo(sys.argv[2], sys.argv[3])
        print(results)
    elif sys.argv[1] == "DNSResolve":
        #Example here
        results = DNSResolve(sys.argv[2])
        print(results)
    elif sys.argv[1] == "DNSReverse":
        #Example here
        results = DNSReverse(sys.argv[2])
        print(results)
    elif sys.argv[1] == "Ports":
        #Example here
        results = Ports()
        print(results)
    elif sys.argv[1] == "Protocols":
        #Example here
        results = Protocols()
        print(results)
    elif sys.argv[1] == "BeginScan":
        #Example here
        results = BeginScan(sys.argv[2])
        print(results)
    elif sys.argv[1] == "ScanStatus":
        #Example here
        results = ScanStatus(sys.argv[2])
        print(results)
    elif sys.argv[1] == "ScanResults":
        #Example here
        results = ScanResults(sys.argv[2])
        print(results)
    elif sys.argv[1] == "Queries":
        results = QueryList()
        print(results)
    elif sys.argv[1] == "HostInfo":
        results = HostInfo(sys.argv[2])
        print(results)
    else:
        print("Invalid Option")
        sys.exit()


Main()
