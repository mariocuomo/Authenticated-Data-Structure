# Authenticated Data Structure
How to verify that the data stored in the cloud are real and have not been modified by the server or by a malicious user?<br>
Using **Authenticated Data Structures**! 


`authenticated_list.py` uses _authenticated list_.<br>
An authenticated list is a linked list.<br>
A node of the linked list, in addition to the construction and value fields, contains a field _h_. This is the _cryptographic hash_ of the node value in combination with the cryptographic hash of the previous node.<br>
The client locally saves the value of _h_ while the authenticated data structure (ADS) is saved on the cloud server. The _h_ value is used as evidence to identify data tampering on the cloud.

