# Command Line Commands

## npm

```zsh
# get all global npm packages
npm list -g --depth=0
```

## ag (search within files)

```zsh
# look for string in all files in dir
ag test_function
# count occurences per file, don't print matches
ag -c test
# "context": print line before and after
ag -C test
# search recursively but only 2 dirs deep
ag --depth 2 jordan
```

## find (search for files)

```zsh
# search for file in current dir
find -name lists.py
# search for file in dir ignoring case
find ./development -iname application.py
```

## cat

```zsh
# put contents of f1 into f2
cat f1 > f2
# concats f1-3 and puts that into f4
cat f1 f2 f3 > f4
# cat results into file
echo $(which ls) > new.txt
```

## Diff

```zsh
# diff and ignore whitespace
diff -w file1.txt file2.txt
```

## tree

```zsh
# show dirs only
tree -d
# show only text files with letter names
tree -P "[a-z]_.txt"
# don't show text files with letter names
tree -P -I "[a-z]_.txt"
# only show 2 levels deep
tree -L 2
# do not open dirs with >4 files
tree --filelimit 4
```

## Files

```zsh
# print the first/last 10 lines
head/tail <filename>
# give exec permission to user for file
chmod +x <filename>
# get size of all contents (h: human, s: summary)
du -hs /path
# get file type and info
file file_name
# list hardware
lshw
# change owner of all files from root to user
chown -R $USER:$USER .
```

## Helper Stuff

```zsh
# brief desc of command 'ls'
whatis ls
# return /usr/bin/vim or whatever
which vim
# looks for possible useful files
whereis vim
```

## networking

```zsh
# save the http response into a.txt
curl -o a.txt www.test.com
# download html
wget google.com
# ping google
ping www.google.com
```

## Environment

```zsh
# set new env var
VAR_NAME=val
export VAR_NAME=val
# remove
unset VAR_NAME
# print all env vars
env
```

## Processes

```zsh
# system processes
top
# fancy system resources
htop
# child processes
ps
# all procs in a tree
pstree
```

## Sort

```zsh
# sort
sort name.txt
# sort descending
sort -r name.txt
```

## General typing

```zsh
# multiline command
\<enter>
# clear line
ctrl+u
# go to start of line
ctrl+a
# go to end of line
ctrl+e
# delete last word
ctrl+w
# move back one word
alt+b
# move forward one word
alt+f
```
