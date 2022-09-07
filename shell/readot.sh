shell

read -p "Please enter your option:" option
if [ "$option" == "1" ]; then
      echo "test 1"
elif [ "$option" == "2" ]; then
      echo "test 2"
elif [ "$option" == "3" ]; then
      echo "test 3" 
else
      echo "Please enter correct option!"
fi


--
for ((i=1;i<=10;i++))
do
  echo "$i"
done