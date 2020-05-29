We first have to download the datasets:

Fake Media:
    Add dataset_train.csv to the FakeMedia/ directory.

COCO:
    From http://cocodataset.org/#download download "http://cocodataset.org/#download", unzip, and put in the coco_captions/ directory.

NLVR2:
    From https://github.com/lil-lab/nlvr/tree/master/nlvr2/data download "train.json" and put in the nlvr2/ directory.

GQA:
    From https://cs.stanford.edu/people/dorarad/gqa/download.html download questions, unzip, and put questions1.3 in the GQA directory.

VQA:
    From https://visualqa.org/download.html download "Training questions 2017 v2.0*", unzip, and put the json into the VQA directory.

In each of the directories, there should be an extract_captions.py script that should produce the output files line by line.

Run analyze_datasets.py to get caption lengths/percentage graphs/files.
