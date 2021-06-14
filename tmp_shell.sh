#!/bin/bash
command_type=$1
env=$2
base_prompt="\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$" 
root_dir='/root/capstone/'


if [ "${command_type}" = "activate" ]; then
	echo "act"
	echo $command_type
	export PS1="(${env})"$PS1
	#change_prompt="(${env})"$PS1
	python3 ${root_dir}change_sys.py ${env}


elif [ "${command_type}" = "deactivate" ]; then
	echo "deact"
	echo $command_type
	echo $PS1
	echo "${PS1%(test)}"
	#$prompt=$PS1 | sed 's/('${env}')//'
	#echo $prompt

	#export PS1="$PS1 | sed 's/('${env}')//'"
fi


