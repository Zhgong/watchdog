# watchdog

simple program to watch if the file was changed recently

## Function

* minitor file
* check time stamp of file
* ff the time difference to current time has exeeded a limit
* execute command

## How to install

```sh
pipenv install
```

## Run under command line

```sh
python watchdog.py <FILE-TO-MONITOR> <SECONDS> ["dummy restart service"]
```

## Add to Crontab