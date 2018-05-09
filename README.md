# Logs Analysis

## Table of Contents

* news-log-analysis.py
* Example-of-output

## Requirements
* python 3.XX

## Run it
* Open the file `news-log-analysis.py` with terminal. In the window, put the cmd "python news-log-analysis.py", then you will see the output of the program.

## Edit it
* Open file with IDLE.

## create view
* create view errors to count the nums of requests lead to errors
    ```
    create view errors as
    select log.time::date as date, count(*) as error
    from log
    where status = '404 NOT FOUND'
    group by date;
    ```

* create view requests to count the nums of all requests
    ```
    create view requests as
    select log.time::date as date, count(*) as total
    from log
    group by date;
    ```
