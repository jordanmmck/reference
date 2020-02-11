# Git

## Branches

push changes on master to branch 'feature' on remote
`git push origin master:feature`

create branch, track origin
`git checkout -b mybranch --track origin/develop`

make branch locally, and switch to it
`git checkout -b a-star`

push branch up
`git push -u origin a-star`

see branches and stuff that we might not have locally
`git ls-remote origin`

push to (and create) new remote branch
`git push origin WEB-503:WEB-503-bugfix`

## Push

-u tells git to remember location so we can just git push
`git push -u origin master`

## Reset

revert back to last commit (changes made on top of commit are lost)
`git reset --hard`
`git reset --hard origin/<branch_name>`

## ignore

update gitignore, then
`git rm -r --cached <file>`
`git rm -r --cached .`

## Stop Tracking

stops tracking and deletes file!
`git rm a.txt b.h`

## log

see git log for one file
`git log --follow README.md`
