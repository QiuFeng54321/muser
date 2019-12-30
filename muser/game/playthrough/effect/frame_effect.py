#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
*------------------------------------------------------------------------------*
# File: /williamye/program/pyxel_projects/muser/muser/game/playthrough/effect/frame_effect.py #
# Project: /williamye/program/pyxel_projects/muser/muser/game/playthrough/effect #
# Created Date: Monday, December 16th 2019, 04:21:53 pm                        #
# Author : Qiufeng54321                                                        #
# Email : williamcraft@163.com                                                 #
#                                                                              #
# Copyright (C) 2019  Qiufeng54321                                             #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
# You should have received a copy of the GNU General Public License            #
# along with this program.  If not, see <https://www.gnu.org/licenses/>.       #
# -----                                                                        #
# Description:                                                                 #
#                                                                              #
#                                                                              #
*------------------------------------------------------------------------------*
'''


import pyxel, time
from game.playthrough.effect.base_effect import *
from game.constants import Constants
from sheet.gen.abs_output import *

class FrameEffect(Effect):
    def __init__(self, frame_note: StartFrame):
        super().__init__(identity=frame_note.identity)
        self.frame_note = frame_note
        # print(self.frame_note.frame)
    def update(self, **kwargs):
        pass
    def draw(self, **kwargs):
        cur = time.time()
        avg = 0
        for y in range(self.frame_note.size[1]):
            for x in range(self.frame_note.size[0]):
                c = time.time()
                if self.frame_note.frame[y][x] != -1:
                    # print(
                    #     f"Draw {self.frame_note.frame[y][x]} at ({self.frame_note.offset_pos[0] + x}, {self.frame_note.offset_pos[1] + y})")
                    pyxel.pix(
                        self.frame_note.offset_pos[0] + x, self.frame_note.offset_pos[1] + y, self.frame_note.frame[y][x])
                avg += (time.time() - c) / (self.frame_note.size[1] * self.frame_note.size[0])
        print(
            f"{time.time() - cur}s, avg {avg}s, execution: {self.frame_note.size[0] * self.frame_note.size[1]} times")
