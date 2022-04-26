import nltk
import random
import string
from sklearn.feature_extraction import text
import re
from hindi_stemmer import hi_stem
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings


f = open("data.txt", encoding="utf8")
article_text = f.read()
f.close()

stop_words = set(line.strip() for line in open('final_stopwords.txt',encoding="utf8"))

article_sentences = nltk.sent_tokenize(article_text)
article_words = nltk.word_tokenize(article_text)

def hi_stem1(tokens):
    if tokens not in stop_words:
        token = ''
        a = []
        for token in tokens.split(" "):
            a.append(hi_stem(token))
        return(a)
    else :
        a = []
        a.append(hi_stem(tokens))
        return(a)

def get_processed_text(document):
    return hi_stem1(document)

greeting_inputs = ("नमस्कार","नमस्ते","सलाम");
greeting_responses = ("""नमस्कार| में आपकी सहायता कैसे कर सकता हूँ ?""");

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token in greeting_inputs:
            return greeting_responses

def generate_response(user_input):
    que_response = ''
    article_sentences.append(user_input)

    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words=stop_words)
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        que_response = que_response + "मैं क्षमाप्रार्थी हूँ पर मैं आपके इस सवाल का उत्तर देने में असमर्थ हूँ ।"
        return que_response
    else:
        que_response = que_response + article_sentences[similar_sentence_number].replace('.','।')
                                   #+ article_sentences[similar_sentence_number - 1].replace('.','।')
        return que_response

exit = ("आज की जानकारी के लिए धन्यवाद,अलविदा","अलविदा","धन्यवाद","खुदा हाफ़िज़")
continue_dialogue = True
print("""नमस्कार |""")

print(""" में आपकी सहायता कैसे कर सकता हूँ ? """)
while(continue_dialogue == True):
    iput = input()
    if re.match(r'^\s*$', iput):
        continue
    human_text=iput.strip()
    if human_text not in exit:
        if human_text == 'शुक्रिया':
            print("चैम्प: यह तो मेरा बड़प्पन है")
            continue_dialogue = False

        else:
            if human_text == 'नमस्कार' or human_text == 'नमस्कार ।':
                warnings.filterwarnings(action='ignore')
                print("चैम्प: " + generate_greeting_response(human_text))
            else:
                print("चैम्प: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
    else:
        print("चैम्प: अलविदा")
        continue_dialogue = False
