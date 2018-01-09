R=$(awk -v min=1 -v max=100 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
attemps_left=10
found=0
for i in `seq 10`
do
	read -p "Guess: " guess
	if [ "$R" -gt "$guess" ]
	then
    		echo "Thinks > $guess"
	elif [ "$R" -lt "$guess" ]
	then
		echo "Thinks < $guess"
	elif [ "$R" -eq "$guess" ]
	then
		echo "Victory!!!"
		found=1
		break
	fi
	attemps_left=$((attemps_left-1));
	echo "Attemps remaining:$attemps_left"
done
if [ "$found" -eq "0" ]
then
	echo "$R"
fi
