from DateMonthYear import DateMonthYear
from Sender import Sender 
from fullMessageDivide import fullMessageDivide
import pandas as pd
import matplotlib.pyplot as plt

parsedData = [] 
chatPath = './group.txt' 
with open(chatPath, encoding="utf-8") as fp:
    fp.readline()
        
    messageBuffer = []
    date, time, author = None, None, None 
    
    while True:
        line = fp.readline() 
        if not line: 
            break
        line = line.strip() 
        if DateMonthYear(line): 
            if len(messageBuffer) > 0:
                parsedData.append([date, time, author, ' '.join(messageBuffer)]) 
            messageBuffer.clear() 
            date, time, author, message = fullMessageDivide(line) 
            messageBuffer.append(message)
        else:
            messageBuffer.append(line) 

print(parsedData)
df = pd.DataFrame(parsedData, columns=['Date', 'Time', 'Sender', 'Message'])
df.describe()

sender_value_counts = df['Sender'].value_counts() 
top_10_sender_value_counts = sender_value_counts.head(10) 
top_10_sender_value_counts.plot.barh(stacked=True) 
null_senders_df = df[df['Sender'].isnull()]
null_senders_df.head()

media_messages_df = df[df['Message'] == '<Media omitted>']
print(media_messages_df.head())

sender_media_messages_value_counts = media_messages_df['Sender'].value_counts()
top_10_sender_media_messages_value_counts = sender_media_messages_value_counts.head(10)
top_10_sender_media_messages_value_counts.plot.barh()

messages_df = df.drop(null_senders_df.index) 
messages_df = messages_df.drop(media_messages_df.index) 
messages_df.head()

messages_df['Letter_Count'] = messages_df['Message'].apply(lambda s : len(s))
messages_df['Word_Count'] = messages_df['Message'].apply(lambda s : len(s.split(' ')))
messages_df['Letter_Count'].sum(), messages_df['Word_Count'].sum()

total_word_count_grouped_by_sender = messages_df[['Sender', 'Word_Count']].groupby('Sender').sum()
sorted_total_word_count_grouped_by_sender = total_word_count_grouped_by_sender.sort_values('Word_Count', ascending=False)
top_10_sorted_total_word_count_grouped_by_sender = sorted_total_word_count_grouped_by_sender.head(10)
top_10_sorted_total_word_count_grouped_by_sender.plot.barh()
plt.xlabel('Number of Words')
plt.ylabel('Senders')

plt.figure(figsize=(15, 2))
word_count_value_counts = messages_df['Word_Count'].value_counts()
top_40_word_count_value_counts = word_count_value_counts.head(40)
top_40_word_count_value_counts.plot.bar()
plt.xlabel('Word Count')
plt.ylabel('Frequency')
