# python-dependency-list

A primitive library for finding external dependencies of a python project.

**Usage:** `python deplst.py pwd` where `pwd` is the root path to the folder containing the python project. The code will:

* Find all `.py` files within the folder
* Extract dependencies by parsing `import X` and `from X import` statements
* Return minimal set

**Known shortcomings:**

* Code is not aware of standard libraries, so it may return libraries like `os` which are installed by default
* Code does not attempt to infer library versions
* Occasionally comments may be parsed as dependencies. Currently fixed by manual deletion, optimally should remove all comments from file prior to parsing
