import json

output = open("nlvr2_train_line_by_line.txt", "w+")

with open('./train.json') as f:
    for line in f:
        data = json.loads(line)
        output.write('{cap}\n'.format(cap=data['sentence']))

output.close()
f.close()