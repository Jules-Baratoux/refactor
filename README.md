Refactor
========

Renames file, folders and contents based on regular expression

###Synopsys
  refactor *pattern* *replace* *pathname* [*pathnames* ...]


###Description
Replaces each occurrences of regular expressions *pattern* by *replace* in *pathnames*.


###Options
-p, --python  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Before *pattern* or *replace*, the expression argument is parsed and evaluated as a Python expression


###Examples
```bash
# replace all occurrences of aaa by bbb
refactor aaa bbb *.h *.cpp Makefile

# refactor using a new convention
refactor aaa_([a-z]+) \1_bbb *.cpp Makefile

# camelCase-ify using a python function
refactor '([a-z]+)_([a-z]+)' -p 'lambda m: m.group(1).lower() + m.group(2).capitalize(),' *.h
```
