#!/usr/bin/python

import cgi

form = cgi.FieldStorage()

print "Content-type:text/html\r\n\r\n"

id = form.getvalue('id')

print '<html>'
print '<h1>\r\n'
print '<b>Make Friends Here!</b>\r\n<br>'
print '</h1>\r\n'

print '<body bgcolor="coral" text="white">\r\n'
print '<ul>'


print '<form action="http://cgi.cs.mcgill.ca/~yoh7/cgi-bin/newfriends.py" method="get">\r\n'

print '<input type=hidden value=%s name=id>' %id


with open('http://cgi.cs.mcgill.ca/~yoh7/cgi-bin/users.txt', 'r') as users:
        count = 0
        for line in users:

                if count % 4 == 0: #print check box full name.
                        print '<br>\r\n\r\n <input type="checkbox" name="newusers" value="%s" > \r\n' % line
                        #print line 

                if count % 2 == 0: #full name and username 
                        print '\r\n' + line + '\r\n'
                count+=1



print '<ul>'
print '<br><br><input type="submit" value="submit" >\r\n'


print '</form>\r\n'
print '</body>\r\n'



print '</html>'

