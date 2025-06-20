import nmap

def scan_subnet(subnet):
    nm = nmap.PortScanner()
    print(f"Scanning {subnet}...")
    nm.scan(hosts=subnet, arguments='-p 554,81,8080,8000 --open')
    ip_list = []
    for host in nm.all_hosts():
        ip_list.append(host)
    return ip_list
  
