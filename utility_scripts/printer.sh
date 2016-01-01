for file in *.txt
do
    awk '{print $1"\t"$2"\t"$3"\t"$4}' $file > $fileOut.txt
    echo $file
done