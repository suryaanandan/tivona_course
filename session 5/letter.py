# Question 7

import sys

class  Letter(object):
 
    def __init__(self, sender_name, sender_address, recipient_name, recipient_address, subject,  body, signature):
        self. sender_name = sender_name
        self.sender_address = sender_address
        self.recipient_name = recipient_name
        self.recipient_address = recipient_address
        self.subject = subject
        self.body = body
        self.signature = signature


    def compose(self):

        print("\n\nFrom : \n\n{} \n{}\n\nTo: \n\n{}\n{}".format("".join(self.sender_name), "".join(self.sender_address), "".join(self.recipient_name), "".join(self.recipient_address)))


        print("Subject : {}\n\t{}\n{}".format("".join(self.subject), "".join(self.body), "".join(self.signature)))

# Tests for the class Letter
print("\n Please enter all the details needed to send post")
sender_name = (str)(input("Enter sender name : "))
print("Enter sender address : ")
sender_address = sys.stdin.readlines()
recipient_name = (str)(input("Enter recipient name : "))
print("Enter recipient address : ")
recipient_address = sys.stdin.readlines()
subject = (str)(input("Enter post subject : "))
print("Enter body of the post : ")
body = sys.stdin.readlines()
print("Enter signature : ")
signature = sys.stdin.readlines()
send_letter = Letter(sender_name, sender_address, recipient_name, recipient_address, subject, body, signature)
send_letter.compose()

