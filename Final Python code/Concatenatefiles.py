import json
new_list = []
seen = set()
for i in range(1,44):
    jsonfile = str(i)+".json"
    with open(jsonfile,'r') as jf:
        data = json.load(jf)
        for person in data:
            user = person['user']
            if user not in seen:
                seen.add(user)
                new_list.append(person)


output_file = 'final.json'
with open(output_file, 'w') as of:
    json.dump(new_list, of)