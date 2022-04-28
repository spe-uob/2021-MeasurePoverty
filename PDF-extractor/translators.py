from deep_translator import GoogleTranslator


#translator function - given an array of lines, translate each line in the array, add to array of translated lines,
#and return
def translator_into_english(sentence):
    return GoogleTranslator(source = 'auto',target = 'en').translate(sentence)

def translator_into_foreign(sentence):
    #CHANGE THE LANGUAGE
    return GoogleTranslator(source = 'en',target = 'lt').translate(sentence)




'''
LIST OF ABBREVIATIONS FOR EACH  LANGUAGE
|- afrikaans: af
|- albanian: sq
|- amharic: am
|- arabic: ar
|- armenian: hy
|- azerbaijani: az
|- basque: eu
|- belarusian: be
|- bengali: bn
|- bosnian: bs
|- bulgarian: bg
|- catalan: ca
|- cebuano: ceb
|- chichewa: ny
|- chinese (simplified): zh-CN
|- chinese (traditional): zh-TW
|- corsican: co
|- croatian: hr
|- czech: cs
|- danish: da
|- dutch: nl
|- english: en
|- esperanto: eo
|- estonian: et
|- filipino: tl
|- finnish: fi
|- french: fr
|- frisian: fy
|- galician: gl
|- georgian: ka
|- german: de
|- greek: el
|- gujarati: gu
|- haitian creole: ht
|- hausa: ha
|- hawaiian: haw
|- hebrew: iw
|- hindi: hi
|- hmong: hmn
|- hungarian: hu
|- icelandic: is
|- igbo: ig
|- indonesian: id
|- irish: ga
|- italian: it
|- japanese: ja
|- javanese: jw
|- kannada: kn
|- kazakh: kk
|- khmer: km
|- kinyarwanda: rw
|- korean: ko
|- kurdish: ku
|- kyrgyz: ky
|- lao: lo
|- latin: la
|- latvian: lv
|- lithuanian: lt
|- luxembourgish: lb
|- macedonian: mk
|- malagasy: mg
|- malay: ms
|- malayalam: ml
|- maltese: mt
|- maori: mi
|- marathi: mr
|- mongolian: mn
|- myanmar: my
|- nepali: ne
|- norwegian: no
|- odia: or
|- pashto: ps
|- persian: fa
|- polish: pl
|- portuguese: pt
|- punjabi: pa
|- romanian: ro
|- russian: ru
|- samoan: sm
|- scots gaelic: gd
|- serbian: sr
|- sesotho: st
|- shona: sn
|- sindhi: sd
|- sinhala: si
|- slovak: sk
|- slovenian: sl
|- somali: so
|- spanish: es
|- sundanese: su
|- swahili: sw
|- swedish: sv
|- tajik: tg
|- tamil: ta
|- tatar: tt
|- telugu: te
|- thai: th
|- turkish: tr
|- turkmen: tk
|- ukrainian: uk
|- urdu: ur
|- uyghur: ug
|- uzbek: uz
|- vietnamese: vi
|- welsh: cy
|- xhosa: xh
|- yiddish: yi
|- yoruba: yo
|- zulu: zu

'''
