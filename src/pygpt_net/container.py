#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.25 21:00:00                  #
# ================================================== #

from pygpt_net.config import Config
from pygpt_net.core.assistants import Assistants
from pygpt_net.core.attachments import Attachments
from pygpt_net.core.camera import Camera
from pygpt_net.core.chain import Chain
from pygpt_net.core.command import Command
from pygpt_net.core.ctx import Ctx
from pygpt_net.core.debugging import Debug
from pygpt_net.core.dispatcher import Dispatcher
from pygpt_net.core.filesystem import Filesystem
from pygpt_net.core.gpt import Gpt
from pygpt_net.core.gpt_assistants import GptAssistants
from pygpt_net.core.history import History
from pygpt_net.core.image import Image
from pygpt_net.core.info import Info
from pygpt_net.core.models import Models
from pygpt_net.core.modes import Modes
from pygpt_net.core.notepad import Notepad
from pygpt_net.core.platforms import Platforms
from pygpt_net.core.plugins import Plugins
from pygpt_net.core.presets import Presets
from pygpt_net.core.settings import Settings
from pygpt_net.installer import Installer
from pygpt_net.updater import Updater


class Container:
    def __init__(self, window=None):
        """
        Service container

        :param window: Window instance
        """
        self.window = window

        # core services
        self.assistants = Assistants(window)
        self.attachments = Attachments(window)
        self.camera = Camera(window)
        self.chain = Chain(window)
        self.command = Command(window)
        self.config = Config(window)
        self.ctx = Ctx(window)
        self.debug = Debug(window)
        self.dispatcher = Dispatcher(window)
        self.filesystem = Filesystem(window)
        self.gpt = Gpt(window)
        self.gpt_assistants = GptAssistants(window)
        self.history = History(window)
        self.image = Image(window)
        self.info = Info(window)
        self.installer = Installer(window)
        self.models = Models(window)
        self.modes = Modes(window)
        self.notepad = Notepad(window)
        self.platforms = Platforms(window)
        self.plugins = Plugins(window)
        self.presets = Presets(window)
        self.settings = Settings(window)
        self.updater = Updater(window)

    def init(self):
        """Initialize all components"""
        self.config.init(all=True)
        self.platforms.init()

    def patch(self):
        """Patch version"""
        self.updater.patch()