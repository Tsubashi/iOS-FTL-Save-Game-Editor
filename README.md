iOS-FTL-Save-Game-Editor
========================

An FTL Save Game modifier for iOS

Description
------------
A set of python scripts for reading and writing continue.sav files for the iOS game FTL. May or may not work on the desktop version. 

To use, place the file to be decoded into the Input folder, make any changes you want to main.py and then run main.py. The output file will be placed in the appropriately named output folder.

Caveats and Oddities
--------------------
As of yet, 
- The script only parses up through the ship info.
- Room info is ignored, since it requires information from the layout file.


License
--------
The MIT License (MIT)

Copyright (c) 2014 Tsubashi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
