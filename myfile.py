import sys
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

def main():
    print(sys.argv, type(sys.argv))
    print(len(sys.argv))
    print(sys.argv[0])
    #print(sys.argv[1])

if __name__=='__main__':
    main()