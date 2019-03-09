import re
from nltk.data import load
from collections import defaultdict
from collections import Counter

tagdict = load('help/tagsets/upenn_tagset.pickle')
tag_list = tagdict.keys()


def CleanFile():
    global final_list
    with open('SnapshotBROWN.pos.all.txt', 'r+') as f:
        data = f.readlines()
        mylist = []
        other_list = []
        for lines in data:
            if lines == '     (. .))\n':
                mylist.append(other_list)
                other_list = []
            else:
                other_list.append(lines)
        out_list = []
        pre_final_list = []
        for i in mylist:
            p = re.findall("[^-()\n.`':,$ ]+", (' '.join(i)))
            q = []
            for j in range(0, len(p)):
                if p[j] in tag_list:
                    q.extend([p[j], p[j + 1]])
            pre_final_list.append(q)

        file = open('tst.txt', 'w')
        for i in pre_final_list:
            file.write(' '.join(i))
            file.write('\n')
        file.close()
        final_list = [item for sublist in pre_final_list for item in sublist]

def HashOfHash():
    global hash_dict
    with open('BROWN-clean-pos.txt', 'r+') as f:
        data = f.read()
        data = data.split()
        word_dict= defaultdict(lambda: [])
        for i in range(0,len(data)-1):
            if data[i]  in tag_list:
                word_dict[data[i+1]].append(data[i])
        hash_dict = {k: dict(Counter(v)) for k, v in word_dict.items()}
        return ('Hash of Hashes from the clean file is given by: {} '.format(hash_dict))


def FrequentTags():
    global top_list
    HashOfHash()
    frequent_tags = defaultdict(int)
    for dicts in hash_dict.values():
        for i, j in dicts.items():
            frequent_tags[i] += j
    top_list = sorted(frequent_tags.items(), key=lambda kv: kv[1], reverse=True)
    return ('The top 20 Tags and their counts are given by: {}'.format(top_list[:20]))


def EvaluateTagger():
    CleanFile()
    FrequentTags()
    MostFrequent_tag = top_list[0][0]
    Evaluated_list = final_list
    Original_tags=[]
    Evaluated_tags =[]
    for i in range(0,len(Evaluated_list)):
        if Evaluated_list[i] in tag_list:
            Original_tags.append(Evaluated_list[i])
            Evaluated_tags.append(MostFrequent_tag)
            Evaluated_list[i]=MostFrequent_tag
    count = 0
    for i in range(0,len(Evaluated_tags)):
        if Evaluated_tags[i]==Original_tags[i]:
            count = count+1
    accuracy = (count/len(Evaluated_tags))*100
    return('The accuracy of the tagger is {}'.format(accuracy))

def main():
    CleanFile()
    print(HashOfHash())
    print('\n')
    print(FrequentTags())
    print('\n')
    print(EvaluateTagger())

main()