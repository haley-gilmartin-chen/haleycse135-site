#!/usr/bin/perl
print "Cache-Control: no-cache\n";
print "Content-type: text/html \n\n";

print <<END;
<!DOCTYPE html>
<html><head><title>GET Request Echo</title>
</head><body><h1 align="center">Get Request Echo</h1>
<hr>
END

print "<b>Query String:</b> $ENV{QUERY_STRING}<br />\n";

if (length ($ENV{'QUERY_STRING'}) > 0){
  $buffer = $ENV{'QUERY_STRING'};
  @pairs = split(/&/, $buffer);
  foreach $pair (@pairs) {
    ($name, $value) = split(/=/, $pair);
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $in{$name} = $value; 
  }
}

$loop = 0;
foreach my $key (%in) {
  $loop += 1;
  if($loop % 2 != 0) {
    print "$key = $in{$key}<br/>\n";
  }
}

print "</body></html>";
