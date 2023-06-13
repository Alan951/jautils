import ipaddress

class IPUtils:

    @staticmethod
    def explode_ip(ip):
        ips = []

        if('-' in ip):
            start_ip, end_ip = ip.split('-')

            start_ip = ipaddress.IPv4Address(start_ip.strip())
            end_ip = ipaddress.IPv4Address(end_ip.strip())

            current_ip = start_ip
            while current_ip <= end_ip:
                ips.append(str(current_ip))
                current_ip += 1  # Pasamos a la siguiente dirección IP
        elif('/' in ip):
            network = ipaddress.IPv4Network(ip.strip(), False)
            [ips.append(str(ip)) for ip in network.hosts()]
        else:
            return ip.strip()

        return ips