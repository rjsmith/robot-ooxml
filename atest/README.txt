robot-ooxml Acceptance Tests
============================

Introduction
------------

This folder contains acceoptance tests for the robot-ooxml parser modules, which
are written using robot framework.

The atest/run_atests.py and test case files under the atest/testdata folder were
adapted and modified from the main RobotFramework distribution (c) 2008-2014 Nokia Solutions and Networks

License and Copyright
---------------------

All the content in `atest` folder is the under following copyright::

    Copyright 2014 RSBA Technology Ltd

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Directory contents
------------------

run_atests.py
    A script for running acceptance tests. See below for further
   instructions.

testdata/
    Contains .docx and .xlsx acceptance test files.

results/
    The place for test execution results like reports, logs and outputs.
    This directory is generated when acceptance tests are executed. It
    is in `.gitignore` and can be safely deleted any time.

Running Acceptance Tests
------------------------

robot-ooxml's acceptance tests are run using `run_atests.py`. Its
usage is displayed with `--help` and also shown below::

Usage:  run_atests.py interpreter [options] datasource(s)

Data sources should be paths to directories or files under `atest/testdata` folder.

Available options are the same that can be used with Robot Framework.
See its help (e.g. `pybot --help`) for more information.

The specified interpreter is used to execute acceptance tests under `testdata` 
It can be simply `python` or `jython`
(if they are in PATH) or to a path a selected interpreter (e.g.
`/usr/bin/python26`). Note that this script itself must always be
executed with Python 2.6 or newer.

Examples:
$ atest/run_atests.py python --test example atest/testdata
$ atest/run_atests.py /usr/bin/jython25 atest/testdata/parsing/data_formats/docx/sample.docx

When acceptance tests are run, both Python and Jython interpreter should be
used to verify interoperability with both supported interpreters. Tests
can (and should) also be run using different Python and Jython versions and
on different operating systems. 

The results of the test execution are written to `results` folder. The
directory contains output, log and report files of the execution as
well as a separate directory for other outputs.

Test Data
---------

The .docx and .xlsx files contained in the /testdata folder structure form the 
acceptance tests for robot-ooxml project.  
The style and content of the included test files were modified from the equivalent files in the main
Robot Framework distribution for the standard - supported parser formats.
