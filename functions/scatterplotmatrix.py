import statistics
import plotnine
from plotnine import *
import pandas as pd

url = 'https://raw.githubusercontent.com/ablair00/FinalProject/main/data/5937P.csv'
df = pd.read_csv(url)

perfectsong_attributes = ['Danceability','Energy','Key','Loudness','Mode','Speechiness','Instrumentalness','Liveness','Valence','Tempo','Duration','Time_Signature']
perfectsong = pd.DataFrame(columns = perfectsong_attributes)
print(perfectsong)

perfectsong.at[0, 'Danceability'] = df['danceability'].mean()
perfectsong.at[0, 'Energy'] = df['energy'].mean()
perfectsong.at[0, 'Key'] = statistics.mode(df['key'])
perfectsong.at[0, 'Loudness'] = df['loudness'].mean()
perfectsong.at[0, 'Mode'] = statistics.mode(df['mode'])
perfectsong.at[0, 'Speechiness'] = df['speechiness'].mean()
perfectsong.at[0, 'Instrumentalness'] = df['instrumentalness'].mean()
perfectsong.at[0, 'Liveness'] = df['liveness'].mean()
perfectsong.at[0, 'Valence'] = df['valence'].mean()
perfectsong.at[0, 'Tempo'] = df['tempo'].mean()
perfectsong.at[0, 'Duration'] = df['duration_ms'].mean()
perfectsong.at[0, 'Time_Signature'] = statistics.mode(df['time_signature'])

print(perfectsong)



df=pd.concat([df, perfectsong], axis=0)


danceyplot = (ggplot(df, aes(x='duration_ms',y='danceability',color='factor(key)', shape='factor(mode)', size='loudness'))
+ geom_point())
              
print(danceyplot)
