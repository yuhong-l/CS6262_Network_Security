import sys, json

# python cal_unique_connection.py alert_json.txt
try:
    snort_alert_json = sys.argv[1]
except:
    print ("Error")
    exit(-1)

comments = set()

attack_categories = ["DoS", "Bruteforce", "WebAttack", "Botnet"]

unique_connections = dict()
with open(snort_alert_json) as fr:
    for line in fr.readlines():
        alert_datum = json.loads(line)

        if alert_datum['msg'] not in attack_categories:
            comments.add("unknown message: " + alert_datum['msg'])
            continue

        if alert_datum['msg'] not in unique_connections.keys():
            unique_connections[alert_datum['msg']] = set()
        tmp_connection = alert_datum['src_ap'] + "-" + alert_datum['dst_ap']
        unique_connections[alert_datum['msg']].add(tmp_connection)

for (key, value) in unique_connections.items():
    print("Attack type: %s, unique connections: %d" % (key, len(value)))
print ("Comments: ")
print (comments)

for key in unique_connections.keys():
    unique_connections[key] = list(unique_connections[key])
with open("connections.txt", "w") as f:
    json.dump(unique_connections, f)


