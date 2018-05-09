#!/usr/bin/env python3

import psycopg2

DBNAME = "news"

# What are the most popular three articles of all time?
db = psycopg2.connect("dbname=news")
c = db.cursor()
query1 = "select articles.title, count(*) as nums \
            from articles join log \
            on articles.slug = substring(log.path, 10) \
            where status = '200 OK' \
            group by articles.title \
            order by nums desc limit 3; "
query2 = "select authors.name, count(*) as nums \
            from authors join \
            (articles join log on articles.slug = substring(log.path, 10)) \
            on authors.id = articles.author \
            where status = '200 OK' \
            group by authors.name \
            order by nums desc; "
query3 = "select date, ratio || '%' as percentage \
            from  \
            (select errors.date, round(cast (errors.error as \
            decimal(18,2))/cast(requests.total as decimal(18,2))*100,2) \
            as ratio \
            from errors join requests \
            on errors.date = requests.date) as foo \
            where ratio > 1 \
            group by date, percentage; "
c.execute(query1)
rows1 = c.fetchall()

print "What are the most popular three articles of all time?"
for row in rows1:
    print "  ", row[0], row[1]

c.execute(query2)
rows2 = c.fetchall()

print "Who are the most popular article authors of all time?"
for row in rows2:
    print "  ", row[0], row[1]

c.execute(query3)
rows3 = c.fetchall()

print "On which days did more than 1% of requests lead to errors?"
for row in rows3:
    print "  ", row[0], row[1]

db.close()
