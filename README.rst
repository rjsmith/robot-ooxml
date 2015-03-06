============
Introduction
============

*robot-ooxml* is a Python library for parsing Microsoft Word .docx and Excel .xlsx format files
into the automated testing tool RobotFramework.

Status: EXPERIMENTAL

Dependent on a patch to Robot Framework that has not yet been added to the main build.
See: https://github.com/robotframework/robotframework/issues/1283

(Originally posted on Google Groups here: http://code.google.com/p/robotframework/issues/detail?id=1283)

This only works when running Robot Framework using the python interpreter (see https://github.com/rjsmith/robot-ooxml/issues/1 ).

============
Installation
============

Install the special cloned version of Robot Framework with the parser patch (see link above)

Add the src/ folder to your PYTHONPATH before running Robot Framework::

   #!/bin/bash
   
   if [ -z "$PYTHONPATH" ]; then
      export PYTHONPATH=<path to>/robot-ooxml/src
   else
      export PYTHONPATH=$PYTHONPATH:<path to>/robot-ooxml/src
   fi
   
   pybot --parser docx:OOXMLParser.DocxReader --parser xlsx:OOXMLParser.XlsxReader atest/testdata

=====
Usage
=====

Specify one or both of the following --parser arguments in the Robot Framework executable command::
   
   --parser docx:OOXMLParser.DocxReader
   --parser xlsx:OOXMLParser.XlsxReader
   
====
DOCX
====

Each Robot Framework Test Table must be specified in its own Microsoft Word table, with the table type keyword prefixed by at least one '*' character.

See the atest/testdata/parsing/data_formats/docx/sample.docx file for an example

====
XLSX
====

The XlsxReader class inspects the first worksheet defined in a Microsoft Excel .xlsx file. The parser skips all rows until it encounters the first 
Robot Framework Test Table (with the table type keyword prefixed by at least one '*' character).

See the atest/testdata/parsing/data_formats/xlsx/Sample.xlsx file for an example

=======
Testing
=======

Run the atest/run_atests.py python file to execute the included Robot Franework - based automated tests.  
See the atest/README.txt file for further instructions.

