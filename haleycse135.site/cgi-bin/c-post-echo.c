#include "stdio.h"
#include "stdlib.h"

int main(int argc, char **argv, char **envp)
{
  char str[1000];
  printf("Cache-Control: no-cache\n");
  printf("Content-type: text/html\n\n");
  printf("<html><head><title>POST Message Body</title></head>\
\t<body><h1 align=center>POST Message Body</h1>\
  \t<hr/>\n");

  printf("Message Body: %s\n<br/>", fgets(str, 1000, stdin));

  printf("</body>");
  printf("</html>");
  return 0;
}
