# Git Merges

Git tries to make it easier to bring independently-made
changes together into a unified view. Different work does
not become a collaboration until it is brought together and
polished so it fits together nicely.


## Ancestor Merge

One way to merge is to find a common ancestor and compare
the file with the smaller changes to the ancestor using
'diff'.

The output from 'diff' can then be given to another
program named 'patch' that will try to recreate those changes
even if the base file has changed a bit. The patch is applied
to the file with the bigger changes. The result is a dumb
but effective way of combining both sets of changes.


## The Old Ways

Old configuration management systems tried to eliminate
the need for merges by "locking" a file. Users were allowed to
"check out" files and use them for their local development
and builds, but the files were checked out read-only to
discourage development. If a developer wanted to make a change
to a file, they would indicate that to version control by
asking for a locked copy. The developer making the request would
be given a writable version; no other developer was allowed
to write until the file had either been checked back in or the
lock given up and any changes abandoned.
