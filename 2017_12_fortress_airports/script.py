#
# These are only codesnippets from the data to generate the original posts. Outputs are json dumps
# used for the Google Charts API in the blog post. Static charts can easily be generated via matplotlib
#

from json import dumps
import pandas as pd

# load data
filename="data.csv" 
df=pd.read_csv(filename)

# create output for first chart
nr=15
l=df[['apt','depPct']][:15].values.tolist()
idx=0
for r in l:
    r[1]=round(r[1]/100,3)
    r.append(df['iata'][idx])
    idx+=1
dumps(l)


#How many airports each airline has with >50% share at the airport? (second chart)
airl={}
for a in aptSorted:
    if a[1]['depPct']>0.5:
        if a[1]['iata'] not in airl:
                airl[a[1]['iata']]=0
        airl[a[1]['iata']]+=1

airldf=pd.DataFrame(list(airl.items()))
airldf.columns=['airline','cnt']
airldf.sort_values(['cnt'],ascending=[False],inplace=True)
l=airldf[['airline','cnt']][:9].values.tolist()
dumps(l)
