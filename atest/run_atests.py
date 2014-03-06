#!/usr/bin/env python

"""A script for running Robot Framework's acceptance tests.

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

NB: This script is a modified version of the atest/run_atests.py module in the main RobotFramework distribution
"""

import os
import shutil
import signal
import subprocess
import sys
import tempfile
from os.path import abspath, basename, dirname, exists, join, normpath, splitext

if sys.version_info < (2, 6):
    sys.exit('Running this script requires Python 2.6 or newer.')

CURDIR = dirname(abspath(__file__))
ARGUMENTS = ' '.join('''
--doc RobotSPOOXMLSPacceptanceSPtests
--reporttitle RobotSPOOXMLSPTestSPReport
--logtitle RobotSPOOXMLSPTestSPLog
--metadata Platform:%(PLATFORM)s
--pythonpath %(PYTHONPATH)s
--outputdir %(OUTPUTDIR)s
--output output.xml
--report report.html
--log log.html
--escape space:SP
--critical regression
--SuiteStatLevel 3
--TagStatExclude x-*
--parser docx:OOXMLParser.DocxReader
--parser xlsx:OOXMLParser.XlsxReader
'''.strip().split())


def atests(interpreter_path, *params):
    interpreter = _get_interpreter_basename(interpreter_path)
    resultdir, tempdir = _get_result_and_temp_dirs(interpreter)
    args = ARGUMENTS % {
        'PYTHONPATH' : join(CURDIR, '..', 'src'),
        'OUTPUTDIR' : resultdir,
        'PLATFORM': sys.platform,
    }
    command = '%s %s %s' % (interpreter_path, args, ' '.join(params))
    environ = dict(os.environ, TEMPDIR=tempdir)
    print 'Running command\n%s\n' % command
    sys.stdout.flush()
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    return subprocess.call(command.split(), env=environ)

def _get_interpreter_basename(interpreter):
    interpreter = basename(interpreter)
    base, ext  = splitext(interpreter)
    if ext.lower() in ('.sh', '.bat', '.cmd', '.exe'):
        return base
    return interpreter

def _get_result_and_temp_dirs(interpreter):
    resultdir = join(CURDIR, 'results', interpreter)
    tempdir = join(tempfile.gettempdir(), 'robottests', interpreter)
    if exists(resultdir):
        shutil.rmtree(resultdir)
    if exists(tempdir):
        shutil.rmtree(tempdir)
    os.makedirs(tempdir)
    return resultdir, tempdir


if __name__ == '__main__':
    if len(sys.argv) == 1 or '--help' in sys.argv:
        print __doc__
        rc = 251
    else:
        rc = atests(*sys.argv[1:])
    sys.exit(rc)
