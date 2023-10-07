import pandas as pd
import re
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Utils:
    """
    Class to import dataset
    """
    def __init__(self) -> None:
        self.token = ToktokTokenizer()
        self.lemma = WordNetLemmatizer()
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words("english"))
        self.punct = '!"#$%&\'()*+,./:;<=>?@[\\]^`{|}~0123456789'
        self.tags_features = pd.read_csv("../data/raw/freq_words.csv", usecols = ['Tag'])

    def dataset_importer(self, file_name, data_column):
        "Imports the mentioned csv file and converts the data column to desired data type"
        raw_df = pd.read_csv(file_name, low_memory=False)
        raw_df = raw_df.drop_duplicates(subset='Id', keep='first')
        raw_df = raw_df[raw_df.Score >= 0]
        raw_df[data_column] = raw_df[data_column].astype(str)
        raw_df.to_csv("../data/raw/raw_with_score_gt_zero.csv", index=False)
        return raw_df
    
    def remove_code_segments(self, df):
        # Removing Code segments
        for index_label, row_series in df.iterrows():
            soup = BeautifulSoup(df.at[index_label, 'Body'], "html.parser")
            for tag in soup.find_all(['pre', 'blockquote', 'code']):
                tag.replaceWith('')
            df.at[index_label , 'Body'] = soup.get_text()
        return df


    def clean_text(self, text):
        # Clean Text
        text = text.lower()
        text = re.sub(r"what's", "what is ", text)
        text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"can't", "can not ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)
        text = re.sub(r"\'scuse", " excuse ", text)
        text = re.sub(r"\'\n", " ", text)
        text = re.sub(r"\r", " ", text)
        text = re.sub(r"<td>", " ", text)
        text = re.sub(r"</td>", " ", text)
        text = re.sub(r"<tr>", " ", text)
        text = re.sub(r"</tr>", " ", text)
        text = re.sub(r"\'\xa0", " ", text)
        text = re.sub('\s+', ' ', text)
        text = text.strip(' ')
        return text
    
    def remove_emoji(self, text):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags 
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    
    def strip_list_noempty(self, mylist):
        newlist = (item.strip() if hasattr(item, 'strip') else item for item in mylist)
        return [item for item in newlist if item != '']
    
    def clean_punct(self, text): 
        words=self.token.tokenize(text)
        punctuation_filtered = []
        regex = re.compile('[%s]' % re.escape(self.punct))
        remove_punctuation = str.maketrans(' ', ' ', self.punct)
        for w in words:
            if w in self.tags_features:
                punctuation_filtered.append(w)
            else:
                punctuation_filtered.append(regex.sub('', w))   
        filtered_list = self.strip_list_noempty(punctuation_filtered)
        return ' '.join(map(str, filtered_list))
    
    def lemitizeWords(self, text):
        words = self.token.tokenize(text)
        listLemma = []
        for w in words:
            x = self.lemma.lemmatize(w, pos="v")
            listLemma.append(x)
        return ' '.join(map(str, listLemma))

    def stopWordsRemove(self, text):
        words = self.token.tokenize(text)
        filtered = [w for w in words if not w in self.stop_words]
        return ' '.join(map(str, filtered))