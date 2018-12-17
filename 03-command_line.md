# Learn command line

Please follow and complete the free online [Bash Scripting Tutorial](https://ryanstutorials.net/bash-scripting-tutorial/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. You should be able to go through these in a couple of hours.

**Note:** Bash is not installed on a PC. Rather, PC users must install Cygwin. Once Cygwin has been installed, the command line interface witll _emulate_ bash. You can find all information regarding Cygwin [here](https://www.cygwin.com/).

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

`pwd` Present Working Directory
`rm` Delete a file
`rm -r` Delete a directory
`touch` Create an empty file
`chmod` Change Mode of a file or directory
`mv` Move or rename a file/directory
`ls -a' List all (hidden) files
`cp` Copy a file/Directory
`ps` list running proccesses
`kill` Terminate a proccess

---

### Q2.  List Files in Unix   

What do the following commands do:  

`ls` List the contents of a directory ... 

`ls -a` ... including hidden files

`ls -l`  ... long format ... showing permissions, access times, file size 

`ls -lh`  ... long format + file size type (KB,MB,GB) 

`ls -lah` ... see above 

`ls -t`  ... lists most recently modified files first 

`ls -Glp`  ... Color output and place a '/' after file if a directory  



---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -d`

`ls -1`

`ls -m`

`ls -i`

`ls -r` 

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` runs a specified command on a stream of delimited data coming from standard input. `xargs` could be used to make a large list of strings uppercase, ex:

`cat name_list | xargs to_upper_case.sh`

 

