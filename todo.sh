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

addToList(){
	echo $taskToDo >> todo.txt
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
		AddToList)
			echo "--------------"
			echo "Enter in what you need to do later"
			read taskToDo
			echo $taskToDo
			addToList $taskToDo
			echo $taskToDo has been added to the TO-DO List
			echo "--------------"
			;;
		RemoveFromList)
		Exit)
			echo "Goodbye!"
			exit 0
	esac
done

