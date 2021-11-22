#Import windows 32 client
import os
import win32com.client as client

name1 = "Conrad"
name2 = "Samson"
email1 = "conrad@attabotics.com"
email2 = "samson@attabotics.com"

#Create Outlook Object
outlook = client.Dispatch('Outlook.Application')

#Email Client
account = outlook.Session.Accounts['fika@attabotics.com']

#Create message object
message = outlook.CreateItem(0)
message.Display()
message.To = email1 + "; " + email2
message.Subject = '[Fika] - Your match for this week!'
message.Body = "Hello " + name1 + " and " + name2 + "! You have been matched for this week! Please see the schedule request! THIS IS A TEST"
message._oleobj_.Invoke(*(64209, 0, 8, 0, account))
message.Display()
message.Save()
message.Send()

#Create meeting
meeting = outlook.CreateItem(1)
meeting.Start = "2021-11-26 10:45"
meeting.Subject = "Friday Fika with " + name1 + " and " + name2 + "!"
meeting.Duration = 15
meeting.Location = "Virtual Meeting"
meeting.MeetingStatus = 1
meeting.Recipients.Add(email1)
meeting.Recipients.Add(email2)
meeting.Recipients.ResolveAll()

meeting.Send()