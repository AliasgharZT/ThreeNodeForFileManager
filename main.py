
class Node(): 
    def __init__(self):
        self.data=None 
        self.prev=None 
        self.next=list()
class Three():
    root=Node()
    len_disk=0
    def add_disk(self,disk):
        d=Node()
        self.root.next.append(d)
        d.prev=self.root
        d.data=disk
        d.next=[]
        self.len_disk+=1
    def print_disk(self):
        for q in range(self.len_disk):
            print(self.root.next[q].data)
    def add_files(self,address):
        try:
            address=address.split('\\')
            address[0]+='\\'
            la=len(address)
            nd=None 
            for q in range(la):
                if q==0:
                    for w in range(self.len_disk):
                        if (self.root.next[w].data)==(address[q]):
                            nd=self.root.next[w]
                elif q+1==la:
                    n=Node()
                    n.data=address[q]
                    n.prev=nd
                    n.next=[]
                    nd.next.append(n)
                else:
                    for w in range(len(nd.next)):
                        if nd.next[w].data==address[q]:
                            nd=nd.next[w]
        except:pass 
    def show_files(self,address):
        try:
            if len(address)==3:
                address=[address]
            else:
                address=address.split('\\')
                address[0]+='\\'
            la=len(address)
            nd=None 
            for q in range(la):
                if q==0:
                    if q+1==la:
                        for w in range(self.len_disk):
                            if (self.root.next[w].data)==(address[q]):
                                nd=self.root.next[w]
                        for e in range(len(nd.next)):
                            print(nd.next[e].data,end=',')
                        print()
                    else:
                        for w in range(self.len_disk):
                            if (self.root.next[w].data)==(address[q]):
                                nd=self.root.next[w]
                elif q+1==la:
                    for w in range(len(nd.next)):
                        if nd.next[w].data==address[q]:
                            nd=nd.next[w]
                    for e in range(len(nd.next)):
                        print(nd.next[e].data,end=',')
                    print()                     
                else:
                    for w in range(len(nd.next)):
                        if nd.next[w].data==address[q]:
                            nd=nd.next[w]
        except:pass 
# -----------------  
t=Three()
ln=['C:\\','E:\\','D:\\','B:\\','K:\\']
ld=len(ln)
for q in range(ld):
    t.add_disk(ln[q])
t.print_disk()
#---------[C]---------
address='C:\\N1'
t.add_files(address)
address='C:\\N1\\main.py'
t.add_files(address)
address='C:\\N1\\main2.py'
t.add_files(address)
address='C:\\N1\\N2'
t.add_files(address)
address='C:/N1/N2/main3.py'
t.add_files(address)
# ---------[E]----------
address='E:\\User'
t.add_files(address)
address+='\\AliasgharZahdyan'
t.add_files(address)
print('---------C------------')
address='C:\\'
t.show_files(address)
address+='N1'
t.show_files(address)
address+='\\N2'
t.show_files(address)
print('-----------E-------------')
address='E:\\User'
t.show_files(address)