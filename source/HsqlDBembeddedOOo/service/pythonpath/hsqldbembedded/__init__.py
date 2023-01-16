#!
# -*- coding: utf_8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                    ║
║   Copyright (c) 2020 https://prrvchr.github.io                                     ║
║                                                                                    ║
║   Permission is hereby granted, free of charge, to any person obtaining            ║
║   a copy of this software and associated documentation files (the "Software"),     ║
║   to deal in the Software without restriction, including without limitation        ║
║   the rights to use, copy, modify, merge, publish, distribute, sublicense,         ║
║   and/or sell copies of the Software, and to permit persons to whom the Software   ║
║   is furnished to do so, subject to the following conditions:                      ║
║                                                                                    ║
║   The above copyright notice and this permission notice shall be included in       ║
║   all copies or substantial portions of the Software.                              ║
║                                                                                    ║
║   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,                  ║
║   EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES                  ║
║   OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.        ║
║   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY             ║
║   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,             ║
║   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE       ║
║   OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.                                    ║
║                                                                                    ║
╚════════════════════════════════════════════════════════════════════════════════════╝
"""

from .connection import Connection

from .documenthandler import DocumentHandler

from .unotool import createService
from .unotool import getDesktop
from .unotool import getDialog
from .unotool import getFileSequence
from .unotool import getPropertyValueSet
from .unotool import getResourceLocation
from .unotool import getSimpleFile
from .unotool import getStringResource
from .unotool import getUriFactory
from .unotool import getUrl
from .unotool import getUrlTransformer
from .unotool import parseUrl

from .dbtool import getDataBaseInfo

from .configuration import g_extension
from .configuration import g_identifier
from .configuration import g_jdbcdriver

from .dbconfig import g_class
from .dbconfig import g_jar
from .dbconfig import g_options
from .dbconfig import g_path
from .dbconfig import g_protocol
from .dbconfig import g_shutdown

from .logger import clearLogger
from .logger import getLoggerSetting
from .logger import getLoggerUrl
from .logger import getMessage
from .logger import logMessage
from .logger import setLoggerSetting

