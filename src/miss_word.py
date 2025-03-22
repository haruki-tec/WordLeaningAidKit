import re

def insert_missed_word_in_dict(dict,num):
    dict[num] = 1
    
    
def add_freq_missed_word_in_dict(dict,num):
    dict[num] += 1
    
    
def appdate_missed_word_dict(dict,num):
    if num in dict:
        add_freq_missed_word_in_dict(dict,num)
        return
    
    insert_missed_word_in_dict(dict,num)
    
    
def appdate_missed_words_dict(dict,nums):
    for num in nums:
        appdate_missed_word_dict(dict,int(num))
        
    sort_dict(dict)
        
def create_texts_about_keys_and_values_from_dict(dict):
    texts = []
    if dict:
        for key,value in dict.items():
            texts.append(f"{key} \t {value}回")
            
    return texts

def sort_dict(dict):
    new_align_dict = sorted(dict.items())
    
    #書き換え
    dict.clear()
    dict.update(new_align_dict)
    
def delete_miss_word(dict,word):
    del dict[word]
    
def delete_miss_words(dict,words):
    for word in words:
        re_match = re.search(r'^\d+', word)
        delete_miss_word(dict,int(re_match.group(0)))
        
    sort_dict(dict)