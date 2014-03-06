# Copyright (c) 2014 Richard Smith, https://github.com/rjsmith
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class XlsxReader(object):
    '''wrapper class for XlsxReader is just to keep the openpyxl modules from 
       being imported unless it's actually being used.
    '''
    def __new__(cls):
        from .xlsxsupport import (XlsxWorkbookReader)

        class XlsxReader(object):
            '''
            Parser class that extracts Robot Framework test suite
            instructions from a Open Office XML .xlsx file.
            
            Only the current active sheet is parsed
            '''
                
            def read(self, xlsxfile, populator):
                """
                Open, reads and parses a xlsx file 
                """
                process = False
                self.populator = populator
                self.xlsxWorkbookReader = XlsxWorkbookReader(xlsxfile)
                sheet = self.xlsxWorkbookReader.getTestSheet()
                for row in sheet.iter_rows():  # Use openpyxl optimised reader to hanle potentially large excel files
                    cells = self.xlsxWorkbookReader.getTextOfRowCells(row)
                    if cells and cells[0].strip().startswith('*') and \
                            populator.start_table([c.replace('*', '') for c in cells]):
                        process = True
                    elif process:
                        populator.add(cells)
                self.populator.eof()
                
        return XlsxReader()
        