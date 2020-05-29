'''
This python script reads the captions from the dataset and converts them into a format
where each caption is on a different line.
'''

import pandas as pd
import argparse
import random

parser = argparse.ArgumentParser(description=
    'Takes captions in dataset and produces an output file formatted one caption per line.')
parser.add_argument('-i', '--input', type=str, help="Path to input file.")
parser.add_argument('-e', '--is_eval', type=bool, help="Whether the input is an eval file, in which case we don't include prefixes.", default=False)
parser.add_argument('-o', '--output', type=str, help="Path to output file.")
parser.add_argument('-l','--length_thresholds', type=int, help='Minimum, maximum number of words in a caption to save.', default=[0,200], nargs=2)
parser.add_argument('-p', '--small_batch_proportion', type=float, help='proportion of lines we wish to keep to generate a small batch', default=1.0)
args = parser.parse_args()

data = pd.read_csv(args.input)
output = open(args.output, "w+")
len_threshs = args.length_thresholds

caption_columns = ['intent_2', 'disinfo_2', 'disinfo_1',
       'mp2_feel_1', 'mp1_mislead_1', 'mp3_mislead_1', 
       'mp2_feel_0', 'mp1_feel_1', 'implications_2', 'edited_title',
       'input_title', 'mp1_feel_2', 'mp3_mislead_0', 'mp1_mislead_2',
       'mp2_mislead_0', 'mp1_mislead_0', 'intent_0',
       'mp2_mislead_1', 'intent_1', 'implications_0',
       'mp2_mislead_2', 'mp3_feel_2', 'disinfo_0', 'implications_1',
       'mp3_mislead_2', 'mp1_feel_0', 'mp3_feel_0', 'mp3_feel_1',
       'mp2_feel_2']

prefixes = ['MP1 would ' 
            'Someone might mistakenly believe that MP1 ',
            'MP2 would ',
            'Someone might mistakenly believe that MP2 ',
            'MP3 would ',
            'Someone might mistakenly believe that MP3 ',
            'Editor created this edit to ',
            'This edit could potentially be used to ',
            'In regards to the edit as a whole, this edit might mislead someone into believing that '
            ]

prefixes_to_prefix_len = {}
for prefix in prefixes:
    prefixes_to_prefix_len[prefix] = len(prefix)

for col in caption_columns:
    prefix_to_cut = None
    caps_in_col = []
    for caption in data[col]:
        if caption != '{}':
            if random.random() <= args.small_batch_proportion: # for creating smaller batches
                if args.is_eval: # we keep track of all prefixes in all columns to not include them in the final output
                    for prefix in prefixes:
                        if str(caption).find(prefix) == 0:
                            caption_without_prefix = str(caption)[prefixes_to_prefix_len[prefix]:]
                            if len(caption_without_prefix.split(' ')) > 1: # One word captions mess with perplexity calculations
                                output.write('{cap}\n'.format(cap=caption_without_prefix))
                else:
                    if len_threshs[1] >= len(str(caption).split(' ')) >= len_threshs[0]:
                        output.write('{cap}\n'.format(cap=str(caption)))
output.close()