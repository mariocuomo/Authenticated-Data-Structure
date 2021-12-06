import hashlib

#DATA STRUCTURES
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

class Node:
    def __init__(self, data):
        self.data = data
        self.h = ""
        self.next = None
        self.prev = None






value_to_store=[12,34,5,243,3,41,90]

print("\nTHIS IS THE LIST TO SAVE IN A CLOUD SERVER")
for value in value_to_store:
    print(str(value)+" ", end="")
print("\n")





#CREATE AUTHENTICATED LIST
print("**********************************************************")
print("\tCREATING AN AUTHENTICATED LIST")
print("**********************************************************")
l_list = LinkedList()


for value in value_to_store:
    if l_list.head==None :
        node = Node(str(value))
        l_list.head=node
        l_list.tail=node
        stringToEncode = node.data

    else:
        node = Node(str(value))
        node.prev=l_list.tail
        l_list.tail.next=node
        l_list.tail=node
        stringToEncode = node.prev.h+node.data


    hashGen = hashlib.sha512()
    hashGen.update(stringToEncode.encode('utf-8'))
    hash = hashGen.hexdigest()
    
    node.h = hash


#SAVE LOCALLY ONLY TRUSTED ROOTHASH
trusted_root_hash=l_list.tail.h


for node in l_list:
    print("VALUE: "+node.data+"\n"+"HASH: "+node.h)
    print("-------")
print("\nTRUSTED ROOT HASH: " + trusted_root_hash)
print("\n")




print("**********************************************************")
print("\tADDING A NEW VALUE TO LIST AND UPDATE ADS")
print("\tnote that there aren't changes to old hash values")
print("**********************************************************")
#APPEND NEW DATA: cost O(1), append at the end of the linked list
value_to_store.append(120)
node = Node(str(120))
node.prev=l_list.tail
l_list.tail.next=node
l_list.tail=node
stringToEncode = node.prev.h+node.data
hashGen = hashlib.sha512()
hashGen.update(stringToEncode.encode('utf-8'))
hash = hashGen.hexdigest()
node.h = hash


#UPDATE TRUSTED ROOTHASH
trusted_root_hash = l_list.tail.h


for node in l_list:
    print("VALUE: "+node.data+"\n"+"HASH: "+node.h)
    print("-------")
print("\nTRUSTED ROOT HASH: " + trusted_root_hash)
print("\n")



#UPDATE AN ELEMENT: cost O(1), if the element is the last one
print("**********************************************************")
print("\tUPDATING THE LAST VALUE")
print("\tnote that there aren't changes to old hash values - only for the last one")
print("**********************************************************")
value_to_store[7]=1
l_list.tail.data=str(value_to_store[7])
stringToEncode = l_list.tail.prev.h+l_list.tail.data
hashGen = hashlib.sha512()
hashGen.update(stringToEncode.encode('utf-8'))
hash = hashGen.hexdigest()
l_list.tail.h = hash


#UPDATE TRUSTED ROOTHASH
trusted_root_hash = l_list.tail.h


for node in l_list:
    print("VALUE: "+node.data+"\n"+"HASH: "+node.h)
    print("-------")
print("\nTRUSTED ROOT HASH: " + trusted_root_hash)
print("\n")


#UPDATE AN ELEMENT: cost O(n), if the element is the first one
print("**********************************************************")
print("\tUPDATING THE FIRST VALUE")
print("\tnote that we have to change all hash values")
print("**********************************************************")
value_to_store[0]=86
l_list.head.data=str(value_to_store[0])
for node in l_list:
    stringToEncode = node.data
    if node.prev!=None:
        stringToEncode = node.prev.h + stringToEncode

    hashGen = hashlib.sha512()
    hashGen.update(stringToEncode.encode('utf-8'))
    hash = hashGen.hexdigest()
    
    node.h = hash


#UPDATE TRUSTED ROOTHASH
trusted_root_hash = l_list.tail.h

for node in l_list:
    print("VALUE: "+node.data+"\n"+"HASH: "+node.h)
    print("-------")
print("\nTRUSTED ROOT HASH: " + trusted_root_hash)
print("\n")


#TO VERIFY DATA ON CLOUD, WE NEED THE ENTIRE DATA STRUCTURE
print("**********************************************************")
print("\tVERIFYING THAT CLOUD SERVER SEND ME THE VERSION THAT I TRUST IN")
print("\tserver send [86,34,5,243,3,41,80,1] (a spoofed version of the original)")
print("**********************************************************")
# real value : [86,34,5,243,3,41,90,1]
spoofed_value_from_cloud=[86,34,5,243,3,41,80,1]
client_list = LinkedList()
for value in spoofed_value_from_cloud:
    if client_list.head==None:
        node = Node(str(value))
        client_list.head=node
        client_list.tail=node
        stringToEncode = node.data

    else:
        node = Node(str(value))
        node.prev=client_list.tail
        client_list.tail.next=node
        client_list.tail=node
        stringToEncode = node.prev.h+node.data


    hashGen = hashlib.sha512()
    hashGen.update(stringToEncode.encode('utf-8'))
    hash = hashGen.hexdigest()
    
    node.h = hash


for node in client_list:
    print("VALUE: "+node.data+"\n"+"HASH: "+node.h)
    print("-------")
print("\n")


print("TRUSTED ROOT HASH: " + trusted_root_hash)
print("CLOUD ROOT HASH:" + client_list.tail.h)

#verify the last hash
if trusted_root_hash==client_list.tail.h :
    print("\nEXCELLENT!!\nWe can belive in cloud server")
else:
    print("\nPAY ATTENTION!\nWe can't belive in cloud server")