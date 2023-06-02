from graphics import *


class Button(Rectangle):

    def __init__(self, win, p1, p2, color, text):
        super().__init__(p1, p2)
        super().draw(win)
        super().setFill(color)

        self.minX = p1.getX()
        self.maxX = p2.getX()
        self.minY = p1.getY()
        self.maxY = p2.getY()

        self.text = Text(Point((self.minX + self.maxX)/2, (self.minY + self.maxY)/2), text)
        self.text.draw(win)

    def isClicked(self, p):
        x = p.getX()
        y = p.getY()
        if x > self.minX:
            if x < self.maxX:
                if y > self.minY:
                    if y < self.maxY:
                        return True
        return False

class QuitButton(Button):

    def __init__(self, win, p1, p2, color = "red", text = "Quit"):
        super().__init__(win, p1, p2, color, text)


class EmailInfo:
    def __init__(self):
        self.tone = ''
        self.urgency = ''
        self.authorName = ''
        self.date = ''
        self.purpose = ''
        self.guestName = ''
        self.platform = ''
        self.code = ''

    def getTone(self):
        return self.tone

    def setTone(self, tone):
        self.tone = tone

    def getUrgency(self):
        return self.urgency

    def setUrgency(self, urgency):
        self.urgency = urgency

    def getAuthorName(self):
        return self.authorName

    def setAuthorName(self, authorName):
        self.authorName = authorName

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = date

    def getPurpose(self):
        return self.purpose

    def setPurpose(self, purpose):
        self.purpose = purpose

    def getGuestName(self):
        return self.guestName

    def setGuestName(self, guestName):
        self.guestName = guestName

    def getPlatform(self):
        return self.platform

    def setPlatform(self, platform):
        self.platform = platform

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code
    
    def validate(self):
        message = None

        if self.tone == '':
            message = 'Please select Tone.'
        elif self.urgency == '':
            message = 'Please select Urgency.'
        elif self.authorName == '':
            message = 'Please provide Your Name.'
        elif self.date == '':
            message = 'Please provide the Date, Time.'
        elif self.purpose == '':
            message = 'Please provide the Purpose.'
        elif self.guestName == '':
            message = "Please provide the Guest's Name."
        elif self.platform == '':
            message = 'Please provide the Platform.'
        elif self.code == '':
            message = 'Please provide the Code.'

        return message



        
class EmailGenerator:
    def __init__(self, info):
        self.info = info
        self.template1 = '''
Dear [guestName]:
 
I am writing to request a meeting with you about [purpose].
Given the importance and urgency of this matter, I hope to meet with you on [date].
The meeting details are as follows:
Meeting platform: [platform]
Meeting’s code/link: [code]
As mentioned, this meeting is urgent; therefore, your prompt response would be greatly appreciated.
 
Looking forward to your reply!

 
Best regards,
[authorName]

Wishing you a successful and productive meeting!

'''
        self.template2 = '''
Dear [guestName]:
 
I am writing to request a meeting with you about [purpose].
Given the importance of this matter, I hope to meet with you on [date].
The meeting details are as follows:
Meeting platform: [platform]
Meeting’s code/link: [code]

Looking forward to your reply!

 
Best regards,
[authorName]

Wishing you a successful and productive meeting!
'''
 

        self.template3 = '''
Dear [guestName],                                                                                                                                                                            
 
I hope you are doing fantastic! I have something in mind that I want to share in a meeting, and I believe you will want to hear it!
We will have a meeting about [purpose], and it is going to be really cool if you are able to join.                                  
I plan to meet with you on [date].                                                                                                                                                       
Let’s meet on [platform]. Here is the link to the meeting [code].                                                                           
This is quite urgent, so please respond to me as soon as possible!                                                                            

Looking forward to hearing from you!                                                                                                                                                                                             
 
With love,                                                                                                                                                                                                                                                           
[authorName]                                                                                                                                                                                                                           

Hope your meet-up brings smiles that last a lifetime!               
'''
        self.template4 = '''

Dear [guestName], 
                     
I hope you are doing fantastic! I have something in mind that I want to share in a meeting, and I believe you will want to hear it!
We will have a meeting about [purpose], and it is going to be really cool if you are able to join.  
I plan to meet with you on [date].
Let’s meet on [platform]. Here is the link to the meeting [code]..

Looking forward to hearing from you!

With love,
[authorName]

Hope your meet-up brings smiles that last a lifetime!
'''

    def generate(self):
        template = None
        if self.info.tone == 'Formal' and self.info.urgency == 'Urgent':
            template = self.template1
        if self.info.tone == 'Formal' and self.info.urgency == 'Not Urgent':
            template = self.template2
        if self.info.tone == 'Informal' and self.info.urgency == 'Urgent':
            template = self.template3
        if self.info.tone == 'Informal' and self.info.urgency == 'Not Urgent':
            template = self.template4
        email = template

        email = email.replace('[guestName]', self.info.getGuestName())
        email = email.replace('[authorName]', self.info.getAuthorName())
        email = email.replace('[purpose]', self.info.getPurpose())
        email = email.replace('[platform]', self.info.getPlatform())
        email = email.replace('[code]', self.info.getCode())
        email = email.replace('[date]', self.info.getDate())
    
        return email
            
        
        
