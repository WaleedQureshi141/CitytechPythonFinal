#Waleed Mustafa Qureshi
#Final Exam

#message class
class message:

    #state
    def __init__(self, a, b, c):
        self.__sender = a
        self.__recipient = b
        self.__text = c

    #getters
    def getSender(self):
        return self.__sender
    def getRecipient(self):
        return self.__recipient
    def getText(self):
        return self.__text

    #setters
    def setSender(self, x):
        self.__sender = x
    def setRecipient(self, x):
        self.__recipient = x
    def setText(self, x):
        self.__text = x

    #behavior
    def displayMessage(self):
        print ('SENDER: %s' %(self.__sender))
        print ('RECIPIENT: %s' %(self.__recipient))
        print ('MESSAGE: %s' %(self.__text))

#email server class
class emailServer:
    
    #state
    def __init__(self, a, b, c):
        self.__name = a
        self.__IPAddress = b
        self.__messageBuffer = c

    #getters
    def getName(self):
        return self.__name
    def getIPAddress(self):
        return self.__IPAddress
    def getMessageBuffer(self):
        return self.__messageBuffer

    #setters
    def setName(self, x):
        self.__name = x
    def setIPAddress(self, x):
        self.__IPAddress = x
    def setMessageBuffer(self, x):
        self.__messageBuffer = x

    #behavior
    def displayMessageCount(self):
        return ('There Are %s Messages On The Email Server' %(len(self.__messageBuffer)))

    def displayEmailServerStatus(self):
        print ('Server Name: %s' %(self.__name))
        print ('Server IP: %s' %(self.__IPAddress))
        print ('Server Message Count: %s' %(len(self.__messageBuffer)))
        if len(self.__messageBuffer) > 0:
            print ('Server Status: GOOD')
        else:
            print ('Server Status: BAD')

    def displayMessages(self):
        print (m1.displayMessage())
        print ()
        print (m2.displayMessage())
        print ()
        print (m3.displayMessage())
        print ()

#objects
#message objects
m1 = message('Professor Locklear', 'Python Class', 'Good Luck On Your Exam Today')
m2 = message('Professor Locklear', 'Python Class', 'Great Job This Semester')
m3 = message('Professor Locklear', 'Python Class', 'Have A Great Summer')
#email server object
eS1 = emailServer('CST1101Server', '127.000.001', ['Good Luck On Your Exam Today', 'Great Job This Semester', 'Have A Great Summer'])

#attributes
print (eS1.displayEmailServerStatus())
print ()
print (eS1.displayMessageCount())
print ()
print (eS1.displayMessages())
    
