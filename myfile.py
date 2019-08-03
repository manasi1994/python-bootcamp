print("This is myfile!")
x=15
y=1
z="This is a string"
a="Hello "
b="World"
c="again"
print("x/y = ", x/y)
myList=[1,2,3,4,5]
i=0
#for i in myList:
 #   print(i)

def myPrint(words):
    print(words,"ok")

#myPrint("Are you")

def myFunc(vList):
    for i in vList:
        print(i)
#myFunc([1,2,"WHYY",4,"hello"])   

def myRecursFunc(vList):
    if len(vList)>0:
        #print(vList.pop())
        myRecursFunc(vList)
#myRecursFunc([1,2,3,4,5])

while(x>0):
    #print(x)
    x-=1
def example2(start,vList,step):
    for i in range(start,len(vList),step):
        print(vList[i])

def example21(start,vList,step):
    if(i<len(vList)):
        print(vList.pop)
        example21(start,vList,step)



#example21(0,[3,4,5,6,7,9,10,11],2)