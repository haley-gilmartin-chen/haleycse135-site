#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv, char **envp)
{
    printf("Cache-Control: no-cache\n");
    printf("Set-Cookie: username=; expires=Thu, 01 Jan 1970 00:00:00 GMT\n");
    printf("Content-type: text/html\n\n");

    printf("<html>");
    printf("<head><title>C Session Destroyed</title></head>");
    printf("<body>");
    printf("<h1>C Session Destroyed</h1>");
    printf("<a href=\"/cgi-bin/c-sessions-1.cgi\">Back to Page 1</a>");
    printf("<br />");
    printf("<a href=\"/cgi-bin/c-sessions-2.cgi\">Back to Page 2</a>");
    printf("<br />");
    printf("<a href=\"/c-cgiform.html\">Back to Form</a>");
    printf("<br />");
    printf("<a href=\"/\">Back to Home</a>");
    printf("</body>");
    printf("</html>");

    return 0;
}