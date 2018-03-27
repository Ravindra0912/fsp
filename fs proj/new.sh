#!/bin/bash
var = ' '
while IFS='' read -r line || [[ -n "$line" ]]; do
    var.= $var$line
done < "$1"
