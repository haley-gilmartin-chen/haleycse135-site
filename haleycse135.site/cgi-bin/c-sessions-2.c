#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv, char **envp)
{
  printf("Cache-Control: no-cache\n");
  printf("Content-type: text/html\n\n");

  printf("<html>");
  printf("<head><title>C Sessions</title></head>\n");
  printf("<body>");
  printf("<h1>C Sessions Page 2</h1>");
  printf("<table>");

  char *cookie = getenv("HTTP_COOKIE");
  if (cookie != NULL && strncmp(cookie, "username=", 9) == 0 && strcmp(cookie, "destroyed") != 0) {
    printf("<tr><td>Cookie:</td><td>%s</td></tr>\n", cookie + 9);
  } else {
    printf("<tr><td>Cookie:</td><td>None</td></tr>\n");
  }

  printf("</table>");
  printf("<br />");
  printf("<a href=\"/cgi-bin/c-sessions-1.cgi\">Session Page 1</a>");
  printf("<br />");
  printf("<a href=\"/c-cgiform.html\">C CGI Form</a>");
  printf("<br /><br />");
  printf("<form action=\"/cgi-bin/c-destroy-session.cgi\" method=\"get\">");
  printf("<button type=\"submit\">Destroy Session</button>");
  printf("</form>");
  printf("</body>");
  printf("</html>");
  return 0;
}