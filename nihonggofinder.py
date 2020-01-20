# coding: utf8

import re
#import codecs
#import unicodedata

def nihongofinder(strline):
  """
  Pattern is 
  Katakana List: \u30A0-\u30FF
  Hiragana List: \u3041-\u3096
  Kanji List : \u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A
  """
  pattern="[\u30A0-\u30FF\u3041-\u3096\u3400-\u4DB5\u4E00-\u9FCB\uF900-\uFA6A]+"
  recomp = re.compile(pattern)
  matchobj=recomp.findall(strline)
  return list(matchobj)

def simpleparser(filename):
  """ simply parsing a file consist of japanese character in its line"""
  with open(filename,'r') as fp:
    line = fp.readline()
    while line:
      ret = nihongofinder(line)
      print("num-of-jpn: %d -> %s" % (len(ret),ret))
      line = fp.readline()
      

if __name__ == '__main__':
  fname="00-5a-DataALT.03.jp-id.src.translated.detoken.gdfand.JaMy"
  simpleparser(fname)


