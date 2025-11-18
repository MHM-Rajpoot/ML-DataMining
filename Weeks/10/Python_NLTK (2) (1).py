#!/usr/bin/env python
# coding: utf-8

# **Step by Step guide to learn Python NLTK <br> **

# In[1]:


import nltk


# In[5]:


nltk.download()


# In[3]:


import os
import nltk.corpus


# In[4]:


print(os.listdir(nltk.data.find("corpora")))
       


# In[6]:


nltk.corpus.gutenberg.fileids()


# **Gutenberg Corpora**
# 

# In[7]:


hemlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
hemlet[:100]


# In[8]:


hemlet_sentences=nltk.corpus.gutenberg.sents('shakespeare-hamlet.txt')
print(hemlet_sentences[:2])
print(len(hemlet_sentences))


# In[9]:


hemlet_paragraphs=nltk.corpus.gutenberg.paras('shakespeare-hamlet.txt')


print(len(hemlet_paragraphs))


# **Brown Corpora**

# In[10]:


from nltk.corpus import brown


# In[11]:


nltk.corpus.brown.fileids()


# In[12]:


brown.categories()


# In[13]:


len(brown.sents())


# In[15]:


len(brown.sents(categories='government'))


# In[16]:


len(brown.words(categories='news'))


# In[17]:


text=(brown.words(categories='news'))
print(text)


# **Frequency of Words**

# In[18]:


from nltk.probability import FreqDist
dist = FreqDist(text)
print(dist)


# In[19]:


vocab=dist.keys()
print(vocab)


# To find out the frequency of individuaal word

# In[21]:


dist['means']


# To find the frequency of specific words

# ID	File	Genre	Description
# A16	ca16	news	Chicago Tribune: Society Reportage
# B02	cb02	editorial	Christian Science Monitor: Editorials
# C17	cc17	reviews	Time Magazine: Reviews
# D12	cd12	religion	Underwood: Probing the Ethics of Realtors
# E36	ce36	hobbies	Norling: Renting a Car in Europe
# F25	cf25	lore	Boroff: Jewish Teenage Culture
# G22	cg22	belles_lettres	Reiner: Coping with Runaway Technology
# H15	ch15	government	US Office of Civil and Defence Mobilization: The Family Fallout Shelter
# J17	cj19	learned	Mosteller: Probability with Statistical Applications
# K04	ck04	fiction	W.E.B. Du Bois: Worlds of Color
# L13	cl13	mystery	Hitchens: Footsteps in the Night
# M01	cm01	science_fiction	Heinlein: Stranger in a Strange Land
# N14	cn15	adventure	Field: Rattlesnake Ridge
# P12	cp12	romance	Callaghan: A Passion in Rome
# R06	cr06	humor	Thurber: The Future, If Any, of Comedy

# In[20]:


news_text = brown.words()
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end='\n')


# Frequency of individual word in specific category

# In[21]:


news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m], end='\n')


# **Normalization and Stemming**<br>

# In[22]:


data=['write','writer','wrote','written','writing']


# In[23]:


# Lancastter Stemmer
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()
[st.stem(t) for t in data]


# In[24]:


# Porter Stemmer
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
[porter.stem(t) for t in data]


# In[25]:


# snowball stemmer
from nltk.stem.snowball import SnowballStemmer
snow=SnowballStemmer("english")
[snow.stem(t) for t in data]


# In[26]:


snow=SnowballStemmer("english").stem("generous")
porter=SnowballStemmer("porter").stem("generous")
print(snow)
print(porter)


# Snowball stemmer is better than Porter

# **Lemmatization**

# It is another way to extract the base form of words, lemmatization is similar to stemming but it brings context to the words. So it links words with similar meaning to one word.  Some treat these two as same but actually, lemmatization is preferred over Stemming because lemmatization does morphological analysis of the words.

# In[27]:


udhr = nltk.corpus.udhr.words('English-Latin1')


# In[28]:


udhr[:20]


# In[29]:


# [porter.stem(t) for t in udhr[:20]]
[SnowballStemmer("english").stem(t) for t in udhr[:20]]


