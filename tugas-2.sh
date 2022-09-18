#!/bin/bash
clear

var1=8
var2=4

echo "var1 = $var1"
echo "var2 = $var2"

expr $var1 + $var2
expr "$var1 - $var2"
expr $var1*$var2
expr $var1 / $var2
expr $var1 % $var2
a=$(expr 12 - 1)
echo $a
