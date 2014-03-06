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

class DocxReader(object):
    '''wrapper class for DocxReader is just to keep the python-docx modules from 
       being imported unless it's actually being used.
    '''
    def __new__(cls):
        from .docxsupport import (DocxDocumentReader)
    
        class DocxReader(object):
            '''
            Parser class that extracts Robot Framework test suite
            instructions from a Open Office XML .docx file.
            '''
                
            def read(self, docxfile, populator):
                """
                Open, reads and parses a docx file 
                """
                self.populator = populator
                self.docxDocumentReader = DocxDocumentReader(docxfile)
                for table in self.docxDocumentReader.getTables():
                    rows = self.docxDocumentReader.getTableRows(table)
                    process = False
                    for row in rows:
                        cells = self.docxDocumentReader.getTextOfRowCells(row)
                        if cells and cells[0].strip().startswith('*') and \
                                populator.start_table([c.replace('*', '') for c in cells]):
                            process = True
                        elif process:
                            populator.add(cells)
                    populator.eof()    
                populator.eof()
                
        return DocxReader()
        