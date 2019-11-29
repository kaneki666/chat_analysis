import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('E:\Programming\python\chat_analysis\chat_data.csv')

sender_value_counts = df['Sender'].value_counts() 
top_10_sender_value_counts = sender_value_counts.head(10) 
top_10_sender_value_counts.plot.barh(stacked=True) 
null_senders_df = df[df['Sender'].isnull()]
null_senders_df.head()

df['Letter_Count'] = df['Message'].apply(lambda s : len(s))
df['Word_Count'] = df['Message'].apply(lambda s : len(s.split(' ')))
df['Letter_Count'].sum(), df['Word_Count'].sum()

total_word_count_grouped_by_sender = df[['Sender', 'Word_Count']].groupby('Sender').sum()
sorted_total_word_count_grouped_by_sender = total_word_count_grouped_by_sender.sort_values('Word_Count', ascending=False)
top_10_sorted_total_word_count_grouped_by_sender = sorted_total_word_count_grouped_by_sender.head(10)
top_10_sorted_total_word_count_grouped_by_sender.plot.barh()
plt.xlabel('Number of Words')
plt.ylabel('Senders')

plt.figure(figsize=(15, 2))
word_count_value_counts = df['Word_Count'].value_counts()
top_40_word_count_value_counts = word_count_value_counts.head(40)
top_40_word_count_value_counts.plot.bar()
plt.xlabel('Word Count')
plt.ylabel('Frequency')
