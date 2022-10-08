# 1

import mysql.connector
import mariadb

print("Enter ICAO code to get the name of the airport: ")
def getAirportNameByIcaoCode(icao_code):
    sql = " select airport_name from airport"
    sql += " where ident ='" + icao_code + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return

connection = mariadb.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='arina',
    password='3790',
    autocommit=True
)

icao_code = input("Enter ICAO code: ")
getAirportNameByIcaoCode(icao_code)


# 2

import mysql.connector
print("Enter the area code code to get the info about the airports in the country: ")
def getAirporsByAreaCode(area_code):
    sql = " select airport_type, airport_name from airport"
    sql += " where iso_country ='" + area_code + "' order by type desc"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='arina',
    password='3790',
    autocommit=True
)

area = input("Enter the area code: ")
getAirporsByAreaCode(area_code)


# 3

from geopy import distance
import mysql.connector

print("Enter the ICAO codes of two airports to get the distance between them: ")
icao_code1 = input("Enter the first ICAO code:")
icao_code2 = input("Enter the second ICAO code:")
def getDistanceByCodes(icao_code1,icao_code2):
    sql = "select latitude_deg, longitude_deg from airport where ident ='" + icao_code1 + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result1 = cursor.fetchall()
    print(result1)
    sql = "select latitude_deg, longitude_deg from airport where ident ='" + icao_code2 + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result2 = cursor.fetchall()
    print(result2)
    return
print(f"The distance between these two airports is {distance.distance(result1, result2).km:.2f} km")

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='arina',
    password=3790,
    autocommit=True
)

distance1 = input("Enter the ICAO code of the first airport: ")
distance2 = input("Enter the ICAO code of the second airport: ")
getAirporsByAreaCode(icao_code1,icao_code2)
