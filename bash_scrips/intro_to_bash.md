# A brief introduction to bash scripting

This document serves as an intro to bash scripts that will give you the very basics. This subdirectory contains many examples of bash scripts that get into more complicated things, but assume some basic knowledge.

Warning: this probably only works for linux or mac so if you're running windows... sorry. 

## 1. What is bash?

Bash is basically the language you use in your terminal to 'talk' to the operating system. All the commands you use when navigating your computer with terminal, like `ls` and and `cd \path\to\dir` are bash commands. If you'll be using Compute Canada it's all unix based and there's no GUI so you need to know bash in order to navigate your files!

Bash is good to know if you want to navigate a computer through the terminal, but its true power is in _bash scripts_. Have you ever found yourself in a situation where you have to manually rename, like, 10 files? Or you have to keep moving the output files of some python script to a new directory? Any inane, repetitive task you have to do related to file and directory management can be automated with bash. 

Bash scripts save you time, but more importantly automating things makes it so that you're much less likely to make a mistake.

## 2. Hello, world!

Let's do the classic first program. First thing you'll need to do is open up your terminal and go to some directory: 

```sh
$ touch hello.sh
$ code hello.sh
```

Here `$` is the unix prompt, so you don't have to write it. The command `touch` creates an empty file called hello.sh, and `code` is the command to open hello.sh with the text editor VSCode. You can replace this with your preferred text editor. 

Once you have hello.sh open in an editor, write: 

```sh
0 #!/bin/bash
1 echo "hello, world!"
```

In line 0, we're just telling the computer where bash is. Don't worry too much about this, but it has to be at the top of all your bash scripts. 

In line 1 we have `echo`, which is the bash equivalent of `print()`.

One we save this, what we've made is an executable file. The way you run an executable file is the following: 

```bash
$ ./hello.sh
```

We put the `./` before the file name in the same way we have to write `python script.py` in order to run a python script. 

You'll notice if you try to run hello.sh, you'll get an error message along the lines of `bash: ./hello.sh: Permission denied`. This is just a thing linux does to protect itself against random scripts; you have to give a new executable permission to run. There's many ways to do it, but the following has never failed me: 

```bash
$ chmod 700 hello.sh
```

And now you can execute your first bash hello world! 

## 3. Variables and loops

Like any other language, bash can store variables. Consider the following script: 

```bash
#!/bin/bash

var=5

for i in 3 4 5 
do 
    echo $(($var+$i))
done
```
A couple of things to note. The body of your foor loop has to be enclosed by the statements `do` and `done`. Bash doesn't care about indentation, so you can also write: 

```bash
for i in 3 4 5 
do 
echo $(($var+$i)) 
done
```
but I like indenting for clarity. Bash _does_ care about spaces in between things, unlike most other languages. So `var = 5` is an illegal variable assignment. 

Another thing is bash is weird about arithmetic, so whenever you do an arithmetic expression you have put it inside `$(())`. Also when you call variables you need to put `$` in front of their name. 

It's weird. You get used to it. 


## 4. File and directory management

Finally, you're ready to get to the most useful part of bash! 

Let's say you have some directory called `project`, which has a subdirectory called `foo`. In `foo` you have a bunch of .txt files, `bar1.txt`, `bar2.txt`, etc. Now, you want to do something to these text files, maybe run them through a python script. 

Let's say the python script will output a file called `output_bar1.txt` when you pass it `bar1.txt` and so on. Let's say the script will dump the results onto `\project`.

Finally, let's say you want to move all of these outputs into some directory called `results`.

For clarity, here's what the directory structure looks like: 

```
project
│   script.py
│   scrip.sh    
│
└───foo
│   │   bar1.txt
│   │   bar2.txt
│   │   ...
│   
└───results
    │   
```

Here is what script.sh, which will do all these things for you, looks like: 
```bash
0 #!/bin/bash
1 for f in foo/*.txt
2 do 
3   echo ${f} | python script.py
4 done
5 for f in */output_*
6 do 
7   mv ${f} results
8 done
```

In line 1, we're telling the computer: for every file in the directory foo that ends with *.txt, do the following. 

The `*` is called a `glob`, and basically it functions as a string matching pattern. Here, it will only loop through files that end with .txt. In line 5, it is used to indicate that we want to loop through the directory where script.sh lives. In line 5, we're also using it to say we only want to loop through files that begin with the string '_output'. The glob is one of the most useful and versatile tools in bash scripting, but be careful with using it! 

In line 3 we're passing the variable `${f}` to the python script, which will look like `\home\path\to\project\foo\bar1.txt`. Now the python script has the path to the file it has to perform an operation on. 

## 5. Now you are ready to bash!

Well not really. There's a lot more to learn, but this is already longer than I intended, and anyways the best way to learn is to do things for yourself. 

I've included probably the most complicated bash script I've written, for reference if you want to check it out! I've also included the scripts it depends on, so you see how the whole passing variables to python works. And it's useful since it formats things in a way that is friendly for Compute Canada array jobs, which you might need eventually. 

Happy coding! 

-Joelle