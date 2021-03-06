#! /usr/bin/env python

import os, sys
import pygame
from pygame.locals import *

def load_image(name, colorkey=None, char_scale=False):
    """
    Chr_scale determines if should be scaled up to bigger than 64x64
    """
    fullname = os.path.join('..\\','sprites')
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if char_scale:
        image = pygame.transform.scale2x(image)
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def getAnimation(image_prefix, char_scale=False):
    """Return a list of images in order
    representing the frames of the animation
    given by the passed prefix (image_prefix should
    include the final underscore)
    Expects images in the sprites folder of the form
    name_of_animation_####.png where #### is the 4 digit frame number
    and sprite is in png format
    (i.e. as exported from GraphicsGale)
    """
    
    fullname_prefix = os.path.join('..\\','sprites')
    fullname_prefix = os.path.join(fullname_prefix, image_prefix)
    
    #Make sure at least the first frame is there
    try:
        image = pygame.image.load(fullname_prefix + '0000.png')
    except pygame.error, message:
        print 'Cannot load image:', image_prefix + \
            '0000.png not found in images folder'
        raise SystemExit, message
    
    #Loop through the frames
    result = []
    index = 0
    while True:
        suffix = "%04d" % index
        try:
            image = pygame.image.load(fullname_prefix + suffix + '.png')
            image = image.convert()
            if char_scale:
                image = pygame.transform.scale2x(image)
            colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
            result.append(image)
        except pygame.error, message:
            #Done loading frames, break
            break
        index += 1
    return result