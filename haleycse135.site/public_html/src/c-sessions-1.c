#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv, char **envp)
{
  // Headers
  printf("Cache-Control: no-cache\n");

  // Get Name from POST data
  char post_data[1000];
  char *name = NULL;
  int content_length;
  char *content_length_str = getenv("CONTENT_LENGTH");
  
  if (content_length_str != NULL) {
    content_length = atoi(content_length_str);
    if (content_length > 0) {
      fgets(post_data, sizeof(post_data), stdin);
      if (strncmp(post_data, "username=", 9) == 0) {
        name = post_data + 9;
        // Remove trailing newline if present
        char *newline = strchr(name, '\n');
        if (newline) *newline = '\0';
      }
    }
  }

  // Set the cookie using a header, add extra \n to end headers
  if (name != NULL && strlen(name) > 0) {
    printf("Content-type: text/html\n");
    printf("Set-Cookie: username=%s\n\n", name);
  } else {
    printf("Content-type: text/html\n\n");
  }

  // Body - HTML
  printf("<html>");
  printf("<head><title>C Sessions</title></head>\n");
  printf("<body>");
  printf("<h1>C Sessions Page 1</h1>");
  printf("<table>");

  // First check for new Cookie, then Check for old Cookie
  if (name != NULL && strlen(name) > 0) {
    printf("<tr><td>Cookie:</td><td>%s</td></tr>\n", name);
  } else {
    char *cookie = getenv("HTTP_COOKIE");
    if (cookie != NULL && strncmp(cookie, "username=", 9) == 0 && strcmp(cookie, "destroyed") != 0) {
      printf("<tr><td>Cookie:</td><td>%s</td></tr>\n", cookie + 9);
    } else {
      printf("<tr><td>Cookie:</td><td>None</td></tr>\n");
    }
  }

  printf("</table>");

  // Links for other pages
  printf("<br />");
  printf("<a href=\"/cgi-bin/c-sessions-2.cgi\">Session Page 2</a>");
  printf("<br />");
  printf("<a href=\"/c-cgiform.html\">C CGI Form</a>");
  printf("<br /><br />");

  // Destroy Cookie button
  printf("<form action=\"/cgi-bin/c-destroy-session.cgi\" method=\"get\">");
  printf("<button type=\"submit\">Destroy Session</button>");
  printf("</form>");

  printf("</body>");
  printf("</html>");
  return 0;
}
