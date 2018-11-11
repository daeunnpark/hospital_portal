#!/usr/bin/env python
import pymysql

def main():

    conn = pymysql.connect(host='10.245.235.98', port=3306, user='root', passwd='hospitalCSE305!', db='hospital')

    cur = conn.cursor()

    cur.execute("SELECT VERSION()")

    print(cur.description)

if __name__ == "__main__": main()