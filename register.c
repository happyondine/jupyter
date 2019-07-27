#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *output;

char* convert(char *src){
        int a = strlen(src);
        int k,j=0,t=0;
        output = malloc(a+1);
        for(k=5;k<a;k++){
                *(output+j) = *(src+k);
                j++;
        }
        for(t=0;t<a+1;t++){
                if(*(output+t) == '+'){
                        *(output+t) = ' ';
                }
        }
        strcat(output,"\n");
        return output;
}


int main(void){

        char input[50];
        char line[1000];
        char temp[50];
        char *token;
        char *username;
        char *password;
        char *fullname;
		char *job;
        int len = atoi(getenv("CONTENT_LENGTH"));
        printf("%s%c%c\n","Content-Type:text/html;charset=iso-8859-1",13,10);
        printf("<TITLE>register</TITLE>");
        printf("<body bgcolor=coral text=white>");
        if (len == 0){ printf("<p>ERROR: no input</p>");}
        else {
                FILE *fp = fopen("http://www.cgi.cs.mcgill.ca/~yoh7/cgi-bin/users.txt","r+");

                //get the user input!!
                fgets(input, len+2, stdin);
                //printf("<p>Input:%s",input);

                strcpy(temp,input);

                //get all tokens
                username = strtok(input,"&");
                password = strtok(NULL,"&");
                fullname = strtok(NULL,"&");
                job = strtok(NULL,"&");

                //convert
                username = convert(username);
                password = convert(password);
                fullname = convert(fullname);
                job = convert(job);



                /*      
                printf("<p>username:%s</p>",username);
                printf("<p>password:%s</p>",password);
                printf("<p>fullname:%s</p>",fullname);
		printf("<p>job:%s</p>",job);
                int result = strlen(username);
                printf("%d",result);
                */

                // check no input
                if(strlen(username) == 1 || strlen(password) == 1 || strlen(fullname) == 1 || strlen(job) == 1){
                        printf("<p>Error: Missing input</p>");
                        printf("<a href= http://www.cgi.cs.mcgill.ca/~yoh7/login.html> Back to Login page</a>");
                        return 1;
                }


                //check unique id
                else{
                        while(fgets(line,1000,fp) != NULL){
                                if(strcmp(username,line) == 0){
                                        printf("<p>Error: Duplicate Username</p>");
                                        printf("<a href= http://www.cgi.cs.mcgill.ca/~yoh7> Back to Landing page</a></br>");
                                        printf("<a href= http://www.cgi.cs.mcgill.ca/~yoh7/login.html> Back to Login page</a>");
                                        return 1;
                                }

                        }

                }
                //printf("<p>unique ID:%s</p>",username);

// append to the textfile
                if(fp == NULL){
                        printf("<p>ERROR</p>");
                }
                else{
                        fputs(username,fp);
                        fputs(password,fp);
                        fputs(fullname,fp);
                        fputs(job,fp);
                }

                fclose(fp);

                FILE *fp2 = fopen("http://www.cgi.cs.mcgill.ca/~yoh7/public_html/friends.txt","a");
                if (fp2 == NULL){ printf("<p>error</p>");}
                else{
                        fputs(username,fp2);
                }
                fclose(fp2);

                printf("<p>Thank you!</p>");
                printf("<a href= http://www.cgi.cs.mcgill.ca/~yoh7/login.html> Back to Login page</a>");
        }

        return 0;
}

