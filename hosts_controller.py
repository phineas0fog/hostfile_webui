import re


def _save(hosts):
    lines = []
    for host in hosts['hosts']:
        if host['active'] == True:
            active = ''
        else:
            active = '#'

        line = f"{active}{host['address']} {host['hostname']}\n"
        lines.append(line)

    with open('hosts', 'w') as f:
        f.writelines(lines)

def get_hosts():
    print('get hosts')
    with open('/etc/hosts') as f:
        raw_hosts = f.readlines()
        clean_hosts = []
        pattern = re.compile("^(#{0,1})([0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}) {1}(.*)")
        count = 0
        for host in raw_hosts:
            try:
                clean_hosts.append({
                    "address": pattern.match(host).group(2),
                    "hostname": pattern.match(host).group(3),
                    "active": True if pattern.match(host).group(1) == "" else False
                })
                count += 1
            except AttributeError:
                pass
    return {'count': count, 'hosts': clean_hosts}


def add_host(data):
    if 'address' in data and 'hostname' in data:
        hosts = get_hosts()
        hosts['hosts'].append(
            {
                'address': data['address'],
                'hostname': data['hostname'],
                'active': True
            }
        )
        _save(hosts)
        return 200
    else:
        return 301


if __name__ == '__main__':
    get_hosts()
