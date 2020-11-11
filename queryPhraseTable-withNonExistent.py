import sys
animation = "|/-\\"
ianim=0

def is_exist(token,strline):
  strfind=strline.split("|||")
  if (strfind[0].strip() == token):
    return True
  else:
    return False 

def print_animation():
  global ianim
  szbckspace="".join("\r" for i in range(len("Please Wait: |")))
  szanim = szbckspace + "Please Wait: "+animation[ianim % len(animation)]
  sys.stdout.write(szanim)
  ianim+=1


if __name__ == "__main__":
  fileinput1 = "ListOOV-gdfand-tgttosrc.JaId"
  fileinput2 = "phrase-table.gdfand.JaId"
  fileoutput = "queryPhraseTable.gdfand.JaId"
  lstnonexist = list() # List on non exists token
  try:
    fhandleout = open(fileoutput,"+w")
    with open(fileinput1) as fhandlein1:
      linetoken = fhandlein1.readline()
      while linetoken:
        splitresult=linetoken.split(" ") 
        if(splitresult[0] != "Token"): # It's not a token
          linetoken = fhandlein1.readline()
          continue
        token=splitresult[1]
        with open(fileinput2) as fhandlein2:
          linephrase = fhandlein2.readline()
          print_animation()
          istokenexist = False #Assume the token never exist of phrase file
          while(linephrase):
            if(is_exist(token,linephrase) == True):
              fhandleout.write(linephrase) # Write result to file output
              fhandleout.flush()
              istokenexist = True
            linephrase = fhandlein2.readline()
          if(istokenexist == False):
            lstnonexist.append(token)
        linetoken = fhandlein1.readline()
    fhandleout.write("\n\n")
    fhandleout.write("Non Existent Token\n")
    fhandleout.write("=========================\n")
    fhandleout.write("Number of non existent token: %d\n" %(len(lstnonexist)))
    for nonexist in lstnonexist:
      fhandleout.write("%s\n" %(nonexist))
    fhandlein2.close()
    fhandleout.close()
    print()
    print("Finished")
  except Exception as ex:
    print("error caught: ",ex)


