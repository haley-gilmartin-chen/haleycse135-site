#!/usr/bin/perl
use CGI;
use CGI::Session;
$session = new CGI::Session("driver:File", undef, {Directory=>"/tmp"});
$cgi = CGI->new;
$cookie = $cgi->cookie(CGISESSID => $session->id);
print $cgi->header( -cookie=>$cookie );

my $name = $session->param('username') || $cgi->param('username');
$session->param("username", $name);

print "<html>";
print "<head>";
print "<title>Perl Sessions</title>";
print "</head>";
print "<body>";
print "<h1>Perl Sessions Page 1</h1>";
if ($name){
	print("<p><b>Name:</b> $name");
}else{
	print "<p><b>Name:</b> You do not have a name set</p>";
}
print "<br/><br/>";
print "<a href=\"/cgi-bin/perl-sessions-2.pl\">Session Page 2</a><br/>";
print "<a href=\"/perl-cgiform.html\">Perl CGI Form</a><br />";
print "<form style=\"margin-top:30px\" action=\"/cgi-bin/perl-destroy-session.pl\" method=\"get\">";
print "<button type=\"submit\">Destroy Session</button>";
print "</form>";
print "</body>";
print "</html>";
