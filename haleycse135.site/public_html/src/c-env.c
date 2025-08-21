#include "stdio.h"
#include "stdlib.h"

int main(int argc, char **argv, char **envp)
{
  printf("Cache-Control: no-cache\n");
  printf("Content-type: text/html\n\n");
  printf("<html><head><title>Environment Variables</title></head> \
\t<body><h1 align=center>Environment Variables</h1> \
  \t<hr/>\n");

  for (char **env = envp; *env != 0; env++)
  {
    char *thisEnv = *env;
    printf("%s\n<br/>", thisEnv);
  }

  printf("</body></html>");
  return 0;
}
