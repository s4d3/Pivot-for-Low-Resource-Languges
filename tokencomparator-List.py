# coding: utf8

def processline(strline):
  """
  Stripped down token in a line, also igonre '・' as token.
  """  
  resz = strline[strline.find("[")+1:strline.find("]")]
  return [sz.strip(" ・") for sz in resz.replace("'","").split(",")]

def gettokenline(szfilename):
  linesresult = []
  with open(szfilename,'r') as finput:
    line=finput.readline()
    while line:
      listword = processline(line)
      linesresult.append(listword)
      line = finput.readline()
  return linesresult

if __name__ == '__main__':
  fileinput1="00-1b-DataALT.03.ja-id.OOV.gdfand.JaEn"
  fileinput2="06-1b-DataALT.03.ja-id.OOV.tgttosrc.JaEn"
  fileoutput = "TokenComparator-List-gdfand-tgttosrc.JaEn"

  linesfile1 = gettokenline(fileinput1)
  linesfile2 = gettokenline(fileinput2)
  
  unk_tok = [] # Collection of unknown token
  try :
    for i in range(len(linesfile1)):
      errlinetok=[] # Will filled with unmatch token between file 1 and file 2
      for tokenf1 in linesfile1[i]:
        isexist=False
        for tokenf2 in linesfile2[i]:
          try:
            if(((tokenf1 in tokenf2) == True) or ((tokenf2 in tokenf1) == True) ):
              isexist=True # We have matched token, break from the current iteration
              break
          except Exception as ex:
            print(ex) # Will raise exception for invalid index (out of index in file2)
        if(isexist is False):errlinetok.append(tokenf1)

      unk_tok.append(errlinetok)
    lncnter=0
    strtokenout = str()
    storagetoken = dict()
    for tokens in unk_tok:
      if(len(tokens) != 0):
        for token in tokens:
          if((token in storagetoken) == False):
            storagetoken[token]=1
          else:
            storagetoken[token]+=1 

        strtokenout += str("Line: %d, number of Unknown Token in file2: %d ==> [%s]\n" %
        (lncnter,len(tokens)," | ".join(sz for sz in tokens)))
      lncnter += 1
          
    with open(fileoutput,'+w') as foutput:
      foutput.write("Report comparator: \n")
      foutput.write("==================================\n")
      foutput.write("Number of Unknown type token: %d\n" % (len(storagetoken)))
      foutput.write("----------------------------------\n")
      for token in storagetoken:
        foutput.write("Token %-10s : %d\n" %(token,storagetoken[token]))
      foutput.write("\n\n")
      foutput.write("Line details: \n")
      foutput.write("--------------------------------\n")      
      foutput.write(strtokenout)
  except Exception as ex:
    print("Exception: ",ex)
  finally:
    print("Finished")

