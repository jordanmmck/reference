# Tmux

## Panes

`o` switch panes
`C-d` kill pane

## Tabs

`c` create window
`n` next window
`p` previous window
`<number>` switch to numbered window
`,` name window
`.` move window

## sessions

`tmux new -s myname` new session with name
`tmux a #` attach
`tmux attach -t 0` attach to session 0
`&` kill window
`d` detach from current session
`tmux ls` see sessions
`tmux rename-session` rename existing session
`-t 0 database`

## Tmuxinator

```zsh
tmuxinator new thing
tmuxinator start thing
tmux kill-session -t myname
```
