inputFile=file.txt

totalLine=$(awk 'END{print NR}' $inputFile)

if [ $totalLine -lt 10 ]; then
	exit 0
fi

head -n 10 $inputFile | tail -n 1