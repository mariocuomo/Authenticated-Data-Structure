import hashlib



def modify(node):
	node.value='V0'
	node.left.value='V1'
	node.right.value='V2'

	node.left.left.value='V11'
	node.left.right.value='V12'
	node.right.left.value='V21'
	node.right.right.value='V22'

	node.left.left.left.value='V111'
	node.left.left.right.value='V112'
	node.left.right.left.value='V121'
	node.left.right.right.value='V122'
	node.right.left.left.value='V211'
	node.right.left.right.value='V212'
	node.right.right.left.value='V221'
	node.right.right.right.value='V222'


def appenchildren(node):
	left = Node()
	right = Node()
	node.left=left
	node.right=right
	left.parent=node
	right.parent=node

def createTree(node,x):
	if x==1:
		appenchildren(node)
		node.left.value=value_to_store[0]
		node.right.value=value_to_store[1]
		value_to_store.pop(0)
		value_to_store.pop(0)
		return

	appenchildren(node)
	createTree(node.left,x-1)
	createTree(node.right,x-1)


def hashing_tree(node):
	stringToEncode=""
	if(node.left==None and node.right==None):
		stringToEncode = str(node.value)
	else:
		stringToEncode = hashing_tree(node.left) + hashing_tree(node.right)

	hashGen = hashlib.sha512()
	hashGen.update(stringToEncode.encode('utf-8'))
	hash = hashGen.hexdigest()
	node.h = hash

	return hash


def print_tree(node):
	lstToPrint=[]

	lst=[node]

	while len(lst)!=0:
		tmp = lst.pop()
		lstToPrint.append(tmp.value)
		if not tmp.right==None:
			lst.insert(0,tmp.left)
		if not tmp.left==None:
			lst.insert(0,tmp.right)

	

	i=0
	j=0
	tmp=0
	time=0

	while j<len(lstToPrint):
		i=j
		x= pow(2, tmp)

		while time<x:
			print(str(lstToPrint[i])+"  ",end=" ")
			i=i+1
			j=j+1
			time=time+1
		print()
		time=0
		tmp=tmp+1

	print('\nV0=hash(V0|V1)= '+node.h)
	print('V1=hash(V11|V12)= '+node.left.h)
	print('V2=hash(V21|V22)= '+node.right.h)
	print('V11=hash(V111|V112)= '+node.left.left.h)
	print('V12=hash(V121|V122)= '+node.left.right.h)
	print('V21=hash(V211|V212)= '+node.right.left.h)
	print('V22=hash(V221|V222)= '+node.right.right.h)
	print('V111=hash(3)= '+node.left.left.left.h)
	print('V112=hash(5)= '+node.left.left.right.h)
	print('V121=hash(12)= '+node.left.right.left.h)
	print('V122=hash(34)= '+node.left.right.right.h)
	print('V211=hash(41)= '+node.right.left.left.h)
	print('V212=hash(55)= '+node.right.left.right.h)
	print('V221=hash(90)= '+node.right.right.left.h)
	print('V222=hash(243)= '+node.right.right.right.h)

	print('\nROOT HASH = V0 = '+node.h)


#DATA STRUCTURES
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.parent = None
        self.value = None
        self.h = None





value_to_store=[3,5,12,34,41,55,90,243]
print("\nTHIS IS THE LIST TO SAVE IN A CLOUD SERVER")
for value in value_to_store:
    print(str(value)+" ", end="")
print("\n")


#CREATING MHT
print("********************************************************************************")
print("\tCREATING A MERKLE HASH TREE")
print("********************************************************************************")


btree = Node()
createTree(btree,3)
value_to_store=[3,5,12,34,41,55,90,243]
hashing_tree(btree)

#pretty for printing
modify(btree)
print_tree(btree)



print("\n\n********************************************************************************")
print("\tVERIFYING THAT CLOUD SERVER SEND ME THE VERSION THAT I TRUST IN")
print("\tserver send 30 as the fourth element (a spoofed version of the original)")
print("\twith the proof LV121-LV11-RV2")
print("********************************************************************************")
proof=[['L','5aadb45520dcd8726b2822a7a78bb53d794f557199d5d4abdedd2c55a4bd6ca73607605c558de3db80c8e86c3196484566163ed1327e82e8b6757d1932113cb8'],['L','b6e35da9cebe623f33ab7eb816275f932568f9653cf169768603d31685b77d5c77d47840256569cfb79e25f38fb45f8750bd8b784616ea42d66eb51e8147eabd'],['R','0e6f9ba83aea8502facfd2173c6aaf31ab5607912e48ecbb46b304ff282c27d155f7cf63ec730fcfe2d307073c3d15261acb029c4dabdca6a9547017115145b8']]


proof_hash="30"
hashGen = hashlib.sha512()
hashGen.update(proof_hash.encode('utf-8'))
proof_hash = hashGen.hexdigest()

for x in proof:
	if x[0]=='L':
		proof_hash = x[1]+proof_hash
	else:
		proof_hash = proof_hash+x[1]

	hashGen = hashlib.sha512()
	hashGen.update(proof_hash.encode('utf-8'))
	proof_hash = hashGen.hexdigest()

print("CLOUD ROOT HASH:" + proof_hash)

#verify the last hash
if btree.h==proof_hash :
    print("\nEXCELLENT!!\nWe can belive in cloud server")
else:
    print("\nPAY ATTENTION!\nWe can't belive in cloud server")
