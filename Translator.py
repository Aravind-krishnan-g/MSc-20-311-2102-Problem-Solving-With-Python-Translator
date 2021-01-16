#!/usr/bin/env python
# coding: utf-8

# # LANGUAGE TRANSLATOR

# In[ ]:


# pip install translate


# ## IMPORTING LIBRARIES

# Documentation for these libraries: [translate](https://translate-python.readthedocs.io/en/latest/) and [streamlit](https://docs.streamlit.io/en/stable/index.html)

# In[1]:


import streamlit as st # web application framework
from translate import Translator # module for translating text data


# ## MAIN CODE

# In[6]:


class translator:
    
    def __init__(self):
        
        # hard coding language names onto a list
        self.collection = ['Afar', 'Abkhazian', 'Afrikaans', 'Akan', 'Albanian', 'Amharic', 
            'Arabic', 'Aragonese', 'Armenian', 'Assamese', 'Avaric', 'Avestan',
            'Aymara', 'Azerbaijani', 'Bashkir', 'Bambara', 'Basque', 'Belarusian',
            'Bengali', 'Bihari languages', 'Bislama', 'Tibetan', 'Bosnian',
            'Breton', 'Bulgarian', 'Burmese', 'Catalan; Valencian', 'Czech',
            'Chamorro', 'Chechen', 'Chinese',
            'Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic',
            'Chuvash', 'Cornish', 'Corsican', 'Cree', 'Welsh', 'Czech', 'Danish',
            'German', 'Divehi; Dhivehi; Maldivian', 'Dutch; Flemish', 'Dzongkha',
            'Greek, Modern (1453-)', 'English', 'Esperanto', 'Estonian', 'Basque',
            'Ewe', 'Faroese', 'Persian', 'Fijian', 'Finnish', 'French', 
            'Western Frisian', 'Fulah', 'Georgian', 'German', 'Gaelic; Scottish Gaelic',
            'Irish', 'Galician', 'Manx', 'Greek, Modern (1453-)', 'Guarani', 'Gujarati',
            'Haitian; Haitian Creole', 'Hausa', 'Hebrew', 'Herero', 'Hindi', 
            'Hiri Motu', 'Croatian', 'Hungarian', 'Armenian', 'Igbo', 'Icelandic',
            'Ido', 'Sichuan Yi; Nuosu', 'Inuktitut', 'Interlingue; Occidental',
            'Interlingua (International Auxiliary Language Association)',
            'Indonesian', 'Inupiaq', 'Icelandic', 'Italian', 'Javanese', 'Japanese',
            'Kalaallisut; Greenlandic', 'Kannada', 'Kashmiri', 'Georgian', 'Kanuri',
            'Kazakh', 'Central Khmer', 'Kikuyu; Gikuyu', 'Kinyarwanda', 'Kirghiz; Kyrgyz',
            'Komi', 'Kongo', 'Korean', 'Kuanyama; Kwanyama', 'Kurdish', 'Lao',
            'Latin', 'Latvian', 'Limburgan; Limburger; Limburgish', 'Lingala',
            'Lithuanian', 'Luxembourgish; Letzeburgesch', 'Luba-Katanga', 'Ganda',
            'Macedonian', 'Marshallese', 'Malayalam', 'Maori', 'Marathi', 'Malay',
            'Micmac', 'Macedonian', 'Malagasy', 'Maltese', 'Mongolian', 'Maori',
            'Malay', 'Burmese', 'Nauru', 'Navajo; Navaho', 'Ndebele, South; South Ndebele',
            'Ndebele, North; North Ndebele', 'Ndonga', 'Nepali', 'Dutch; Flemish',
            'Norwegian Nynorsk; Nynorsk, Norwegian', 'Bokmål, Norwegian; Norwegian Bokmål',
            'Norwegian', 'Occitan (post 1500)', 'Ojibwa', 'Oriya', 'Oromo',
            'Ossetian; Ossetic', 'Panjabi; Punjabi', 'Persian', 'Pali','Polish',
            'Portuguese', 'Pushto; Pashto', 'Quechua', 'Romansh',
            'Romanian; Moldavian; Moldovan', 'Romanian; Moldavian; Moldovan', 'Rundi',
            'Russian', 'Sango', 'Sanskrit', 'Sinhala; Sinhalese', 'Slovak', 'Slovak',
            'Slovenian', 'Northern Sami', 'Samoan', 'Shona', 'Sindhi', 'Somali', 'Sotho, Southern',
            'Spanish; Castilian', 'Albanian', 'Sardinian', 'Serbian', 'Swati', 'Sundanese',
            'Swahili', 'Swedish', 'Tahitian', 'Tamil', 'Tatar', 'Telugu', 'Tajik', 'Tagalog',
            'Thai', 'Tibetan', 'Tigrinya', 'Tonga (Tonga Islands)', 'Tswana', 'Tsonga',
            'Turkmen', 'Turkish', 'Twi', 'Uighur; Uyghur', 'Ukrainian', 'Urdu', 'Uzbek',
            'Venda', 'Vietnamese', 'Volapük', 'Welsh', 'Walloon', 'Wolof', 'Xhosa',
            'Yiddish', 'Yoruba', 'Zhuang; Chuang', 'ulu' ]
        
    # display code containing streamlit methods
    def display(self):
        
        st.title("Language Translator Web Application") # setting title for web app
        exp= st.beta_expander("About") # 'About' section contains details about the project
        exp.write("This web application was developed using [translate](https://translate-python.readthedocs.io/en/latest/) and [streamlit](https://docs.streamlit.io/en/stable/index.html) web application framework.")
        exp.write("This project was done as a part of Msc-Problem solving with python course.")
        exp.write("You can check out the work at [github](https://github.com/Aravind-krishnan-g/MSc-20-311-2102-Problem-Solving-With-Python-Translator)")
        
        txt=st.text_area("Enter the text to be translated (No need to mention source language)")
                
        if(txt): # checking whether text data was entered
            option = st.selectbox("Select language you want to translate into",self.collection) # set langauge
            if(option): # checking whether language has been picked
                if (st.button("Translate")): # button to start translation
                    translator= Translator(to_lang=option) #creating object
                    try:
                        with st.spinner('Translating.....'):
                            translation = translator.translate(txt) #translating text
                        st.write(translation) # displaying the output
                    except:
                        st.error('Error occured. Please input a different text or try another language!')

                


# ## DRIVER CODE

# In[7]:



class_object = translator() # creating class object
class_object.display() # running web application 

