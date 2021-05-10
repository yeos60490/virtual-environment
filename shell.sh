#!/bin/bash
command_type = $1
env = $2
base_prompt = "\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$" 

echo $command_type

if [ ${command_type} == "activate" ]
then
	export PS1="(${env})"$PS1

elif [ ${command_type} == "deactivate" ] 
then
	export PS1=base_prompt
fi
