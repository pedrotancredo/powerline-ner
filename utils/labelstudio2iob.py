#%%
import re
import json
import pandas as pd

    #%%
    # Read the contents of the JSON file
def labelstudio2iob(data):
    # input_path = '../recursos/anotacao.json'
    # with open(input_path, encoding='utf-8') as file:
    #     data = json.load(file)

    # Extract the values of 'sentence' and 'label'
    final_df = pd.DataFrame()
    for item in data:
        sentence_id = item['id']
        sentence = item['t_model_audio']
        #if item['label'] does not exist pass
        if 'label' not in item:
            continue
        
        labels = item['label']
        print(sentence)
        # print('----')

        # Define intervalos principais

        labels.sort(key=lambda x: x['start'])

        intervals = []

        # Iterate over each interval in the sorted teste list
        for interval in labels:
            # Check if the current interval is contained within any of the intervals already in the result list
            is_contained = False
            for existing_interval in intervals:
                if existing_interval['start'] <= interval['start'] and existing_interval['end'] >= interval['end']:
                    is_contained = True
                    break

            # If the current interval is not contained within any existing intervals, add it to the result list
            if not is_contained:
                intervals.append(interval)

        # Rewrite labels by get 1st list element
        for interval in intervals:
            interval['labels'] = interval['labels'][0]
            interval['sentence_id'] = sentence_id


        # Fill the intervals considering the string start at 0 and end at len(sentence)
        # Initialize the list of new intervals
        new_intervals = []

        # Set the start of the first new interval
        if intervals[0]['start'] != 0:
            end = intervals[0]['start']
            new_intervals.append({'start' : 0,
                                'end': end,
                                'text': sentence[0:end],
                                'labels': None,
                                'sentence_id' : sentence_id})

        # Create new intervals
        for i in range(len(intervals)-1):
            # Add the new interval to the list
            start = intervals[i]['end']
            end = intervals[i+1]['start']
            if start < end:
                new_intervals.append({'start' : start,
                                    'end' : end,
                                    'text' : sentence[start:end],
                                    'labels' : None,
                                    'sentence_id' : sentence_id
                                    })

        # Add the last new interval
        if intervals[-1]['end'] < len(sentence):
            start = intervals[-1]['end']
            new_intervals.append({'start' : start,
                                'end' : len(sentence),
                                'text' : sentence[start:len(sentence)],
                                'labels' : None,
                                'sentence_id' : sentence_id
                                })

        # Append the original intervals
        new_intervals.extend(intervals)

        # Sort the intervals
        # new_intervals.sort()

        df = pd.DataFrame(new_intervals).sort_values(by=['start']).reset_index(drop=True)
        #Filter where df equals ' ' and labels equals None
        df = df[(df['text'] != ' ') & (df['labels'] != None)]


        # Iterate over each row in the dataframe
        new_data = []
        for _, row in df.iterrows():
            text = row['text']
            labels = row['labels']
            sentence_id = row['sentence_id']

            # Split the text into words and punctuation using regular expression
            words = re.findall(r'\w+|[^\w\s]', text)

            # Assign IOB tags to each word
            iob_tags = []
            for i, word in enumerate(words):
                if labels is None:
                    iob_tags.append('O')
                elif i == 0:
                    iob_tags.append('B-' + labels)
                else:
                    iob_tags.append('I-' + labels)

            # Create a dictionary for each word with the word, IOB tag, and sentence ID
            for word, iob_tag in zip(words, iob_tags):
                new_data.append({'word': word, 'iob_tag': iob_tag, 'sentence_id': sentence_id})

        # Create a new dataframe from the list of dictionaries
        new_df = pd.DataFrame(new_data).reset_index(drop=True)

        # Rename columns to '0', '1', and 'sentence'
        new_df = new_df.rename(columns={'word': '0', 'iob_tag': '1', 'sentence_id': 'sentence'})

        # Remove the index and reset the index
        new_df = new_df.reset_index(drop=True)

        # Append the new dataframe to the final dataframe
        final_df = pd.concat([final_df, new_df], ignore_index=True)
    return final_df


# %%
