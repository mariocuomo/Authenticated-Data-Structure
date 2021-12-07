# Authenticated Data Structure
How to verify that the data stored in the cloud are real and have not been modified by the server or by a malicious user?<br>
Using **Authenticated Data Structures**! 

<br>

## Authenticated Linked List

`authenticated_list.py` uses _authenticated list_.<br>
An authenticated list is a linked list.

<div align="center">
  <img src="https://github.com/mariocuomo/Authenticated-Data-Structure/blob/main/linked_list.png" width="800"/>
</div>

A node of the linked list, in addition to the construction and value fields, contains a field _h_. This is the _cryptographic hash_ of the node value in combination with the cryptographic hash of the previous node.<br>
The client locally saves the value of _h_ while the authenticated data structure (ADS) is saved on the cloud server. The _h_ value is used as evidence to identify data tampering on the cloud.<br>
To verify the correctness of the data it is necessary to build the entire linked list.<br>
Cost: O(n)

<div align="center">
  <img src="https://github.com/mariocuomo/Authenticated-Data-Structure/blob/main/example1.png" width="800"/>
</div>


<br>

## Merkle Hash Tree (MHT)

`merkle_hash_tree.py` uses _Markle Hash Tree_.<br>
A MHT is a balanced binary tree.<br>
Each node contains a hash of the combination of the child nodes. 

<div align="center">
  <img src="https://github.com/mariocuomo/Authenticated-Data-Structure/blob/main/mht.jpg" width="600"/>
</div>

The client locally saves the value of _h_ while the authenticated data structure (ADS) is saved on the cloud server. The _h_ value is used as evidence to identify data tampering on the cloud.<br>
To verify the correctness of the data it is necessary to construct the path from the leaf node to the root. The cloud server proposes the information to reconstruct this path. <br>
Cost: O(log n) 

<div align="center">
  <img src="https://github.com/mariocuomo/Authenticated-Data-Structure/blob/main/example2.png" width="800"/>
</div>
