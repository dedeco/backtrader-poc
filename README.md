# Backtrader - Prova de conceito

1. How do I get set up? Set up Install python 3.x and Create a virtualenv:
    [See here how to](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/)

2. Create and running virtualenv
    ```
    user@server:~$ virtualenv -p python3 backenv
    user@server:~$ source backenv/bin/activate
    ```
3. Install all requeriments to use:
    ```
    (bmat) user@server:~$ pip install -r requirements.txt
    ```
4.  Running some strategy feeding from database
    ```
    (bmat) user@server:~$ python run_stat_bitmex_from_db.py
    ```
5.  Running some strategy feeding from CSV file
    ```
    (bmat) user@server:~$ python run_stat_goog.py
    ```
6.  Executing some query and add some data just like test
    ```
    (bmat) user@server:~$ python actions.py
    ```