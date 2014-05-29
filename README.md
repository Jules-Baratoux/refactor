refactor
========

Renames file, folders and contents based on reguler expretions

###Synopsys
  refactor *pattern* *replace* *pathname* [*pathnames* ...]


###Description
Replaces each occurrences of regular expressions *pattern* by *replace* in *pathnames*.


###Options
-p, --python
    Before *replace* or *pathname*, the expression argument is parsed and evaluated as a Python expression


###Examples
    refactor aaa bbb *.cpp Makefile
    refactor aaa_([a-z]+) \1_bbb *.cpp Makefile
    refactor '([a-zA-Z]+)_([a-zA-Z]+)' --python 'lambda m: m.group(1).lower() + m.group(2).capitalize(),' *.h
