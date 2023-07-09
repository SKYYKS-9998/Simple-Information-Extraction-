import nltk
import re
from collections import defaultdict
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

class infoExtract:
    def __init__(self, data_dict):
        print("Forming chunked sentences")
        self.ne_chunked_sent_dict = defaultdict(list)
        for cur_file in data_dict.keys():
            for text in data_dict[cur_file]:  # 对每个文件，均进行一遍关系抽取处理
                # 分句
                sentences = nltk.sent_tokenize(text)
                # 分词
                tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
                # 标注
                tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
                # 命名实体识别
                ne_chunked_sent = [nltk.ne_chunk(tagged) for tagged in tagged_sentences]
                self.ne_chunked_sent_dict[cur_file].append(ne_chunked_sent)

    def findOF(self):
        OF = re.compile(r'.*\bof\b.*')
        for cur_dir in self.ne_chunked_sent_dict.keys():
            for cur_file in self.ne_chunked_sent_dict[cur_dir]:
                for sent in cur_file:
                    for rel in nltk.sem.extract_rels('PER', 'ORG', sent, corpus='ace', pattern=OF):
                        print(nltk.sem.relextract.rtuple(rel))

    def findWin(self):
        WON = re.compile(r'.*\bw[io]n\b.*')
        for cur_dir in self.ne_chunked_sent_dict.keys():
            for cur_file in self.ne_chunked_sent_dict[cur_dir]:
                for sent in cur_file:
                    for rel in nltk.sem.extract_rels('PER', 'ORG', sent, corpus='ace', pattern=WON):
                        print(nltk.sem.relextract.rtuple(rel))

    def findPresident(self):
        PE = re.compile(r'.*\bpresident\b.*')
        for cur_dir in self.ne_chunked_sent_dict.keys():
            for cur_file in self.ne_chunked_sent_dict[cur_dir]:
                for sent in cur_file:
                    for rel in nltk.sem.extract_rels('PER', 'ORG', sent, corpus='ace', pattern=PE):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('PER', 'GPE', sent, corpus='ace', pattern=PE):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('GPE', 'PER', sent, corpus='ace', pattern=PE):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('ORG', 'PER', sent, corpus='ace', pattern=PE):
                        print(nltk.sem.relextract.rtuple(rel))

    def findJoin(self):
        JN = re.compile(r'.*\bjoin\b.*|.*\bjoined\b.*|.*\bjoining\b.*')
        for cur_dir in self.ne_chunked_sent_dict.keys():
            for cur_file in self.ne_chunked_sent_dict[cur_dir]:
                for sent in cur_file:
                    for rel in nltk.sem.extract_rels('PER', 'ORG', sent, corpus='ace', pattern=JN):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('PER', 'GPE', sent, corpus='ace', pattern=JN):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('ORG', 'ORG', sent, corpus='ace', pattern=JN):
                        print(nltk.sem.relextract.rtuple(rel))

    def findDefeat(self):
        DF = re.compile(r'.*\bdefeat\b.*|.*\bdefeated\b.*')
        for cur_dir in self.ne_chunked_sent_dict.keys():
            for cur_file in self.ne_chunked_sent_dict[cur_dir]:
                for sent in cur_file:
                    for rel in nltk.sem.extract_rels('PER', 'PER', sent, corpus='ace', pattern=DF):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('GPE', 'GPE', sent, corpus='ace', pattern=DF):
                        print(nltk.sem.relextract.rtuple(rel))
                    for rel in nltk.sem.extract_rels('ORG', 'ORG', sent, corpus='ace', pattern=DF):
                        print(nltk.sem.relextract.rtuple(rel))
