<?php
    $DATABASE_HOST = "mysql-app";
    $DATABASE_USER = "adminroot";
    $DATABASE_PASS = "welcome123";
    $DATABASE_NAME = "docRegform2";

    $conn = mysqli_connect($DATABASE_HOST, $DATABASE_USER, $DATABASE_PASS, $DATABASE_NAME);

    if(!$conn) {
        echo "Connection Failed";
    }
