# -*- coding: utf-8 -*-
import re
import os
import codecs
import os.path
from PIL import Image

class ColorsPicker:

    def __init__(self):
        self.redPicker = []
        self.pinkPicker = []
        self.purplePicker = []
        self.deeppurplePicker = []
        self.indigoPicker = []
        self.bluePicker = []
        self.lightbluePicker = []
        self.cyanPicker = []
        self.tealPicker = []
        self.greenPicker = []
        self.lightgreenPicker = []
        self.limePicker = []
        self.yellowPicker = []
        self.amberPicker = []
        self.orangePicker = []
        self.deeporangePicker = []
        self.brownPicker = []
        self.greyPicker = []
        self.bluegreyPicker = []

        redFin = codecs.open('./colors/red.txt', 'r', 'utf-8')
        for line in redFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/red'):
                pass
            else:
                os.mkdir('./colors/red')
            if os.path.isfile('./colors/red/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/red/'+colorHex+'.png')
            self.redPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        redFin.close()

        pinkFin = codecs.open('./colors/pink.txt', 'r', 'utf-8')
        for line in pinkFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/pink'):
                pass
            else:
                os.mkdir('./colors/pink')
            if os.path.isfile('./colors/pink/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/pink/'+colorHex+'.png')
            self.pinkPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        pinkFin.close()

        purpleFin = codecs.open('./colors/purple.txt', 'r', 'utf-8')
        for line in purpleFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/purple'):
                pass
            else:
                os.mkdir('./colors/purple')
            if os.path.isfile('./colors/purple/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/purple/'+colorHex+'.png')
            self.purplePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        purpleFin.close()

        deeppurpleFin = codecs.open('./colors/deeppurple.txt', 'r', 'utf-8')
        for line in deeppurpleFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/deeppurple'):
                pass
            else:
                os.mkdir('./colors/deeppurple')
            if os.path.isfile('./colors/deeppurple/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/deeppurple/'+colorHex+'.png')
            self.deeppurplePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        deeppurpleFin.close()

        indigoFin = codecs.open('./colors/indigo.txt', 'r', 'utf-8')
        for line in indigoFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/indigo'):
                pass
            else:
                os.mkdir('./colors/indigo')
            if os.path.isfile('./colors/indigo/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/indigo/'+colorHex+'.png')
            self.indigoPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        indigoFin.close()

        blueFin = codecs.open('./colors/blue.txt', 'r', 'utf-8')
        for line in blueFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/blue'):
                pass
            else:
                os.mkdir('./colors/blue')
            if os.path.isfile('./colors/blue/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/blue/'+colorHex+'.png')
            self.bluePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        blueFin.close()

        lightblueFin = codecs.open('./colors/lightblue.txt', 'r', 'utf-8')
        for line in lightblueFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/lightblue'):
                pass
            else:
                os.mkdir('./colors/lightblue')
            if os.path.isfile('./colors/lightblue/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/lightblue/'+colorHex+'.png')
            self.lightbluePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        lightblueFin.close()

        cyanFin = codecs.open('./colors/cyan.txt', 'r', 'utf-8')
        for line in cyanFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/cyan'):
                pass
            else:
                os.mkdir('./colors/cyan')
            if os.path.isfile('./colors/cyan/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/cyan/'+colorHex+'.png')
            self.cyanPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        cyanFin.close()

        tealFin = codecs.open('./colors/teal.txt', 'r', 'utf-8')
        for line in tealFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/teal'):
                pass
            else:
                os.mkdir('./colors/teal')
            if os.path.isfile('./colors/teal/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/teal/'+colorHex+'.png')
            self.tealPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        tealFin.close()

        greenFin = codecs.open('./colors/green.txt', 'r', 'utf-8')
        for line in greenFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/green'):
                pass
            else:
                os.mkdir('./colors/green')
            if os.path.isfile('./colors/green/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/green/'+colorHex+'.png')
            self.greenPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        greenFin.close()

        lightgreenFin = codecs.open('./colors/lightgreen.txt', 'r', 'utf-8')
        for line in lightgreenFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/lightgreen'):
                pass
            else:
                os.mkdir('./colors/lightgreen')
            if os.path.isfile('./colors/lightgreen/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/lightgreen/'+colorHex+'.png')
            self.lightgreenPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        lightgreenFin.close()

        limeFin = codecs.open('./colors/lime.txt', 'r', 'utf-8')
        for line in limeFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/lime'):
                pass
            else:
                os.mkdir('./colors/lime')
            if os.path.isfile('./colors/lime/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/lime/'+colorHex+'.png')
            self.limePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        limeFin.close()

        yellowFin = codecs.open('./colors/yellow.txt', 'r', 'utf-8')
        for line in yellowFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/yellow'):
                pass
            else:
                os.mkdir('./colors/yellow')
            if os.path.isfile('./colors/yellow/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/yellow/'+colorHex+'.png')
            self.yellowPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        yellowFin.close()

        amberFin = codecs.open('./colors/amber.txt', 'r', 'utf-8')
        for line in amberFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/amber'):
                pass
            else:
                os.mkdir('./colors/amber')
            if os.path.isfile('./colors/amber/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/amber/'+colorHex+'.png')
            self.amberPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        amberFin.close()

        orangeFin = codecs.open('./colors/orange.txt', 'r', 'utf-8')
        for line in orangeFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/orange'):
                pass
            else:
                os.mkdir('./colors/orange')
            if os.path.isfile('./colors/orange/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/orange/'+colorHex+'.png')
            self.orangePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        orangeFin.close()

        deeporangeFin = codecs.open('./colors/deeporange.txt', 'r', 'utf-8')
        for line in deeporangeFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/deeporange'):
                pass
            else:
                os.mkdir('./colors/deeporange')
            if os.path.isfile('./colors/deeporange/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/deeporange/'+colorHex+'.png')
            self.deeporangePicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        deeporangeFin.close()

        brownFin = codecs.open('./colors/brown.txt', 'r', 'utf-8')
        for line in brownFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/brown'):
                pass
            else:
                os.mkdir('./colors/brown')
            if os.path.isfile('./colors/brown/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/brown/'+colorHex+'.png')
            self.brownPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        brownFin.close()

        greyFin = codecs.open('./colors/grey.txt', 'r', 'utf-8')
        for line in greyFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/grey'):
                pass
            else:
                os.mkdir('./colors/grey')
            if os.path.isfile('./colors/grey/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/grey/'+colorHex+'.png')
            self.greyPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        greyFin.close()

        bluegreyFin = codecs.open('./colors/bluegrey.txt', 'r', 'utf-8')
        for line in bluegreyFin:
            line = line.strip()
            try:
                colorName, colorHex = line.split()
            except ValueError:
                continue
            colorRGB = []
            hex2RGB = re.split('(..)',colorHex)[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/bluegrey'):
                pass
            else:
                os.mkdir('./colors/bluegrey')
            if os.path.isfile('./colors/bluegrey/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (64, 64)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/bluegrey/'+colorHex+'.png')
            self.bluegreyPicker.append({'colorName':colorName, 'colorHex':colorHex, 'colorRGB':colorRGB})
        bluegreyFin.close()

    def redPicker(self):
        return self.redPicker

    def pinkPicker(self):
        return self.pinkPicker

    def purplePicker(self):
        return self.purplePicker

    def deeppurplePicker(self):
        return self.deeppurplePicker

    def indigoPicker(self):
        return self.indigoPicker

    def bluePicker(self):
        return self.bluePicker

    def lightbluePicker(self):
        return self.lightbluePicker

    def cyanPicker(self):
        return self.cyanPicker

    def tealPicker(self):
        return self.tealPicker

    def greenPicker(self):
        return self.greenPicker

    def lightgreenPicker(self):
        return self.lightgreenPicker

    def limePicker(self):
        return self.limePicker

    def yellowPicker(self):
        return self.yellowPicker

    def amberPicker(self):
        return self.amberPicker

    def orangePicker(self):
        return self.orangePicker

    def deeporangePicker(self):
        return self.deeporangePicker

    def brownPicker(self):
        return self.brownPicker

    def greyPicker(self):
        return self.greyPicker

    def bluegreyPicker(self):
        return self.bluegreyPicker
