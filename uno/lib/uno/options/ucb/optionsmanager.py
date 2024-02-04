#!
# -*- coding: utf-8 -*-

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

import unohelper

from com.sun.star.logging.LogLevel import INFO
from com.sun.star.logging.LogLevel import SEVERE

from .optionsmodel import OptionsModel
from .optionsview import OptionsView

from ..unotool import executeDispatch
from ..unotool import getDesktop

from ..logger import LogManager

from ..configuration import g_identifier
from ..configuration import g_defaultlog
from ..configuration import g_synclog

import traceback


class OptionsManager(unohelper.Base):
    def __init__(self, ctx, window, logger):
        self._ctx = ctx
        self._model = OptionsModel(ctx)
        exist = self._model.hasData()
        resumable = self._model.isResumable()
        data = self._model.getViewData()
        self._view = OptionsView(window, exist, resumable, data)
        self._logmanager = LogManager(ctx, window.Peer, 'requirements.txt', g_identifier, g_defaultlog, g_synclog)
        self._logger = logger
        self._logger.logprb(INFO, 'OptionsManager', '__init__()', 151)

    def loadSetting(self):
        data = self._model.getViewData()
        self._view.setViewData(*data)
        self._logmanager.loadSetting()
        self._logger.logprb(INFO, 'OptionsManager', 'loadSetting()', 161)

    def saveSetting(self):
        share, name, index, timeout, download, upload = self._view.getViewData()
        option = self._model.setViewData(share, name, index, timeout, download, upload)
        log = self._logmanager.saveSetting()
        self._logger.logprb(INFO, 'OptionsManager', 'saveSetting()', 171, option, log)

    def enableShare(self, enabled):
        self._view.enableShare(enabled)

    def enableTimeout(self, enabled):
        self._view.enableTimeout(enabled)

    def viewData(self):
        url = self._model.getDatasourceUrl()
        getDesktop(self._ctx).loadComponentFromURL(url, '_default', 0, ())

    def download(self):
        self._view.setStep(1)

    def upload(self):
        self._view.setStep(2)

