#!/bin/bash

clear

echo "				TO-DO LIST"

TODO_LIST="./todo.txt"

getList(){
	while IFS= read -r line
	do
		echo "$line"
	done < "$TODO_LIST"
}

PS3="Enter in one of the following commands: "

select command in DisplayList AddToList RemoveFromList Exit
do
	case $command in
		DisplayList)
			echo "-----List-----"
			getList
			echo "--------------"
			;;
		Exit)
			echo "Goodbye!"
			exit 0
	esac
done

