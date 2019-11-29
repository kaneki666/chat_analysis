from Sender import Sender
def fullMessageDivide(line):    
    splitLine = line.split(' - ') 
    
    dateTime = splitLine[0] 
    
    date, time = dateTime.split(', ')
    
    message = ' '.join(splitLine[1:])
    
    if Sender(message): 
        splitMessage = message.split(': ') 
        author = splitMessage[0] 
        message = ' '.join(splitMessage[1:]) 
    else:
        author = None
    return date, time, author, message
