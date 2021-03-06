#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
*------------------------------------------------------------------------------*
# File: /williamye/program/pyxel_projects/muser/muser/game/playthrough/effect/effect_controller.py #
# Project: /williamye/program/pyxel_projects/muser/muser/game/playthrough/effect #
# Created Date: Saturday, December 14th 2019, 10:02:08 pm                      #
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

from .base_effect import Effect
import util


class EffectController:
    pool: dict = {}

    @staticmethod
    def add_effect(effect: Effect):
        EffectController.pool[effect.identity] = effect

    @staticmethod
    def remove_effect(identity: int):
        if identity in EffectController.pool.keys():
            del EffectController.pool[identity]

    @staticmethod
    def clear_effects():
        EffectController.pool.clear()

    @staticmethod
    def update(*args, **kwargs):
        for effect in EffectController.pool.values():
            effect.update(args, kwargs)

    @staticmethod
    @util.timeit(without=(-1, 30))
    def draw(*args, **kwargs):
        # logger.print("Start drawing")
        for effect_key in sorted(EffectController.pool.keys()):
            # logger.print(effect_key)
            EffectController.pool[effect_key].draw(args, kwargs)
