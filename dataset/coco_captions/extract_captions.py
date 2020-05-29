import json

output = open("coco_train_line_by_line.txt", "w+")

with open('./captions_train2014.json') as f:
    for line in f:
        data = json.loads(line)
        annotations = data['annotations']
        for annotation in annotations:
            output.write('{cap}\n'.format(cap=annotation['caption']))

output.close()
f.close()