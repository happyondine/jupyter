#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int main(){

printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
printf("<TITLE>See Friends</TITLE>");
printf("<body bgcolor=coral text=white>");


    FILE *fp = fopen("http://www.cs.mcgill.ca/~yoh7/cgi-bin/users.txt", "r");
char line[999];
int count = 0;

while(fgets(line, 100, fp)!=NULL){
	if(count%4 == 0){
		printf("%s", line);
		printf("<form action=http://www.cs.mcgill.ca/~yoh7/cgi-bin/profile.py method=get>");
		printf("<input type=hidden value=%s name=friend>", line);
		printf("<input type=submit value=profile>");
		printf("</form>");
	}
count++;
}



return 0;
}
