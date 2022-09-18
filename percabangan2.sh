#!/bin/bash

printf "jajan apa yang kamu suka ?\n"
printf "pentol ?\n"
printf "batagor ?\n"
printf "cireng ?\n"

read jajan

case "jajan" in
	"pentol")
		echo "pentol buk mah wenak slur!"
		;;
	"batagor")
		echo "batagore mas budi mantep bet"
		;;
	"cireng")
		echo "cireng kantin rasanya enak"
		;;
	*)
		echo "makanan yang kamu suka gaenak hehe"
		;;
esac
