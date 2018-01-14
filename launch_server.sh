#!/bin/bash

NAME="AnaViz"
BASEDIR=$(dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ))
FLASKDIR=$BASEDIR"/AnaViz/"
NUM_WORKERS=3
NUM_THREADS=2
NUM_CONNECTIONS=2048
LOG_FILE=$FLASKDIR"logs/gunicorn_log.log"
ERROR_LOG_FILE=$FLASKDIR"logs/gunicorn_error.log"
ACCESS_LOG_FILE=$FLASKDIR"logs/gunicorn_access.log"
IP_PORT="127.0.0.1:9900"

echo "Starting $NAME on $IP_PORT"

export PYTHONPATH=$FLASKDIR:$PYTHONPATH

gunicorn  \
  --bind $IP_PORT \
  --name $NAME \
  --workers $NUM_WORKERS \
  --threads $NUM_THREADS \
   --worker-connections $NUM_CONNECTIONS \
  --log-level=debug \
  --log-file $LOG_FILE \
  --error-logfile $ERROR_LOG_FILE \
  --access-logfile $ACCESS_LOG_FILE \
  --limit-request-line 0 \
  application:application
