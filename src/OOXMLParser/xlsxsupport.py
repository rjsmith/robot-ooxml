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

from robot.errors import DataError

try:
    from openpyxl import (load_workbook, Workbook)
except ImportError:
    raise DataError("Using xlsx test data requires having "
                    "'openpyxl' module installed.")

class XlsxWorkbookReader:
    '''
    Wrapper class around openpyxlx API calls to inspect structure of xlsx file
    '''
    def __init__(self, xlsxfile):
        self.workbook = load_workbook(xlsxfile, use_iterators = True)
            
    def getTestSheet(self):
        '''
        Returns reference to first sheet in workbook
        '''
        return self.workbook.get_sheet_by_name(self.workbook.get_sheet_names()[0])
            
    def getTextOfRowCells(self, row):
        cellTexts = []
        for cell in row:
            value = cell.internal_value
            if value is None:
                value = ''
            cellTexts.append(unicode(value))
        return cellTexts
    
        
        