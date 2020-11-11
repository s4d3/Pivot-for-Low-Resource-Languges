# coding: utf8
import re

re_kanji = re.compile("^[\\s\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A]+$")
re_hiragana = re.compile("^[\\s\u3041-\u3096]+$")
re_katakana = re.compile("^[\\s\u30A0-\u30FF]+$")

iskanji = lambda sz:re_kanji.search(sz)
ishiragana = lambda sz : re_hiragana.search(sz)
iskatakana = lambda sz : re_katakana.match(sz)

def kanjikanasort(word,document):
  """
  return :  0 -> all kanji
            1 -> all Hiragana
            2 -> all katakana
            3 -> mixed
  """
  if(iskanji(word)):
    document["kanji"].append(word)
  elif(ishiragana(word)):
    document["hiragana"].append(word)
  elif(iskatakana(word)):
    document["katakana"].append(word)
  else:
    document["mixed"].append(word)
  return document

def processline(strline):
  resz = strline[strline.find("[")+1:strline.find("]")]
  return [sz.strip(" ") for sz in resz.replace("'","").split(",")]

if __name__ == '__main__':
  docresult = {
    "kanji":[],
    "hiragana":[],
    "katakana":[],
    "mixed":[]
  }

  # wordlist=[" 病院 "," 市民病院"," ひらがな","ください","ヤラ・トラムズ","インドネシア","インドラバグス","バス停","新しいビル","くろボール","日本 うま"]
  # for word in wordlist:
  #   print("X=",kanjikanatype(word))

  fileinput="00-5b-DataALT.03.ja-id.OOV.gdfand.JaMy"
  fileoutput="00-5c-DataALT.03.ja-id.sortedOOV.gdfand.JaMy"
  #fileinput="out.txt"
  #fileoutput="outSorted.txt"
  with open(fileinput,'r') as finput:
    line=finput.readline()
    while line:
      listword = processline(line)
      for word in listword:
        kanjikanasort(word,docresult)
      line = finput.readline()

  with open(fileoutput,'+w') as foutput:
    foutput.write("Number of Kanji: %d\n" % len(docresult["kanji"]))
    foutput.write("============================\n")
    for res in docresult["kanji"]:
      foutput.write(res+"\n")
    foutput.write("\n\n\n")
    foutput.write("Number of Hiragana: %d\n" % len(docresult["hiragana"]))
    foutput.write("============================\n")
    for res in docresult["hiragana"]:
      foutput.write(res+"\n")
    foutput.write("\n\n\n")
    foutput.write("Number of Katakana: %d\n" % len(docresult["katakana"]))
    foutput.write("============================\n")
    for res in docresult["katakana"]:
      foutput.write(res+"\n")
    foutput.write("\n\n\n")
    foutput.write("Number of Mixed: %d\n" % len(docresult["mixed"]))
    foutput.write("============================\n")
    for res in docresult["mixed"]:
      foutput.write(res+"\n")
