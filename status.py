#!/usr/bin/python

import cgi, cgitb

form = cgi.FieldStorage()

update = form.getvalue('status update')
username = form.getvalue('id')

if update != None:
	status_update = open("status.txt","a")
	status_update.write(username)
	status_update.write(" : ")
	status_update.write(update)
	status_update.write("\r\n")
	status_update.close()

#with open("friends.txt") as f:
#	for line in f:
#		if(line.split(' ', 1)[0] == username):
#			valid_users = line
#				break

#valid_users2 = valid_users.split()


print "Content-type:text/html\r\n\r\n"

print '<html><body bgcolor="coral" text="white"><a href="http://cgi.cs.mcgill.ca/~yoh7/cgi-bin/dashboard.py"><font color="FFFFFF">Click to see Updated Dashboard</a></body></html>'


print '<form action="http://cgi.cs.mcgill.ca/~yoh7/cgi-bin/dashboard.py" method="get">'
print '<input type=hidden value=%s name=id>'%username
print '<input type="submit" value="see updated dashboard">'

