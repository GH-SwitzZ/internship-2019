from xml.etree import ElementTree
import os,json
data=input('filename:')
# data='weather'
xpars = os.path.abspath(os.path.join(data+".xml"))
dom =ElementTree.parse(xpars)
root=dom.getroot()
js=[]
subtext=False

def To_attrib(r):
    attrib=str(r.attrib).replace(chr(92),'')
    return attrib
def To_tag(r):
    tag=chr(39)+str(r.tag)+chr(39)+":"
    return tag


# find component
for x in root:
    sub=[]
    c=0
    i=''
    # find details
    for r in x.iter():
        if not subtext:
            attrib=To_attrib(r)
            tag=To_tag(r)
        else:
            tag=tag+'{'+To_tag(r)
            attrib=To_attrib(r)
            subtext=False
        
        if r.text :#is not end
            i=list(x)
            # head attrib
            if len(r.attrib)!=0:                
                attrib.replace('}','') 
            # sub text 
            elif r.tag!=x.tag:               
                attrib=chr(34)+r.text+chr(34)
            else :
                subtext=True
                c+=1
                continue           
        elif  c==len(i) and i!='':#end            
            attrib=attrib+'}'
        #add details 
        sub.append(tag+attrib)
        c+=1
    js.append(sub)


c=0
myjson='{'
json.load
for i in js:
    c+=1
    if c==len(js):
        myjson=myjson+(str(i).replace(chr(34),'').replace(chr(91),'').replace(']',''))
    else:
        myjson=myjson+(str(i).replace(chr(34),'').replace(chr(91),'').replace(']',','))
myjson=myjson+'}'.replace(chr(39),chr(34))
print(myjson)
# file=input('filename:')
# file_json=open(file+'.json','w+')
file_json=open(data+'.json','w+')
file_json.write(myjson)
file_json.close()