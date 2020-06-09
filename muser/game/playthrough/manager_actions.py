#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
*------------------------------------------------------------------------------*
# File: /williamye/program/pyxel_projects/muser/muser/game/playthrough/manager_actions.py #
# Project: /williamye/program/pyxel_projects/muser/muser/game/playthrough      #
# Created Date: Friday, December 13th 2019, 03:24:05 pm                        #
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


from sheet.gen.abs_output import *
from game.playthrough.note import PositionedNote
from game.playthrough.effect.frame_effect import *
from game.playthrough.effect.move_effect import *
from game.playthrough.effect.criteria_effect import *
from game.playthrough.fancy_note import *
class ManagerActions:
    @staticmethod
    def from_note(note):
        if isinstance(note, AbsNote):
            return PositionedNote(note)
        elif isinstance(note, StartFancy):
            return StartEffectNote(FancyEffect, note)
        elif isinstance(note, EndEffect):
            return EndEffectNote(note)
        elif isinstance(note, StartFrame):
            return StartEffectNote(FrameEffect, note)
        elif isinstance(note, StartMove):
            return StartEffectNote(MoveEffect, note)
        elif isinstance(note, StartCriteria):
            return StartEffectNote(CriteriaEffect, note)
        else:
            return note
