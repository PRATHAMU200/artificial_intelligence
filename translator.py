'''Usage

from translation import baidu, google, youdao, iciba

print(google('hello world!', dst = 'zh-CN'))
print(google('hello world!', dst = 'ru'))
print(baidu('hello world!', dst = 'zh'))
print(baidu('hello world!', dst = 'ru'))
print(youdao('hello world!', dst = 'zh-CN'))
print(iciba('hello world!', dst = 'zh'))
print(bing('hello world!', dst = 'zh-CHS'))
Documents

You may find document here

Advanced usage

Proxies

You may not use some of the function without proxies.

Proxies can be set as following.

from translation import google, ConnectError

# 127.0.0.1:1080 is a vaild proxies
try:
    print(google('hello world!', dst = 'zh-CN', proxies = {'http': '127.0.0.1:1080'}))
except ConnectError:
    print('Invaild proxy')
Default

You may change default setting such as:

default source language (auto if not set)
default destination language (zh-CN if not set)
default translation (youdao if not set)
default proxies (no proxy if not set)
from translation import (set_default_translation, set_default_language,
    set_default_proxies, get, ConnectError)

set_default_translation('google')
set_default_language('auto', 'zh-CN')
set_default_proxies({'http': '127.0.0.1:1080'})
try:
    print(get('hello world!'))
except ConnectError:
    print('Invaild proxy')
More

More functions are introduced in the document.

Language

Language list of all the translation are provided in document.

Somehow, iciba and youdao can only provide English translation.

Google

el    : Greek,
eo    : Esperanto,
en    : English,
af    : Afrikaans,
sw    : Swahili,
ca    : Catalan,
it    : Italian,
iw    : Hebrew,
sv    : Swedish,
cs    : Czech,
cy    : Welsh,
ar    : Arabic,
ur    : Urdu,
ga    : Irish,
eu    : Basque,
et    : Estonian,
az    : Azerbaijani,
id    : Indonesian,
es    : Spanish,
ru    : Russian,
gl    : Galician,
nl    : Dutch,
pt    : Portuguese,
la    : Latin,
tr    : Turkish,
tl    : Filipino,
lv    : Latvian,
lt    : Lithuanian,
th    : Thai,
vi    : Vietnamese,
gu    : Gujarati,
ro    : Romanian,
is    : Icelandic,
pl    : Polish,
ta    : Tamil,
yi    : Yiddish,
be    : Belarusian,
fr    : French,
bg    : Bulgarian,
uk    : Ukrainian,
hr    : Croatian,
bn    : Bengali,
sl    : Slovenian,
ht    : Haitian Creole,
da    : Danish,
fa    : Persian,
hi    : Hindi,
fi    : Finnish,
hu    : Hungarian,
ja    : Japanese,
ka    : Georgian,
te    : Telugu,
zh-TW : Chinese Traditional,
sq    : Albanian,
no    : Norwegian,
ko    : Korean,
kn    : Kannada,
mk    : Macedonian,
zh-CN : Chinese Simplified,
sk    : Slovak,
mt    : Maltese,
de    : German,
ms    : Malay,
sr    : Serbian
'''
from translation import baidu, google, youdao, iciba , bing
print(google('hello world!', dst = 'hi'))
#print(bing('hello world!', dst = 'hi'))

