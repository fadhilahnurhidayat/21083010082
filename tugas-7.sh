#!/bin/bash

{
	echo "==luas bidang persegi=="
	echo "Masukkan Panjang"
	read panjang
	echo "Masukkan Lebar"
	read lebar
	let luasbidangpersegi=$panjang*$lebar
	echo "Luas persegi :
$luasbidangpersegi"

}
