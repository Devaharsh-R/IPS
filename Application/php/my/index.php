<?php
include("simple_html_dom.php");
$removedTags = file_get_html("https://www.bsnl.co.in/opencms/bsnl/BSNL/services/mobile/prepaid_plans_100822.html");
// $content=htmlspecialchars($html);
// $removedTags="<H1>HELLO WORLD</H1><BR><U>HI</U>";
$removedTags=filter_var($removedTags,FILTER_SANITIZE_STRING);
echo $removedTags;
?>