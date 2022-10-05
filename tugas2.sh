#!/bin/bash

echo "==============DAFTAR BARANG=============="
echo "1. Velg OZ Racing KW Super (1000000)"
echo "2. Shock OHLINS KW Super (1500000)"
echo "3. Rem Brembo KW Super (500000)"
echo "4. Kaliper Brembo KW Super (1500000)"
echo "5. Stabilizer OHLINS KW Super (500000)"
echo "========================================="

read -p "Mau menghabiskan uang berapa hari ini: " pil;

if [ $pil -eq 1 ]; 
then
   echo "Masukkan Jumlah Bos:";

read jum1

let bayar=jum1*1000000

elif [ $pil -eq 2 ]; 
then
   echo "Masukkan Jumlah Bos:";

read jum2

let bayar=jum2*1500000

elif [ $pil -eq 3 ]; 
then
   echo "Masukkan Jumlah Bos:";

read jum3

let bayar=jum3*500000

elif [ $pil -eq 4 ]; 
then
   echo "Masukkan Jumlah Bos:"; 

read jum4

let bayar=jum4*1500000

elif [ $spil -eq 5 ];
then
	echo "Masukkan Jumlah Bos:";
read jum5

let bayar=jum5*500000
else
   echo "Maaf menu yang anda pilih tidak tersedia";
fi
   echo "Uang yang harus anda bayarkan: Rp.$bayar"
