import json
from os import listdir
from os.path import isfile, join
from tqdm import tqdm
from matplotlib import pyplot as plt
import seaborn

seaborn.set()

FakeMedia_files = [join('./FakeMedia/', f) for f in listdir('./FakeMedia/') if f.find('line_by_line') != -1 and isfile(join('./FakeMedia/', f))]
coco_files = [join('./coco_captions/', f) for f in listdir('./coco_captions/') if f.find('line_by_line') != -1 and isfile(join('./coco_captions/', f))]
VQA_files = [join('./VQA/', f) for f in listdir('./VQA/') if f.find('line_by_line') != -1 and isfile(join('./VQA/', f))]
GQA_files = [join('./GQA/', f) for f in listdir('./GQA/') if f.find('line_by_line') != -1 and isfile(join('./GQA/', f))]
nlvr2_files = [join('./nlvr2/', f) for f in listdir('./nlvr2/') if f.find('line_by_line') != -1 and isfile(join('./nlvr2/', f))]


def get_word_len_percentages(files):
    lines = []
    total_captions = 0
    len_counts = {}
    for file_path in files:
        f = open(file_path, 'r')
        for line in f:
            tokens = line.split(' ')
            len_counts[len(tokens)] = len_counts.get(len(tokens), 0) + 1
            total_captions += 1
    
    for k,v in len_counts.items():
        len_counts[k] /= total_captions

    lens = []
    percentages = []
    for kv in sorted(len_counts.items()):
        lens.append(kv[0])
        percentages.append(kv[1])
    return (lens, percentages)

def write_percentages_to_csv(lengths, percentages, filename):
    output = open(filename, 'w+')
    output.write('length,percentage\n')
    for pair in zip(lengths, percentages):
        output.write('{len},{per}\n'.format(len=pair[0], per=pair[1]))
    output.close()

print('Reading in Fake Media captions...')
FakeMedia_percentages = get_word_len_percentages(FakeMedia_files)
print('Reading in COCO captions...')
coco_percentages = get_word_len_percentages(coco_files)
print('Reading in VQA captions...')
VQA_percentages = get_word_len_percentages(VQA_files)
print('Reading in GQA captions...')
GQA_percentages = get_word_len_percentages(GQA_files)
print('Reading in nlvr2 captions...')
nlvr2_percentages = get_word_len_percentages(nlvr2_files)

write_percentages_to_csv(FakeMedia_percentages[0], FakeMedia_percentages[1], 'fake_media_length_percentages.csv')
write_percentages_to_csv(coco_percentages[0], coco_percentages[1], 'coco_length_percentages.csv')
write_percentages_to_csv(VQA_percentages[0], VQA_percentages[1], 'vqa_length_percentages.csv')
write_percentages_to_csv(GQA_percentages[0], GQA_percentages[1], 'gqa_length_percentages.csv')
write_percentages_to_csv(nlvr2_percentages[0], nlvr2_percentages[1], 'nlvr2_length_percentages.csv')

plt.plot(FakeMedia_percentages[0], FakeMedia_percentages[1], label='Fake Media Dataset')
plt.plot(coco_percentages[0], coco_percentages[1], label='COCO Dataset')
plt.plot(VQA_percentages[0], VQA_percentages[1], label='VQA Dataset')
plt.plot(GQA_percentages[0], GQA_percentages[1], label='GQA Dataset')
plt.plot(nlvr2_percentages[0], nlvr2_percentages[1], label='Nlvr2 Dataset')
plt.xlabel('Caption/Annotation lengths')
plt.ylabel('% Caption/Annotations')
plt.legend()

plt.savefig('caption_annotation_lengths1.png')
plt.show()
