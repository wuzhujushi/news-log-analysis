# Logs Analysis

## Table of Contents

* news-log-analysis.py

## Requirements
* python 3.XX

## Run it
* Open the file `ententainment_center.py` with IDLE. In the window, select Run option of menu, then select Run Module to run the script. The page will load in your default webbrowser.

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
