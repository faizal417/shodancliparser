# importing the modules

import re
import json
from pprint import pprint

#cat filename | xargs -P 1 -I % sh -c 'shodan cli scan %' : To scan multiple ip address

# result = open(input('filename: '),'r')
result = open("shodanresult", 'r')
result_content = str(result.read())
result.close()

# Divide the result into blocks
ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ip_address = ip.findall(result_content)
# print (ip)
# print (ip_address)

block = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
res_blocks = block.split(result_content)
res_blocks.pop(0)


# print (res_blocks)
# dic = {ip_address[i]: res_blocks[i] for i in range(len(ip_address))}
# print (dic)
# Find hostnames,city,Country,organisation,updated and ports from blocks

h = []
count=0
for i, block in enumerate(res_blocks):
    obj = {
        "ip":"",
        "hostname": "",
        "City": "",
        "Country": "",
        "Organization":  "",
        "Updated":                ""
    }
    # for block in res_blocks:
    hostnames = re.compile(r'Hostnames: \s+(.+)\n')
    hostname = hostnames.findall(block)
    obj["ip"]= ip_address[i]
    obj["hostname"] = hostname
    cities = re.compile(r'City: \s+(.+)\n')
    city = cities.findall(block)
    obj["City"] = city
    countries = re.compile(r'Country: \s+(.+)\n')
    country = countries.findall(block)
    obj["Country"] = country
    organisations = re.compile(r'Organization: \s+(.+)\n')
    organisation = organisations.findall(block)
    obj["Organization"] = organisation
    updates = re.compile(r'Updated: \s+(.+)\n')
    update = updates.findall(block)
    obj["Updated"] = update

    h.append(obj)
    # dic = {ip_address[i]: h[i] for i in range(len(ip_address))}
    # print (dic)

print(h)
# print(len(h))
# ports= re.compile(r'Ports:(.*)')
# port = (ports.findall(block))
# print (port)


# for i in ip_address:
#     for j in hostname:
#         final=[{'ip': i,'hostname':j}]
#         pretty_json = json.dumps(final, sort_keys=True, indent=4)
#         print (pretty_json)
# print (hostname)
# hostnames= re.compile(r'Hostnames: (.+)\n')
# matches = hostnames.findall(result_content)
# # print (matches)
# for host in matches:
#     print (host)
