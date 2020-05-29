import json
from os import listdir
from os.path import isfile, join
from tqdm import tqdm

onlyfiles = [f for f in listdir('./questions1.3/train_all_questions/') if isfile(join('./questions1.3/train_all_questions/', f))]


i = 0
for i in tqdm(range(len(onlyfiles))):
    output = open("".join(["GQA_train_line_by_line", str(i), ".txt"]), "w+")
    with open(''.join(['./questions1.3/train_all_questions/', onlyfiles[i]])) as f:
        for line in f:
            data = json.loads(line)
            for item in data:
                output.write('{cap}\n'.format(cap=data[item]['question']))
                output.write('{cap}\n'.format(cap=data[item]['fullAnswer']))
    f.close()
    output.close()

