Team members: Haley Chen
Grader passcode: CSE135password 
Link: https://haleycse135.site/

Automatic deploy setup: 
- Created a user on droplet called "deploy" and gave ssh key to github in Action Secrets
- Added key to server 
- Created a deploy.yml file and added Action Secrets there

Login info: 
- username: grader
- password: CSE135password

Changes to HTML file after compression:
- I enabled Apache's deflate feature and allowed it to compress HTML files.
- In DevTools, it showed my HTML is being encoded with gzip. 
- The resource size (1.4 kB) was significantly larger than the transfer size (963 B). This allows for faster page loading. 

Removing server header:
- I installed libapache2-mod-security2 and added a custom SecServerSignature and named it CSE135 Server. (I also had to set ServerTokens to Full to do this.) The server name ca be seen in DevTools. 
(Credit: https://www.tecmint.com/change-apache-server-name-to-anything-in-server-headers/)