//login
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void){

        printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);

        char user[11]; // only allowed 10 characters as an input.. see login.html
        char pass[11];

        char c;
        int a = 0;
        int len = atoi(getenv("CONTENT_LENGTH"));
        char string[200];
        printf("<p> length is %d <p>",len);


        while( (c=getchar()) != EOF && a<len){
                string[a] = c;
                c = getchar();
                a++;
                    printf("<p> char is %c <p>",c);
       }
        string[a] = '\0';

        printf("<p> string is %s <p>",string);
}