# In[30]:


from nltk.stem import WordNetLemmatizer 
# lemmatizer=nWordNetLemmatizerltk. () 
  
lemmatizer = WordNetLemmatizer() 
[lemmatizer.lemmatize(t) for t in udhr[:20]]


# **Tokenization**<br>
# It is the process of breaking strings into tokens which in turn are small structures or units. Tokenization involves steps which are breaking a complex sentence into words, understanding the importance of each word with respect to the sentence 
# 

# In[31]:


sentence= "Children shouldn't drink a sugary drink before bed."
sentence.split(' ')


# In[32]:


from nltk.tokenize import word_tokenize as tokenizer
semtence_tokens=tokenizer(sentence)
semtence_tokens


# In[33]:


para = "This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"


# In[34]:


from nltk.tokenize import sent_tokenize as sentokenize
para_into_sentence=sentokenize(para)
para_into_sentence


# In[36]:


text = "In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of South America"


# In[37]:


token=tokenizer(text)
from nltk.probability import FreqDist
fdist = FreqDist(token)
fdist


# In[37]:


fdist.most_common(5)


# In[38]:


from nltk.corpus import stopwords
stopwords=stopwords.words("english")
len(stopwords)
print(stopwords)


# In[39]:


[w for w in token
 if w.lower() not in stopwords]


# **Regex Tokenizer**<br>
# To remove this full stop, regex Tokenizer will be used that uses the pattern to tokenize the sentence

# In[40]:


regex_tokenizer = nltk.RegexpTokenizer(r"\w+")


# In[41]:


regextokens=regex_tokenizer.tokenize(text)
print(regextokens)


# In[42]:


import nltk
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
# txt = """ This is one sentence. This is another sentence."""
print(tokenizer.tokenize(text))


# In[43]:


regextokens


# **POS Tagging**<br>Assigning the lexical categories

# In[44]:


# NLTK provides documentation for each tag, which can be queried using the tag,

nltk.help.upenn_tagset('VBG')


# In[45]:


tagset=nltk.pos_tag(regextokens)
tagset


# In[78]:


NLTK_Tag=nltk.pos_tag(text.split())
print(NLTK_Tag)


# In[57]:


tagger = nltk.data.load('taggers/maxent_treebank_pos_tagger/english.pickle')
t=tagger.tag(text.split())
print(t)


# **Tagged Corpora**<br>To represent tagged token using a tuple consisting of the token and the tag.

# In[79]:


tagged_token = nltk.tag.str2tuple('Learn/VB')

print(tagged_token)
print(tagged_token[0])
print(tagged_token[1])


# **Reading Tagged Corpora**

# In[59]:


nltk.corpus.brown.fileids()
nltk.corpus.brown.categories()
nltk.corpus.brown.words(categories='government')
nltk.corpus.brown.tagged_words(categories='government')[:10]


# **N-grams**

# In[46]:


data = ["this", "is", "not", "a", "test", "this", "is", "real", "not", "a", "test", "this", "is", "this", "is","real","not", "a", "test", "good", "morning"]
from nltk import ngrams, FreqDist
all_counts = dict()
for size in 2, 3, 4, 5:
    all_counts[size] = FreqDist(ngrams(data, size))
all_counts[2].most_common(5)
# all_counts[2]


# **Chunking**<br>

# In[ ]:





# In[47]:


# Loading Libraries 
from nltk.chunk.regexp import ChunkString, ChunkRule 
from nltk.tree import Tree 
  
# ChunkString() starts with the flat tree 
tree = Tree('S', [('the', 'DT'), ('book', 'NN'), 
               ('has', 'VBZ'), ('many', 'JJ'), ('chapters', 'NNS')]) 
tree.draw()


# In[ ]:


# Initializing ChunkString() 
chunk_string = ChunkString(tree) 
print ("Chunk String : ", chunk_string) 


# In[ ]:


grammar = r"""
  NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
  PP: {<IN><NP>}               # Chunk prepositions followed by NP
  VP: {<VB.*>} # Chunk verbs and their arguments
        
  """


