'''The translate() method returns an object that contains information about the translated text, the source and destination languages and the pronunciation of the text. By default, the translate() method returns the English translation of the text passed to it. In our case, the object returned by the translate() method is stored in the result variable.

The object returned by the translate() method has the following attributes:

src: The source language
dest: Destination language, which is set to English (en)
origin: Original text, that is 'Mitä sinä teet' in our example
text: Translated text, that will be 'what are you doing?' in our case
pronunciation: Pronunciation of the translated text

'''



#print(result.src)
#print(result.dest)
#print(result.origin)
#print(result.text)
#print(result.pronunciation)







#result = translator.translate('Mikä on nimesi', src='fi', dest='fr')
#import googletrans

#print(googletrans.LANGUAGES)
# for hindi use "hi" or "hindi"


from googletrans import Translator


def translate(query):
    translator = Translator()
    result = translator.translate(query , dest='en')
    
    print(result.text)
    return (result.text)



def translate_hindi(query):
    translator = Translator()
    result = translator.translate(query , src = 'en' , dest='hi')
    
    return (result.text)


