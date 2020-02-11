# VIM

## Cut and Paste (using vim-easyclip)

```
// These 'cut' to the yank register. Deleting now just deletes.
m                       move
mm                      move line
p<ctrl-p>               paste then cycle down yanked stuff!!! <ctrl-n> up
Y                       yank to end of line
```

## Moving

```
``                      go back to last place in file
CTRL^                   go to previous file
gi                      move cursor to where it was and insert
C-e                     scroll down
C-y                     scroll up
```

## Fugitive

```
:Gstatus                git status
:Gw                     git add <this file>
:Git add .              git add all
:Gcommit                commit
:Gpush                  git push
:Gpull                  git pull
:Gdiff                  git diff
:Gblame                 git blame
```

## General

```
:pwd                    print working directory
```

## Macros

```
qw                  record macro and store it in reg w
@w                  run macro w
10@w                run macro w 10 times
:let @w='oTEST'     assign macro
:let @W='i;'        add i; to the end of macro w
:let @w='<ctr+r w>  edit macro
@+                  play whatever is in sys reg as a macro
```

## Registers (using vim-easyclip)

```
""                  always last yanked
"0                  always last yanked
"1                  second to last thing yanked ...
...
"a                  free reg"
"+                  system reg"
"%                  current file path (:let @+=@% copies to system clipboard)"
":                  last run command (use @: to run it again)"
"<register id><action>
:reg                see contents"
:reg a              see reg a contents
.                   paste last stuff entered while in insert
"a y                yank to reg a (yy to yank line)
"A y                append to reg a
"a p                paste from reg 'a'
ctrl+r a            paste from 'a' while in insert
22 "a p             paste from reg a 22 times
```

## Commands

```
:<ctrl+r+           paste from sys reg into command box
```

## Find and Replace

```
:[range]s/pattern/string/[cgil]

[none]          current line
%               whole file
10,20           line 10 - 20

:s/abc/123      replace abc with 123 on current line
:4,8s/abc/xyz   replace abc with xyz on line 4-8

c               confirm each
g               replace all in line
i               ignore case
l               dont't ignore case

 %s/foo/bar         replace all foo with bar (remove % for single line)
:%s/foo/bar/c      replace all foo with bar but ask for permission
```

## Editing

```
:%s/\s\+$//e        remove extra spaces/tabs!
2 space tab to 4    :set ts=2 sts=2 noet
                    :retab!
                    :set ts=4 sts=4 et
                    :retab
ct,                 change up to com a
C+v                 insert next char as literal (good for tabs)
```

## Surround

```
cs"'                change double quote to single"
cs'<q>              change surround single quote to q tag
cst"                change surround tag to quote
ds"                 delete surrounding quotes
ysiw]               surround word with []
yssb                surround line with parens
S'                  in visual mode surround selection
```

## Nerdtree

```
ctrl+w+w            toggle between vim and nerdtree!
shift+i             toggle hidden files/folders
<leader>r           refresh tree
C                   make selected dir the main one, "zoom in"
```

## CtrlP

```
<c-d>               switch between filename/fullpath
<c-j> or <c-k>      browse list
# automatically search all dirs!
```

## Deoplete

```
ctrl+n              scroll down list
ctrl+p              scroll up list!
```

## Verbs

```
it                  inner tag
i"                  inner quote"
ip                  inner para
as                  as sentence
```

## Panes

```
Cw-q                cancel split pane
ctrl+w+w            change split panes
ctrl+w <h|j|k|l>    change split panes by direction
```

## Search

```
#                   move to and search for prev instance word under cursor
n/N                 go to next/prev thing
```

## Print

```
:hardcopy > myfile.pdf
:TOhtml
```

## Help

```
:help NERDtree-m    open help, look for m command
```

## Exit paste mode

```
:set nopaste
```
