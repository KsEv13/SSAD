# 0010 Cipher
## Credits
*Amina Khusnutdinova and Kseniya Evdokimova*
---------------------------------------------------
## The description
#### **What does the program "0010 cipher" do?**
The program receives *a string written in Latin letters* as an *input*. At the *output*, the user receives a code - *an encrypted string*.
The principle of encryption :
1. Each letter in the string is assigned a number (in our version, the number = the ordinal number of the letter in the Latin alphabet).
``` number = string.ascii_lowercase.index(word[i].lower()) ```
2. The program returns the letters "disguised as numbers" in the reverse order in which they were in the message.
-------------------------------------------------------------------
## The objective of the program
#### **Why did we create this project?**
We are a team of scouts who need to exchange secret messages frequently. If such messages fall into the hands of other spies, a political conflict may occur. We needed a tool that could encrypt messages quickly and very accurately.
#### **What problems does the 0010 cipher solve?**
Our intelligence team was constantly faced with the problem of encrypting messages.
It is not easy in extreme conditions, under the surveillance of other agents, to quickly classify important data. Very often, we received messages with errors due to the fact that our team members independently tried to classify the data, which affected the effectiveness of decryption.
With the help of 0010 cipher, we began to receive accurate data very quickly and solved the problem with distorted information.
-----------------------------------------------------------
## How to start?
### Input - any English string 
### Output - cipher in numbers
#### Input: ``` Innopolis```
#### Output: ``` 19 9 12 15 16 15 14 14 9 ```
