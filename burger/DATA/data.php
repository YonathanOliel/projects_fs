<?php


class DataBase
{

    private static $dbHost = "localhost";
    private static $dbName = "burger_code";
    private static $dbUser = "root";
    private static $dbUserPassword = "";
    private static $conection = null;


    public static function connect()
    {
        try
        {
            self::$conection = new PDO("mysql:host=" . self::$dbHost, "dbname=". self::$dbName, self::$dbUser, self::$dbUserPassword);
        }
        catch(PDOException $e)
        {
            die($e->getMessage());
        }
        return self::$conection;
    }

    public static function disconnect()
    {
        self::$conection = null;

    }
}

DataBase::connect();
echo "conneted";

?>