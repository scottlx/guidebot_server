<?php

function locate_val($key) {
    $a = array();
    $a["servername"] = "localhost"; //mysql servername
    $a["username"] = "root"; //mysql username
    $a["password"] = "0801iamAndersen"; //mysql password
    $a["databasename"] = "map"; //mysql database
    if(!array_key_exists($key,$a)) {
        die("locate value does not exist [$key]");
    }
    return $a[$key];
}
