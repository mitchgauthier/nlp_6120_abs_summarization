from tqdm import tqdm
import os
import pandas as pd

path = "/Users/apple/Downloads/BBC News Summary"



Articles = []
Summaries = []
Titles = []


for root, dirs, files in tqdm(os.walk(path)):
    for file in files:
        if 'txt' in file:
            if os.path.isfile(root + '/' + file):
                if 'Summaries' in (root + '/' + file):
                    with open(root + '/' + file, 'r', errors='ignore') as f:
                        summary = ''.join([line.rstrip() for line in f.readlines()])
                        Summaries.append(summary)
                        f.close()
                else:
                    with open(root + '/' + file, 'r', errors='ignore') as f:
                        article = []
                        for n, line in enumerate(f.readlines()):
                            if n == 0:
                                title = line.rstrip()
                                Titles.append(title)
                            elif not line == '\n':
                                article.append(line.rstrip('\n'))
                        article = ' '.join(article)
                        Articles.append(article)
                        f.close()

print(len(Articles), len(Titles), len(Summaries))



# sen = Articles[0].split('.')
# lead_1 = sen[0] + '.'
# print(lead_1)
# lead_3 = '.'.join(sen[:3]) + '.'
# print(lead_3)

lead_1 = []
lead_3 = []
for art in Articles:
    sep_sen = art.split('.')
    lead_1.append(sep_sen[0] + '.')
    lead_3.append('.'.join(sep_sen[:3]) + '.')

# print(lead_3[:3])
# print(lead_1[:3])

data = pd.DataFrame({'Title': Titles, 'Article': Articles, 'Summary': Summaries, 'Lead-1': lead_1, 'Lead-3': lead_3})
# print(data.head(3))

data.to_csv(r'bbc_news_and_summary.csv', index=False)