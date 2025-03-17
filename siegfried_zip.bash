#! /bin/bash

files=~/Data/DSpace_Data_Mirror/ZIP
output=~/Data/File_Format_ZIP_Analyses

for i in $(ls $files)
do
echo $i
sf -z -csv  ${files}/$i >> ${output}/'siegfried_default_'$i.csv # -sig deluxe.sig and don't forget to change the name...
done