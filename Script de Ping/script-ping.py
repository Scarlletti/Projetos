import subprocess

def testarping(host):
    resultado = subprocess.run(["ping", host], stdout=subprocess.DEVNULL)
    
    if resultado.returncode == 0:
        return True
    else:
        return False


ips = input("Digite os hosts separados por vírgula: ")
hosts = ips.split(",")

# remove espaços extras de cada host
hosts_limpos = []
for host in hosts:
    hosts_limpos.append(host.strip())


print("Host | Status")

for host in hosts_limpos:
    status = testarping(host)

    if status == True:
        status_texto = "UP"
    else:
        status_texto = "DOWN"

    print(f"{host} | {status_texto}")
