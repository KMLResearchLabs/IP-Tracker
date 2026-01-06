import requests
#pip install requests

def geoip(ip):
    url = f"http://ip-api.com/json/{ip}"
    r = requests.get(url).json()

    if r['status'] == 'success':
        answer = (
            "\n"
            f"=== <GEO IP> ===\n"
            + "-" * 40 + "\n"  
            f"[+] Consulted IP: {r["query"]}\n"
            f"[+] Country: {r["country"]}\n"
            f"[+] Region: {r["regionName"]}\n"
            f"[+] City: {r["city"]}\n"
            f"[+] Latitude: {r["lat"]}\n"
            f"[+] Longitude: {r["lon"]}\n"
            f"[+] Provider: {r["isp"]}\n"
            f"[+] Google link: https://www.google.com/maps/@{r["lat"]},{r["lon"]},20z\n"
            + "-" * 40
        )
        return answer
    else:
        return print(f"[ERROR] Check if the IP is right, if it is, something goed wrong")

target_ip = str(input("\n>>> Type the IP: ")).strip()
request = geoip(target_ip)
print(request)