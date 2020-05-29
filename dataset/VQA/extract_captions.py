import json

import json

output = open("VQA_train_line_by_line.txt", "w+")

with open('./v2_OpenEnded_mscoco_train2014_questions.json') as f:
    for line in f:
        data = json.loads(line)
        for question in data['questions']:
            output.write('{cap}\n'.format(cap=question['question']))

output.close()
f.close()