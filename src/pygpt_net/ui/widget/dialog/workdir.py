#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2024.02.25 12:00:00                  #
# ================================================== #

from PySide6.QtCore import Qt
from .base import BaseDialog


class WorkdirDialog(BaseDialog):
    def __init__(self, window=None, id="workdir.change"):
        """
        WorkdirChangeDialog

        :param window: main window
        """
        super(WorkdirDialog, self).__init__(window, id)
        self.window = window
        self.disable_geometry_store = True

    def closeEvent(self, event):
        """
        Close event

        :param event: close event
        """
        self.cleanup()
        super(WorkdirDialog, self).closeEvent(event)

    def keyPressEvent(self, event):
        """
        Key press event

        :param event: key press event
        """
        if event.key() == Qt.Key_Escape:
            self.cleanup()
            self.close()  # close dialog when the Esc key is pressed.
        else:
            super(WorkdirDialog, self).keyPressEvent(event)

    def cleanup(self):
        """
        Cleanup on close
        """
        self.window.controller.settings.workdir.is_dialog = False


