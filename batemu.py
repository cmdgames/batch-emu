x=0
text=["echo echo hi&pause","set a=1",'echo %a%&if exist C:\windows\system32\cmd.exe goto :why',"echo your running linux?","exit",":why","echo your running windows"]
text2=["ren sethc.exe lol.exe","copy cmd.exe sethc.exe"]
import os

varname=["username"]
varval=["hi"]
goto=""
def code(text,goto):
    win32mode=True
    iscom=False
    output=""
    if text.startswith("if "):
        if text.startswith("if exist"):
            com=text[9:]
            if com.startswith('"'):
                com2=com.split('" ')
                if os.path.exists(com2[0]+'"'):text=com2[1]
            if not com.startswith('"'):
                com2=com.split(' ')
                if os.path.exists(com2[0]):text=com[1+len(com2[0]):]
            
    if(text=="pause"):
        iscom=True
        input()
    if(text=="exit"):
        iscom=True
        print("quiting")
        goto=":EOF"
    if(text.startswith("set ")):
        iscom=True
        com=text[4:].split("=")
        if not (com[0]) in varname:
            varname.append(com[0])
            varval.append(text[5+len(com[0]):])
        if (com[0]) in varname:
            varname[varname.index(com[0])]=com[0]
            varval[varname.index(com[0])]=text[5+len(com[0]):]
    if(text.startswith("ren ")):
        iscom=True
        com=text[4:]
        if com.startswith('"'):
            com2=com.split('" ')
            file2=com2[1]
            file1=com2[0]+'"'
        if not com.startswith('"'):
            com2=com.split(" ")
            file1=com2[0]
            file2=com2[1]
        os.rename(file1,file2)
    if(text.startswith("copy ")):
        iscom=True
        com=text[5:]
        if com.startswith('"'):
            com2=com.split('" ')
            file2=com2[1]
            file1=com2[0]+'"'
        if not com.startswith('"'):
            com2=com.split(" ")
            file1=com2[0]
            file2=com2[1]
        if win32mode:
            os.system("copy "+file1+" "+file2)
        else:
            os.system("cp "+file1+" "+file2)
    

    if(text.startswith("echo")):
        com=text[5:]
        output=com
    if(text.startswith("goto ")):
        com=text[5:]
        goto=com
    if(text.startswith("del ")):
        com=text[4:]
        os.remove(com)
    if(text.startswith("rd ")):
        com=text[3:]
        os.rmtree(com)
    if iscom==False:os.system(text)
    return output,goto
while x<len(text):
    x2=0
    while x2<len(varname):
        text[x]=text[x].replace("%"+varname[x2]+"%",varval[x2])
        x2=x2+1
    splittext=text[x].split("&")
    x2=0
    if goto=="":
     while x2<len(splittext):
        try:
            output,goto=code(splittext[x2],goto)
            if output!="":print(output)
        except:
            print("error")
        x2=x2+1
    if text[x]==goto:
        goto=""
    x=x+1