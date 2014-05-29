refactor
========

Renames file, folders and contents based on reguler expretions

refactor *pattern* *replace* *pathname* [*pathnames* ...]

Replaces each occurrences of regular expressions *pattern* by *replace* in *pathnames*.

Interpret python expressions using the *--python* flag before *replace* and *pathname*

```
refactor aaa bbb *.cpp Makefile
refactor aaa_([a-z]+) \1_bbb *.cpp Makefile
refactor '([a-zA-Z]+)_([a-zA-Z]+)' --python 'lambda m: m.group(1).lower() + m.group(2).capitalize(),' *.h
```
