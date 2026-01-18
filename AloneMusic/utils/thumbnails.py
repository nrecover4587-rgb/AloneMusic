# Copyright (c) 2025 Nand Yaduwanshi <NoxxOP>
# Location: Supaul, Bihar
#
# All rights reserved.
#
# This code is the intellectual property of Nand Yaduwanshi.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: badboy809075@gmail.com
#
# ATLEAST GIVE CREDITS IF YOU STEALING :
# ELSE NO FURTHER PUBLIC THUMBNAIL UPDATES

    import os
import random
import traceback
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from py_yt import VideosSearch
import aiohttp
import aiofiles
import math

# Safe fallback in case AloneMusic.app is missing
try:
    from AloneMusic import app
except ImportError:
    app = type('App', (), {'username': 'AloneMusic'})()  # fallback username

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

CANVAS_W, CANVAS_H = 1320, 760
FONT_REGULAR_PATH = "AloneMusic/assets/font2.ttf"
FONT_BOLD_PATH = "AloneMusic/assets/font3.ttf"
DEFAULT_THUMB = "AloneMusic/assets/AloneMusicBots.jpg"

# ----------------- Helper Functions ----------------- #

def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if draw.textlength(test_line, font=font) <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines[:2]

def random_gradient():
    gradients = [
        [(15, 12, 41), (48, 43, 99), (36, 36, 62)],
        [(10, 10, 10), (35, 35, 40), (20, 20, 25)],
        [(26, 26, 46), (56, 56, 86), (40, 40, 60)],
    ]
    return random.choice(gradients)

def apply_gradient(canvas, colors):
    overlay = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for y in range(CANVAS_H):
        progress = y / CANVAS_H
        if progress < 0.4:
            t = progress / 0.4
            r = int(colors[0][0] * (1-t) + colors[1][0] * t)
            g = int(colors[0][1] * (1-t) + colors[1][1] * t)
            b = int(colors[0][2] * (1-t) + colors[1][2] * t)
        else:
            t = (progress - 0.4) / 0.6
            r = int(colors[1][0] * (1-t) + colors[2][0] * t)
            g = int(colors[1][1] * (1-t) + colors[2][1] * t)
            b = int(colors[1][2] * (1-t) + colors[2][2] * t)
        draw.line([(0, y), (CANVAS_W, y)], fill=(r, g, b, 255))
    return Image.alpha_composite(canvas, overlay)

# ----------------- Main gen_thumb Function ----------------- #

async def gen_thumb(videoid: str):
    """
    Old gen_thumb logic goes here.
    Copy everything from your previous gen_thumb function
    starting with fetching YouTube video and generating thumbnail.
    """
    # ... paste your full gen_thumb code here ...
    pass

# ----------------- Exported get_thumb ----------------- #

    