# In[ ]:


chunker = nltk.RegexpParser(grammar) 
sent=chunker.parse(tree)
sent.draw()


# In[65]:


chunker1 = nltk.RegexpParser(grammar) 
sent = [('the', 'DT'), ('sushi', 'NN'), ('roll', 'NN'), ('was', 'VBD'),  
        ('filled', 'VBN'), ('with', 'IN'), ('the', 'DT'), ('fish', 'NN')] 
result2=chunker.parse(sent) 
result2.draw()


# In[66]:


chunker1 = nltk.RegexpParser(grammar) 
sent = [('sushi', 'NN'), ('sushi', 'NN')] 
result2=chunker.parse(sent) 
result2.draw()


# In[33]:


from nltk.chunk import RegexpParser
chunker = RegexpParser(r''' 
NP: 
{<DT><NN.*><.*>*<NN.*>} 
}<VB.*>{ 
''') 
sent = [('the', 'DT'), ('sushi', 'NN'), ('roll', 'NN'), ('was', 'VBD'),  
        ('filled', 'VBN'), ('with', 'IN'), ('the', 'DT'), ('fish', 'NN')] 
result2=chunker.parse(sent) 
print(result2)
result2.draw()


# **POS Tagging helps in removing Ambiguity occuring in a sentence**

# In[67]:


# plant is an ambiguious word

sentence=nltk.word_tokenize("each one plant one")
sentence1=nltk.word_tokenize("Plants required light and water to grow")
sentence=nltk.pos_tag(sentence)
sentence1=nltk.pos_tag(sentence1)
print(sentence)
print(sentence1)


# In[68]:


# NLTK lesk is used for word disambiguition
from nltk.wsd import lesk
print(lesk(sentence, 'plant'))
print(lesk(sentence1, 'plant','n'))


# In[69]:


from nltk.corpus import wordnet as wn
for ss in wn.synsets('plant'):
    print(ss,ss.definition())


# **Name Entity Recognition using NLTK**

# In[70]:


# With the function nltk.ne_chunk(), we can recognize named entities using a 
# classifier, the classifier adds category labels such as PERSON, ORGANIZATION, and GPE.

import nltk


my_sent = "WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E. Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcement."

parse_tree = nltk.ne_chunk(nltk.tag.pos_tag(nltk.word_tokenize(my_sent)), binary=True)  # POS tagging before chunking!

parse_tree.draw()
print(parse_tree)


# In[71]:


named_entities = []

for t in parse_tree.subtrees():
    if t.label() == 'NE':
        named_entities.append(t)
        # named_entities.append(list(t))  # if you want to save a list of tagged words instead of a tree

print(named_entities)


# In[72]:


from nltk.tree import Tree

txt="WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E. Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcement."

pos_tag = nltk.pos_tag(txt.split())
parse_tree = nltk.ne_chunk(pos_tag )
# print(chunk)
parse_tree.draw()
NE=[]
for chunk in parse_tree:
    if hasattr(chunk, 'label'):
        NE=(chunk.label(), ' '.join(c[0] for c in chunk))
        print(NE)
        
    


# In[73]:


word = nltk.word_tokenize(my_sent)   
pos_tag = nltk.pos_tag(word)   
chunk = nltk.ne_chunk(pos_tag)   
NE = [ " ".join(w for w, t in name) for name in chunk if isinstance(name, nltk.Tree)]   
print (NE)


# In[74]:


word = nltk.word_tokenize(my_sent)   
pos_tag = nltk.pos_tag(word)   
chunk = nltk.ne_chunk(pos_tag)   
for name in chunk:
    if isinstance(name,nltk.Tree):
        ne=" ".join(w for w, t in name)
        print(ne)
       

# NE = [ " ".join(w for w, t in name) for name in chunk if isinstance(name, nltk.Tree)]   
# print (NE)


# In[75]:


sentence="Alice Loves Bob"


# In[76]:


chunk=nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)))
print(chunk)


# In[ ]:




