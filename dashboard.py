#!/usr/bin/python

import cgi

form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"

id = form.getvalue('id')

print id

print '<html>'

print '<body bgcolor="coral" text="white">'
print '<center>'
print '<h1>Dashboard</h1>'
print '</center>'
print '<b>MENU</b>'
print '<br><br>'

print '<form action="http://cgi.cs.mcgill.ca/~yoh7">'
print '<input type="submit" value="Click here to Logout">'
print '</form>'

print '<form action="http://cs.mcgill.ca/~yoh7/cgi-bin/makefriends.py" method="get">'
print '<input type=hidden value=%s name=id>' %id
print '<input type="submit" value="Click here to make friends">'
print '</form>'

print '<form action="http://cgi.cs.mcgill.ca/~yoh7/cgi-bin/seefriends.cgi" method=get>'
print '<input type=submit value="see a friend">'
print '</form><br><br>'

print '<h3><b>About me</b></h3>'
print '</html>'

x=0

file = open("http://cs.mcgill.ca/~yoh7/cgi-bin/users.txt", "r")
s = file.readlines()
for line1 in s:
	str1 = line1.rstrip()
	x+=1
	if (str1 == id):
                break
			
y=0

with open("http://cs.mcgill.ca/~yoh7/cgi-bin/users.txt") as file:
        for line2 in file:
                y+=1
                if(y==x):
                        print "USERNAME: "
                        print line2
                        print '<br>'
                elif (y==x+2):
                        print "FULL NAME: "
                        print line2
                        print '<br>'
                elif (y==x+3):
                        print "JOB DESCRIPTION: "
                        print line2
                        print '<br><br><br>'


print '<html>'

print '<br><br>'

print '<b>NEWS FEED</b><br><br>'
print '<form action="http://cs.mcgill.ca/~yoh7/cgi-bin/status.py" method="post">'
print 'Update your status: <input type="text" name="status update">'
print '<input type=hidden value=%s name=id>' %id
print '<input type="submit" value="update">'
print '</form>'



print '</html>'


count = 0

valid_users = None

with open("http://cs.mcgill.ca/~yoh7/cgi-bin/friends.txt") as f:
       for line in f:
                if(line.split(' ', 1)[0] == id):
                       valid_users = line
                       break
		elif(line.split('\n', 1)[0] == id):
			valid_users = line
			break

valid_users2 = valid_users.split()


#f=open('status.txt','r')
#for line in reversed(open("status.txt").readlines()):
#	print line.rstrip()
#	print '<html><h6></h6></html>'
#	count = count + 1
#	if count == 20:
#		break



for line in reversed(list(open("http://cs.mcgill.ca/~yoh7/cgi-bin/status.txt"))):
	count = count + 1
	for a in valid_users2:
		if((line.split(' ', 1)[0] == a) and (line.split(' ',1)[0] != id) ):
			print line
			print '<html><h1></h1></html>'
		if (line.split(' ', 1)[0] == id):
			print line
			print '<html><h1></h1></html>'
	if count == 20:
		break

