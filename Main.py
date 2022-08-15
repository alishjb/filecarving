import re,os
username=os.popen("id -un").read() # getting username
username=username.replace('\n','')
jpg_sof = b'\xff\xd8\xff' # jpeg files start with hex ff d8 ff 
jpg_eof = b'\xff\xd9'     # jpeg files end with hex ff d8 ff
sof_list,eof_list=[],[]   # creating an empty list for append start and end of hidden jpeg file in main file
path=f'/home/{username}/Desktop/test_files/test.pdf' # address of file ( u can replate it with file name if main.py and target file is in same folder ) 
file_handler= open(path,'rb') # reading main file
data = file_handler.read() 
for match in re.finditer(jpg_sof,data):
    sof_list.append(match.start())

for match in re.finditer(jpg_eof,data):
    eof_list.append(match.start())
i = 0 
for sof in sof_list:
    jpg_data = data[sof:eof_list[i]+1]
    filename = f"/home/{username}/Desktop/test_files/Carved_{sof}_{eof_list[i]}.jpg"
    res=open(filename,'wb')
    res.write(jpg_data)
    res.close()
    i+=1
