# Command Line

npm list -g --depth=0

## browser

open index.html                 open file in browser!

## ag (search within files)

ag test_function .
ag -c test                      just count occurences don't print matches
ag -C test                      print line before and after (context)
ag --depth 2 jordan             only go 2 dirs deep
ag -g *.txt jordan              search txt files for jordan
ag -g txt$ .                    give me all the filenames that end in txt

## find (search for files)

find /dir -name "file.*"        search for file.anything
find . -iname application.py    look for the file and ignore case
find . -type f -name "*.foo"    recursive search for files ending in foo

## cat

cat f1 > f2                     put contents of f1 into f2
cat f1 | less                   print contents page by page
cat > f2                        input into f2. C-d to end. overwrite
cat >> f2                       appends not overwrites
cat f1 f2 f3 > f4               concats f1-3 and puts into f4
echo $(which ls) > new.txt      cat results into file

## Diff

diff -w file1.txt file2.txt     ignore whitespace
diff -r /a/dir /b/dir/          recursive, compare everything
diff -x '*.a' -x '*.b' /dir/1   exclude some files

## tree

tree -d                         directories only
tree -P "[a-z]*.txt"            show only text files with letter names
tree -P -I  "[a-z]*.txt"        don't show text files with letter names
tree -L 2                       only show 2 levels deep
tree --filelimit 4              do not open dirs with >4 files

## curl

curl -o a.txt www.jm.com        save the stuff into a.txt

## wget

wget google.com                 download html, and give some stats on file

## Network

ifconfig                        get network interface info
ping www.google.com             ping google
netstat                         display tcp connections, routing tables, etc
dig www.google.com              get A record, CNAME etc
route                           show ip routing etc
host www.google.com             IP to name or name to IP

## Environment

VAR_NAME=val                    create env var
unset VAR_NAME                  remove env var
export VAR_NAME=val             set env var
env                             print all env vars

## Programs

whatis ls                       brief desc of command 'ls'
which vim                       return /usr/bin/vim or whatever
whereis                         looks for possible useful files

## Files

head/tail <filename>            print the first/last 10 lines
chmod -x <filename>             give exec permission to file
mv myfold/*                     move contents up to current dir
du -hs /path                    get size of all contents (h: human, s: summary)
file file_name                  get file type and info
lshw                            list hardware
chown -R $USER:$USER .          change owner of all files from root to user

## General typing

\<enter>                        multiline command
ctrl+u                          clear line
ctrl+a                          go to start of line
ctrl+e                          go to end of line
ctrl+w                          delete last word
alt+b                           move back one word
alt+f                           move forward one word

## Redirecting

> or 1>                         redirect stdout
2>                              redirect stderr
&>                              redirect both
cat a.txt | grep "test"         pipe output of cat to grep

## Processes

top                             system processes
htop                            fancy system resources
ps                              child processes
pstree                          all procs in a tree

## Tar/Zip

tar xvf archive_name.tar            extract tar
tar xvzf archive_name.tar           extract tar
tar cvf archive_name.tar dirname/   create tar
unzip file.zip
zip -r pics.zip pics                recursive zip

## Deb

sudo dpkg -i file.deb
sudo apt install -f

## Sort

sort name.txt                   sort
sort -r name.txt                sort descending
