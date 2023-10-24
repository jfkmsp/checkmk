#!/usr/bin/env python3
# Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Use CSS-standard, extended colors from https://www.w3.org/wiki/CSS/Properties/color/keywords"""

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class RGB:
    red: int
    green: int
    blue: int

    def __post_init__(self) -> None:
        assert 0 <= self.red <= 255
        assert 0 <= self.green <= 255
        assert 0 <= self.blue <= 255


class Color(Enum):
    ALICE_BLUE = RGB(240, 248, 255)
    ANTIQUE_WHITE = RGB(250, 235, 215)
    AQUA = RGB(0, 255, 255)
    AQUAMARINE = RGB(127, 255, 212)
    AZURE = RGB(240, 255, 255)
    BEIGE = RGB(245, 245, 220)
    BISQUE = RGB(255, 228, 196)
    BLACK = RGB(0, 0, 0)
    BLANCHE_DALMOND = RGB(255, 235, 205)
    BLUE = RGB(0, 0, 255)
    BLUE_VIOLET = RGB(138, 43, 226)
    BROWN = RGB(165, 42, 42)
    BURLY_WOOD = RGB(222, 184, 135)
    CADET_BLUE = RGB(95, 158, 160)
    CHARTREUSE = RGB(127, 255, 0)
    CHOCOLATE = RGB(210, 105, 30)
    CORAL = RGB(255, 127, 80)
    CORNFLOWER_BLUE = RGB(100, 149, 237)
    CORN_SILK = RGB(255, 248, 220)
    CRIMSON = RGB(220, 20, 60)
    CYAN = RGB(0, 255, 255)
    DARK_BLUE = RGB(0, 0, 139)
    DARK_CYAN = RGB(0, 139, 139)
    DARK_GOLDENROD = RGB(184, 134, 11)
    DARK_GRAY = RGB(169, 169, 169)
    DARK_GREEN = RGB(0, 100, 0)
    DARK_KHAKI = RGB(189, 183, 107)
    DARK_MAGENTA = RGB(139, 0, 139)
    DARK_OLIVE_GREEN = RGB(85, 107, 47)
    DARK_ORANGE = RGB(255, 140, 0)
    DARK_ORCHID = RGB(153, 50, 204)
    DARK_RED = RGB(139, 0, 0)
    DARK_SALMON = RGB(233, 150, 122)
    DARK_SEA_GREEN = RGB(143, 188, 139)
    DARK_SLATE_BLUE = RGB(72, 61, 139)
    DARK_SLATE_GRAY = RGB(47, 79, 79)
    DARK_TURQUOISE = RGB(0, 206, 209)
    DARK_VIOLET = RGB(148, 0, 211)
    DEEP_PINK = RGB(255, 20, 147)
    DEEP_SKYBLUE = RGB(0, 191, 255)
    DIM_GRAY = RGB(105, 105, 105)
    DODGER_BLUE = RGB(30, 144, 255)
    FIRE_BRICK = RGB(178, 34, 34)
    FLORAL_WHITE = RGB(255, 250, 240)
    FOREST_GREEN = RGB(34, 139, 34)
    FUCHSIA = RGB(255, 0, 255)
    GAINSBORO = RGB(220, 220, 220)
    GHOST_WHITE = RGB(248, 248, 255)
    GOLD = RGB(255, 215, 0)
    GOLDENROD = RGB(218, 165, 32)
    GRAY = RGB(128, 128, 128)
    GREEN = RGB(0, 128, 0)
    GREEN_YELLOW = RGB(173, 255, 47)
    HONEYDEW = RGB(240, 255, 240)
    HOT_PINK = RGB(255, 105, 180)
    INDIAN_RED = RGB(205, 92, 92)
    INDIGO = RGB(75, 0, 130)
    IVORY = RGB(255, 255, 240)
    KHAKI = RGB(240, 230, 140)
    LAVENDER = RGB(230, 230, 250)
    LAVENDER_BLUSH = RGB(255, 240, 245)
    LAWN_GREEN = RGB(124, 252, 0)
    LEMON_CHIFFON = RGB(255, 250, 205)
    LIGHT_BLUE = RGB(173, 216, 230)
    LIGHT_CORAL = RGB(240, 128, 128)
    LIGHT_CYAN = RGB(224, 255, 255)
    LIGHT_GOLDENROD_YELLOW = RGB(250, 250, 210)
    LIGHT_GRAY = RGB(211, 211, 211)
    LIGHT_GREEN = RGB(144, 238, 144)
    LIGHT_PINK = RGB(255, 182, 193)
    LIGHT_SALMON = RGB(255, 160, 122)
    LIGHT_SEA_GREEN = RGB(32, 178, 170)
    LIGHT_SKY_BLUE = RGB(135, 206, 250)
    LIGHT_SLATE_GRAY = RGB(119, 136, 153)
    LIGHT_STEEL_BLUE = RGB(176, 196, 222)
    LIGHT_YELLOW = RGB(255, 255, 224)
    LIME = RGB(0, 255, 0)
    LIME_GREEN = RGB(50, 205, 50)
    LINEN = RGB(250, 240, 230)
    MAGENTA = RGB(255, 0, 255)
    MAROON = RGB(128, 0, 0)
    MEDIUM_AQUAMARINE = RGB(102, 205, 170)
    MEDIUM_BLUE = RGB(0, 0, 205)
    MEDIUM_ORCHID = RGB(186, 85, 211)
    MEDIUM_PURPLE = RGB(147, 112, 219)
    MEDIUM_SEA_GREEN = RGB(60, 179, 113)
    MEDIUM_SLATE_BLUE = RGB(123, 104, 238)
    MEDIUM_SPRING_GREEN = RGB(0, 250, 154)
    MEDIUM_TURQUOISE = RGB(72, 209, 204)
    MEDIUM_VIOLET_RED = RGB(199, 21, 133)
    MIDNIGHT_BLUE = RGB(25, 25, 112)
    MINT_CREAM = RGB(245, 255, 250)
    MISTY_ROSE = RGB(255, 228, 225)
    MOCCASIN = RGB(255, 228, 181)
    NAVAJO_WHITE = RGB(255, 222, 173)
    NAVY = RGB(0, 0, 128)
    OLD_LACE = RGB(253, 245, 230)
    OLIVE = RGB(128, 128, 0)
    OLIVE_DRAB = RGB(107, 142, 35)
    ORANGE = RGB(255, 165, 0)
    ORANGE_RED = RGB(255, 69, 0)
    ORCHID = RGB(218, 112, 214)
    PALE_GOLDENROD = RGB(238, 232, 170)
    PALE_GREEN = RGB(152, 251, 152)
    PALE_TURQUOISE = RGB(175, 238, 238)
    PALE_VIOLET_RED = RGB(219, 112, 147)
    PAPAYA_WHIP = RGB(255, 239, 213)
    PEACH_PUFF = RGB(255, 218, 185)
    PERU = RGB(205, 133, 63)
    PINK = RGB(255, 192, 203)
    PLUM = RGB(221, 160, 221)
    POWDER_BLUE = RGB(176, 224, 230)
    PURPLE = RGB(128, 0, 128)
    REBECCA_PURPLE = RGB(102, 51, 153)
    RED = RGB(255, 0, 0)
    ROSY_BROWN = RGB(188, 143, 143)
    ROYAL_BLUE = RGB(65, 105, 225)
    SADDLE_BROWN = RGB(139, 69, 19)
    SALMON = RGB(250, 128, 114)
    SANDY_BROWN = RGB(244, 164, 96)
    SEASHELL = RGB(255, 245, 238)
    SEA_GREEN = RGB(46, 139, 87)
    SIENNA = RGB(160, 82, 45)
    SILVER = RGB(192, 192, 192)
    SKY_BLUE = RGB(135, 206, 235)
    SLATE_BLUE = RGB(106, 90, 205)
    SLATE_GRAY = RGB(112, 128, 144)
    SNOW = RGB(255, 250, 250)
    SPRING_GREEN = RGB(0, 255, 127)
    STEEL_BLUE = RGB(70, 130, 180)
    TAN = RGB(210, 180, 140)
    TEAL = RGB(0, 128, 128)
    THISTLE = RGB(216, 191, 216)
    TOMATO = RGB(255, 99, 71)
    TURQUOISE = RGB(64, 224, 208)
    VIOLET = RGB(238, 130, 238)
    WHEAT = RGB(245, 222, 179)
    WHITE = RGB(255, 255, 255)
    WHITE_SMOKE = RGB(245, 245, 245)
    YELLOW = RGB(255, 255, 0)
    YELLOW_GREEN = RGB(154, 205, 50)