def main():

    win = GraphWin("Graph Example", 1000, 1000)
    #buttons
    Quit = Button(win, Point(20, 370), Point(100, 430), "red2", "Quit")
    Reset = Button(win, Point(120, 370), Point(200, 430), "red2", "Reset")
    Generate = Button(win, Point(20, 270), Point(100, 330), "SlateBlue1", "Generate")
    Urgent = Button(win, Point(20, 170), Point(100, 230), "plum1", "Urgent")
    NotUrgent = Button(win, Point(120, 170), Point(200, 230), "plum1", "Not Urgent")
    Formal = Button(win, Point(20, 70), Point(100, 130), "plum1", "Formal")
    Informal = Button(win, Point(120, 70), Point(200, 130), "plum1", "Informal")


    T1 = Text(Point(40, 60), "1. Tone")
    T1.draw(win)
    T1.setFace("times roman")
    T1.setTextColor("MediumPurple2")
    T1.setSize(15)

    T2 = Text(Point(53, 160), "2. Urgency")
    T2.draw(win)
    T2.setFace("times roman")
    T2.setTextColor("MediumPurple2")
    T2.setSize(15)
    
    T3 = Text(Point(731, 50), "3. Your name ")
    T3.draw(win)
    T3.setFace("times roman")
    T3.setTextColor("MediumPurple2")
    T3.setSize(15)
    E3 = Entry(Point(800, 70), 30)
    E3.draw(win)
    

    T4 = Text(Point(730, 150), "4. Date, Time ")
    T4.draw(win)
    T4.setFace("times roman")
    T4.setTextColor("MediumPurple2")
    T4.setSize(15)
    E4 = Entry(Point(800, 170), 30)
    E4.draw(win)

    T5 = Text(Point(755, 250), "5. Meeting's Purpose ")
    T5.draw(win)
    T5.setFace("times roman")
    T5.setTextColor("MediumPurple2")
    T5.setSize(15)
    E5 = Entry(Point(800, 270), 30)
    E5.draw(win)

    T6 = Text(Point(740, 350), "6. Guest's name ")
    T6.draw(win)
    T6.setFace("times roman")
    T6.setTextColor("MediumPurple2")
    T6.setSize(15)
    E6 = Entry(Point(800, 370), 30)
    E6.draw(win)

    T7 = Text(Point(749, 450), "7. Social Platform ")
    T7.draw(win)
    T7.setFace("times roman")
    T7.setTextColor("MediumPurple2")
    T7.setSize(15)
    E7 = Entry(Point(800, 470), 30)
    E7.draw(win)

    T8 = Text(Point(760, 550), "8. Meeting's code/link ")
    T8.draw(win)
    T8.setFace("times roman")
    T8.setTextColor("MediumPurple2")
    T8.setSize(15)
    E8 = Entry(Point(800, 570), 30)
    E8.draw(win)

    Text1 = Text(Point(500, 20), "Generate email")
    Text1.setSize(30)
    Text1.setFace("times roman")
    Text1.setTextColor("MediumPurple4")
    Text1.draw(win)

    noti = Text(Point(100, 450), "")
    noti.setFace("times roman")
    noti.setTextColor("red3")
    noti.draw(win)

    Text2 = Text(Point(550, 700), "")
    Text2.setSize(15)
    Text2.setFace("times roman")
    Text2.draw(win)
    Text2._reconfig("justify", "left")

    info = EmailInfo()
    while True:
        m = win.getMouse()
        if Quit.isClicked(m):
            win.close()
            break
       
        if Formal.isClicked(m):
            info.setTone("Formal")
            Formal.setFill('pink')
            Informal.setFill('plum1')
        if Informal.isClicked(m):
            info.setTone("Informal")
            Informal.setFill('pink')
            Formal.setFill('plum1')
        if Urgent.isClicked(m):
            info.setUrgency("Urgent")
            Urgent.setFill('pink')
            NotUrgent.setFill('plum1')
        if NotUrgent.isClicked(m):
            info.setUrgency("Not Urgent")
            NotUrgent.setFill('pink')
            Urgent.setFill('plum1')
            

        if Generate.isClicked(m):
            info.setAuthorName(E3.getText())
            info.setDate(E4.getText())
            info.setPurpose(E5.getText())
            info.setGuestName(E6.getText())
            info.setPlatform(E7.getText())
            info.setCode(E8.getText())

            message = info.validate()

            if message != None:
                noti.setText(message)
            else:
                generator = EmailGenerator(info)
                email = generator.generate()
                Text2.setText(email)
                print(email)

              
        if Reset.isClicked(m):
            info = EmailInfo()
            Formal.setFill('plum1')
            Informal.setFill('plum1')
            Urgent.setFill('plum1')
            NotUrgent.setFill('plum1')
            E3.setText('')
            E4.setText('')
            E5.setText('')
            E6.setText('')
            E7.setText('')
            E8.setText('')
            Text2.undraw()
            noti.undraw()
            
            
            
           












if __name__ == "__main__":
    main()
