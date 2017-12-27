
# coding: utf-8

# # Estudando NLP
# 
# O que eu pretendo usar: CSTNews Corpus
# 
# 
# NLTK;
# 
# Portuguese Examples: http://www.nltk.org/howto/portuguese_en.html

# In[1]:


import nltk


# # 1. Tokenização
# 
# ## 1.1 Tokenização em setenças
# 
# Token é um pedaço de um todo, então: 
# 
# - uma palavra é um token em uma sentença;
# - uma sentença é um token em um paragrafo.
# 
# Logo separar um paragrafo em sentenças é tokenizar sentenças.

# In[2]:


from nltk.tokenize import sent_tokenize

f = open('sample.txt')
dataset = f.read()

sentence_tokenized = sent_tokenize(dataset)
print(sentence_tokenized)


# In[3]:


len(sentence_tokenized)


# ### Tokenização em Português!

# In[4]:


import nltk.data
portuguese_tokenizer = nltk.data.load('tokenizers/punkt/PY3/portuguese.pickle')
portuguese_tokenizer.tokenize(dataset)


# ## 1.2 Tokenização em palavras

# In[5]:


from nltk.tokenize import word_tokenize

first_sentence_word_tokenized = word_tokenize(sentence_tokenized[0])
print(first_sentence_word_tokenized)## 1.3 Tokenização com expressão regular


# ## 1.3 Tokenização com expressão regular
# 
# Por exemplo para pegar apenas palavras em um texto

# In[6]:


from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer("[\w']+")

first_sentence_word_tokenized_without_punctuation = tokenizer.tokenize(sentence_tokenized[0])
print(first_sentence_word_tokenized_without_punctuation)


# ## 1.4 Treinando um tokenizador de sentenças
# 
# O tokenizador do NLTK é para uso geral, nem sempre é a melhor opção para textos, dependendo da formatação do texto. 

# In[7]:


from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext

text = webtext.raw('overheard.txt')
sent_tokenizer = PunktSentenceTokenizer(text)


# In[8]:


sents = sent_tokenizer.tokenize(text)
sents


# Como podemos observador, as sentenças são separadas (tokenizadas) em conversas, por que o `PunktSentenceTokenizer` usa um algorítmo de unsupervised learning para aprender o que constitui uma quebra de sentença. É não-supervisionado por que você não precisa dar nenhum texto para treinamento do algoritmo, apenas o texto em si.

# ## 1.5 Filtrando stopwords
# 
# Stopwords são palavras que geralmente não contribuem para o significado de uma sentença.

# In[9]:


from nltk.corpus import stopwords

portuguese_stops = set(stopwords.words('portuguese'))
words = first_sentence_word_tokenized_without_punctuation

words_without_stop = [word for word in words if word not in portuguese_stops]
print(words_without_stop)


# # 2. Substituindo e corrigindo palavras
# 
# ## 1.1 Stemming 
# 
# Stemming é a técnica que remove os afixos das palavras, deixando apenas seu radical, existe uma versão em Português que é `RSLPStemmer`

# In[10]:


from nltk.stem import RSLPStemmer

stemmer = RSLPStemmer()
stem_acidente = stemmer.stem(words_without_stop[1]) #acidente
print(stem_acidente)


# ## 3. Transformando texto raw no formato do NLTK
# 
# NLTK tem seu formato de texto padrão, para converter o que é preciso ser feito:
# 
# - Tokenizar o texto em palavras
# - Usar método de conversão para `nltk.txt``

# ### 3.1 Tokenizando em palavras

# In[11]:


text_tokenized = word_tokenize(dataset)
type(text_tokenized)


# ### 3.2 Convertendo

# In[12]:


text_format = nltk.Text(text_tokenized)
type(text_format)


# By transforming a raw text into a text we can use more NLTK features

# ### Análise de estrutura de texto
# 
# A concordância nos permite ver palavras em contexto.

# In[13]:


text_format.concordance('acidente')


# In[14]:


text_format.similar('um')


# In[15]:


text_format.collocations()


# Análisando a frequência relativa de palavras

# In[16]:


from nltk import FreqDist

fd1 = FreqDist(text_format)
print(dict(fd1))
