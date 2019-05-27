#!/bin/bash

find java python shell -type f \
    | xargs grep 'https' \
    | awk '{ print $NF }' \
    | sort
