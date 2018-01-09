total=0
found=0
for i in $1/* ; do
	total=$((total+1)); 
	if grep -q moveme "$i"; then
        	found=$((found+1));
		mv $i $2/
     	fi
done
echo $found
echo $total
