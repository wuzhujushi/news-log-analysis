# Logs Analysis

## Table of Contents

* news-log-analysis.py
* Example-of-output.txt

## Requirements
* python 3.XX

## Run it

### Installing the Virtual Machine

##### Use a terminal
You'll be doing these exercises using a Unix-style terminal on your computer. If you are using a **Mac or Linux** system, your regular terminal program will do just fine. On **Windows**, we recommend using the **Git Bash** terminal that comes with the Git software. If you don't already have Git installed, download Git from [git-scm.com](https://git-scm.com/downloads).

##### Install VirtualBox
Download VirtualBox from [virtualbox.org.](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1Install) the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.
Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

##### Install Vagrant
Download vagrant from [vagrantup.com.](https://www.vagrantup.com/downloads.html)Install the version for your operating system.
**Windows users:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

![](https://s3.cn-north-1.amazonaws.com.cn/u-img/a0a8f8ed-a91f-4f49-9c63-f3cf9a5155f4)
If Vagrant is successfully installed, you will be able to run `vagrant --version`
in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the `$` sign is the shell prompt.

##### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.
![](https://s3.cn-north-1.amazonaws.com.cn/u-img/b8421e2f-0ca2-4c14-8c7b-2d8c554997da)
Starting the Ubuntu Linux installation with `vagrant up`.
This screenshot shows just the beginning of many, many pages of output in a lot of colors.

When `vagrant up` is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!
![](https://s3.cn-north-1.amazonaws.com.cn/u-img/c793524e-fbbd-49a9-8bc3-8776ec92f00d)
Logging into the Linux VM with `vagrant ssh`.

### Running the data

##### Download the data
Next, [download the data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called `newsdata.sql`. Put this file into the `vagrant` directory, which is shared with your virtual machine.

##### Load the data
To load the data, `cd` into the `vagrant` directory and use the command `psql -d news -f newsdata.sql`.
Here's what this command does:
* psql — the PostgreSQL command line program
* -d news — connect to the database named news which has been set up for you
* -f newsdata.sql — run the SQL statements in the file newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### create view
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

### Running the program
Open the file `news-log-analysis.py` with terminal. In the window, run the cmd `python news-log-analysis.py`, then you will see the output of the program.

## Edit it
* Open the file `news-log-analysis.py` with IDLE.
* Open the file `Example-of-output.txt` with notepad or other unformatted editor.
