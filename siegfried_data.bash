#! /bin/bash

files=~/Data/DSpace_Data_Mirror/ZIP
output=~/Data/File_Format_Analyses

for i in $(ls $files)
do
# Sort out incorrectly named files
if [ ${#i} -ge 8 ]; then
    continue;
fi
# Check if it is actually a directory
verdict=$(file ${files}/$i | cut -d ':' -f 2)
# echo ${verdict:0:8}
if [ "directo" == ${verdict:0:8} ]
then 
    file_name_part="$(echo $i | awk '{print tolower($0)}')"
    sf -csv -sig deluxe.sig ${files}/$i/ >> ${output}/'siegfried_deluxe_'$file_name_part.csv # ohne -sig deluxe.sig und Dateiname default
fi
echo $i
done