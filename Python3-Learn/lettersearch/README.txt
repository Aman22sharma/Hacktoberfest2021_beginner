This module provids the lettersearch method that takes two strings, one for a phrase and one for a set of letters to search within that phrase. 

To create a package from your own material:

1) Create a setup.py file (check the included setup.py for an example)

2) Create a README.txt file.  This file will provide details on the package

3) install setuptools and wheel
  python3 -m pip install --user --upgrade setuptools wheel

4) create the package
  python3 setup.py sdist bdist_wheel 

This will create a /dist directory that will include your package materials
