#Bilingual Evaluation Understudy (BLEU) score functions
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu

#takes in reference string and candidate string
def bleuScore(ref, cand):
    ref.split()
    cand.split()
    cc = SmoothingFunction() #smoothing is used for short sentences or sentences without 3/4-grams
    return sentence_bleu([ref], cand, smoothing_function=cc.method4)#sentenece_blue() requires sentences to be tokenized list


#takes in two reference strings and a candidate string
def bleuScore2Ref(ref,ref2, cand):
    ref.split()
    ref2.split()
    cand.split()
    cc = SmoothingFunction() #smoothing is used for short sentences or sentences without 3/4-grams
    return sentence_bleu([ref, ref2], cand, smoothing_function=cc.method4)#sentenece_blue() requires sentences to be tokenized list


ref1 = "Mesmerized by my quest to create machines that thought like people, I had turned into a person who thought like a machine"
ref2 = "Mesmerized by my journey to create machines that thought like people, I had turned into a person that thought like a machine"

candidate = "Mesmerized by my quest to create machines that thought like humans, I had turned into a person who thought like a machine"

#sample:
score = bleuScore(ref1 , candidate)
print(score)

score2 = bleuScore2Ref(ref1, ref2, candidate)
print(score2)
