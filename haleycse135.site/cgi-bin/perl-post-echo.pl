#!/usr/bin/perl
print "Cache-Control: no-cache\n";
print "Content-type: text/html \n\n";

print <<END;
<!DOCTYPE html>
<html><head><title>POST Request Echo</title>
</head><body><h1 align="center">POST Request Echo</h1>
<hr>
END

my $bytes_read = read STDIN, my $form_data, $ENV{CONTENT_LENGTH};

if (length ($form_data) > 0){
  $buffer = $form_data;
  @pairs = split(/&/, $buffer);
  foreach $pair (@pairs) {
    ($name, $value) = split(/=/, $pair);
    $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
    $in{$name} = $value;
  }
}

print "<b>Message Body:</b><br />\n";
print "<ul>\n";

$loop = 0;
foreach my $key (%in) {
  $loop += 1;
  if($loop % 2 != 0) {
    print "<li>$key = $in{$key}</li>\n";
  }
}

print "</ul>\n";
print "</body></html>\n";
