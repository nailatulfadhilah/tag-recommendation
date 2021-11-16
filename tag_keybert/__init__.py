from keybert import KeyBERT
from transformers import TFBertModel
from unicodedata import normalize


def replace_ptbr_char_by_word(word):
    """ Will remove the encode token by token"""
    word = str(word)
    word = normalize('NFKD', word).encode('ASCII', 'ignore').decode('ASCII')
    return word


def remove_pt_br_char_by_text(text, stop_words):
    """ Will remove the encode using the entire text"""
    text = str(text)
    text = " ".join(replace_ptbr_char_by_word(word) for word in text.split() if word not in stop_words)
    return text


def keybert(doc):
    with open('stopwords_id.txt', 'r') as f:
        yake_stop_words = f.read().split()

    text = remove_pt_br_char_by_text(doc, yake_stop_words)

    custom_kw_model = KeyBERT(TFBertModel.from_pretrained("indobenchmark/indobert-large-p2"))
    keywords = custom_kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 3),
                                                use_mmr=True, diversity=0.2,
                                                stop_words=None, top_n=15)

    list_keyword = []
    for kw in keywords:
        list_keyword.append(kw[0])
    return list_keyword
