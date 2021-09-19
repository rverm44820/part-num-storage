
file = open('part_num_cmm.txt','r')
d={}
dict={}
g=[]
k=[]

for line in file:
        
    x = line.split(',')
    a=x[0]
    b=x[1]
    c=len(b)-1 #strips off'\n'
    b=b[0:c]
    d[a]=b
print(d)

# given key already exists in a dictionary.
  
# Function to print sum
def checkKey(d, key):
      
    if key in d.keys():
        print(" cmm Present, ", end =" ")
        print("cmm =", d[key])
    else:
        print("Not present")
        g=input('enter first item part number  ')
        k=input('enter second item cmm ')
        print(g)
        print(k)
        d.update({g: k})
        print(d)
        outfile = open('part_num_cmm.txt','a')
        outfile.write('\n')
        outfile.write( g + ',')
        outfile.write(k + ' ')
        outfile.close()


  
key = input('Enter part number  ')
checkKey(d, key)
print()  
print()
print(d)

