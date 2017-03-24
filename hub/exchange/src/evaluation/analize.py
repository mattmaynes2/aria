import ast
with open('table.txt','r') as f:
    d=ast.literal_eval(f.read())

table=d['table']

for event,row in table.items():
    for decision in row['decisions']:
        bCount = row['behaviourCounts'][decision['behaviourId']]
        ratio = decision['count']/bCount
        if ratio > 0.8 :
            print("behaviour {} triggers {} on {} ".format(decision['behaviourId'], ast.literal_eval(decision['message'])['data'],event))
