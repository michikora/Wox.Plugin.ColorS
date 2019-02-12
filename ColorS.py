# -*- coding: utf-8 -*-
import os
import re
import subprocess
from PIL import Image
from Picker import ColorsPicker
from wox import Wox, WoxAPI

class ColorsViewer(Wox):

    def query(self, query):
        result = []
        if not query:
            result.append({
                "Title": "Red",
                "SubTitle": "#F44336",
                "IcoPath": "./icon/f44336.png",
            })
            result.append({
                "Title": "Pink",
                "SubTitle": "#E91E63",
                "IcoPath": "./icon/e91e63.png",
            })
            result.append({
                "Title": "Purple",
                "SubTitle": "#9C27B0",
                "IcoPath": "./icon/9c27b0.png",
            })
            result.append({
                "Title": "Deeppurple",
                "SubTitle": "#673AB7",
                "IcoPath": "./icon/673ab7.png",
            })
            result.append({
                "Title": "Indigo",
                "SubTitle": "#3F51B5",
                "IcoPath": "./icon/3f51b5.png",
            })
            result.append({
                "Title": "Blue",
                "SubTitle": "#2196F3",
                "IcoPath": "./icon/2196f3.png",
            })
            result.append({
                "Title": "Lightblue",
                "SubTitle": "#03A9F4",
                "IcoPath": "./icon/03a9f4.png",
            })
            result.append({
                "Title": "Cyan",
                "SubTitle": "#00BCD4",
                "IcoPath": "./icon/00bcd4.png",
            })
            result.append({
                "Title": "Teal",
                "SubTitle": "#009688",
                "IcoPath": "./icon/009688.png",
            })
            result.append({
                "Title": "Green",
                "SubTitle": "#4CAF50",
                "IcoPath": "./icon/4caf50.png",
            })
            result.append({
                "Title": "Lightgreen",
                "SubTitle": "#8BC34A",
                "IcoPath": "./icon/8bc34a.png",
            })
            result.append({
                "Title": "Lime",
                "SubTitle": "#CDDC39",
                "IcoPath": "./icon/cddc39.png",
            })
            result.append({
                "Title": "Yellow",
                "SubTitle": "#FFEB3B",
                "IcoPath": "./icon/ffeb3b.png",
            })
            result.append({
                "Title": "Amber",
                "SubTitle": "#FFC107",
                "IcoPath": "./icon/ffc107.png",
            })
            result.append({
                "Title": "Orange",
                "SubTitle": "#FF9800",
                "IcoPath": "./icon/ff9800.png",
            })
            result.append({
                "Title": "Deeporange",
                "SubTitle": "#FF5722",
                "IcoPath": "./icon/ff5722.png",
            })
            result.append({
                "Title": "Brown",
                "SubTitle": "#795548",
                "IcoPath": "./icon/795548.png",
            })
            result.append({
                "Title": "Grey",
                "SubTitle": "#9E9E9E",
                "IcoPath": "./icon/9e9e9e.png",
            })
            result.append({
                "Title": "Bluegrey",
                "SubTitle": "#607D8B",
                "IcoPath": "./icon/607d8b.png",
            })
            return result
        elif re.match('#', query):
            colorRGB = []
            hex2RGB = re.split('(..)',query.strip('#'))[1::2]
            for line in hex2RGB:
                colorRGB.append(int(line, 16))
            colorRGB = tuple(colorRGB)
            if os.path.isdir('./colors/convert'):
                pass
            else:
                os.mkdir('./colors/convert')
            if os.path.isfile('./colors/convert/'+query.strip('#')+'.png'):
                pass
            else:
                thumbSize = (2, 2)
                colorThumb = Image.new('RGB', thumbSize, colorRGB)
                colorThumb.save('./colors/convert/'+query.strip('#')+'.png')
            result.append({
                "Title": str(colorRGB),
                "SubTitle": query,
                "IcoPath": "colors/convert/"+query.strip('#')+".png",
                'JsonRPCAction':{
                    'method': 'copy_colorHex',
                    'parameters': [str(colorRGB).strip('()')],
                    'dontHideAfterAction': False
                    }
            })
            return result
        elif re.match('(^\()?[0-9]+\s?,?\s?[0-9]+\s?,?\s?[0-9]+\s?($\))?', query):
            colorHex = ''
            rgb2Hex = query.strip('(')
            rgb2Hex = rgb2Hex.strip(')')
            rgb2Hex = list(filter(lambda x: len(x) > 0,re.split(',|\s',rgb2Hex)))
            rgb2Hex = map(int, rgb2Hex)
            rgb2Hex = tuple(rgb2Hex)
            for line in rgb2Hex:
                isDigit = '%x' % line
                if len(isDigit) == 1:
                    isDigit = '0' + isDigit
                colorHex += isDigit
            if os.path.isdir('./colors/convert'):
                pass
            else:
                os.mkdir('./colors/convert')
            if os.path.isfile('./colors/convert/'+colorHex+'.png'):
                pass
            else:
                thumbSize = (2, 2)
                colorThumb = Image.new('RGB', thumbSize, rgb2Hex)
                colorThumb.save('./colors/convert/'+colorHex+'.png')
            result.append({
                "Title": "#" + colorHex.upper(),
                "SubTitle": query,
                "IcoPath": "colors/convert/"+colorHex+".png",
                'JsonRPCAction':{
                    'method': 'copy_colorHex',
                    'parameters': [colorHex],
                    'dontHideAfterAction': False
                    }
            })
            return result
        elif query.capitalize() == "Red":
            listUp = ColorsPicker()
            for line in listUp.redPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/red/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Pink":
            listUp = ColorsPicker()
            for line in listUp.pinkPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/pink/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Purple":
            listUp = ColorsPicker()
            for line in listUp.purplePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/purple/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Deeppurple":
            listUp = ColorsPicker()
            for line in listUp.deeppurplePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/deeppurple/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Indigo":
            listUp = ColorsPicker()
            for line in listUp.indigoPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/indigo/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Blue":
            listUp = ColorsPicker()
            for line in listUp.bluePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/blue/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Lightblue":
            listUp = ColorsPicker()
            for line in listUp.lightbluePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/lightblue/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Cyan":
            listUp = ColorsPicker()
            for line in listUp.cyanPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/cyan/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Teal":
            listUp = ColorsPicker()
            for line in listUp.tealPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/teal/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Green":
            listUp = ColorsPicker()
            for line in listUp.greenPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/green/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Lightgreen":
            listUp = ColorsPicker()
            for line in listUp.lightgreenPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/lightgreen/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Lime":
            listUp = ColorsPicker()
            for line in listUp.limePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/lime/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Yellow":
            listUp = ColorsPicker()
            for line in listUp.yellowPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/yellow/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Amber":
            listUp = ColorsPicker()
            for line in listUp.amberPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/amber/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Orange":
            listUp = ColorsPicker()
            for line in listUp.orangePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/orange/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Deeporange":
            listUp = ColorsPicker()
            for line in listUp.deeporangePicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/deeporange/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Brown":
            listUp = ColorsPicker()
            for line in listUp.brownPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/brown/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Grey":
            listUp = ColorsPicker()
            for line in listUp.greyPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/grey/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        elif query.capitalize() == "Bluegrey":
            listUp = ColorsPicker()
            for line in listUp.bluegreyPicker:
                result.append({
                    "Title": line['colorName'],
                    "Subtitle": "#" + line['colorHex'].upper() + str(line['colorRGB']),
                    "IcoPath": "colors/bluegrey/"+line['colorHex']+".png",
                    'JsonRPCAction':{
                        'method': 'copy_colorHex',
                        'parameters': [line['colorHex']],
                        'dontHideAfterAction': False
                    }
                })
            return result

        else:
            result.append({
                "Title": "Red",
                "SubTitle": "#F44336",
                "IcoPath": "./icon/f44336.png",
            })
            result.append({
                "Title": "Pink",
                "SubTitle": "#E91E63",
                "IcoPath": "./icon/e91e63.png",
            })
            result.append({
                "Title": "Purple",
                "SubTitle": "#9C27B0",
                "IcoPath": "./icon/9c27b0.png",
            })
            result.append({
                "Title": "Deeppurple",
                "SubTitle": "#673AB7",
                "IcoPath": "./icon/673ab7.png",
            })
            result.append({
                "Title": "Indigo",
                "SubTitle": "#3F51B5",
                "IcoPath": "./icon/3f51b5.png",
            })
            result.append({
                "Title": "Blue",
                "SubTitle": "#2196F3",
                "IcoPath": "./icon/2196f3.png",
            })
            result.append({
                "Title": "Lightblue",
                "SubTitle": "#03A9F4",
                "IcoPath": "./icon/03a9f4.png",
            })
            result.append({
                "Title": "Cyan",
                "SubTitle": "#00BCD4",
                "IcoPath": "./icon/00bcd4.png",
            })
            result.append({
                "Title": "Teal",
                "SubTitle": "#009688",
                "IcoPath": "./icon/009688.png",
            })
            result.append({
                "Title": "Green",
                "SubTitle": "#4CAF50",
                "IcoPath": "./icon/4caf50.png",
            })
            result.append({
                "Title": "Lightgreen",
                "SubTitle": "#8BC34A",
                "IcoPath": "./icon/8bc34a.png",
            })
            result.append({
                "Title": "Lime",
                "SubTitle": "#CDDC39",
                "IcoPath": "./icon/cddc39.png",
            })
            result.append({
                "Title": "Yellow",
                "SubTitle": "#FFEB3B",
                "IcoPath": "./icon/ffeb3b.png",
            })
            result.append({
                "Title": "Amber",
                "SubTitle": "#FFC107",
                "IcoPath": "./icon/ffc107.png",
            })
            result.append({
                "Title": "Orange",
                "SubTitle": "#FF9800",
                "IcoPath": "./icon/ff9800.png",
            })
            result.append({
                "Title": "Deeporange",
                "SubTitle": "#FF5722",
                "IcoPath": "./icon/ff5722.png",
            })
            result.append({
                "Title": "Brown",
                "SubTitle": "#795548",
                "IcoPath": "./icon/795548.png",
            })
            result.append({
                "Title": "Grey",
                "SubTitle": "#9E9E9E",
                "IcoPath": "./icon/9e9e9e.png",
            })
            result.append({
                "Title": "Bluegrey",
                "SubTitle": "#607D8B",
                "IcoPath": "./icon/607d8b.png",
            })
            return result

    def copy_colorHex(self, colorHex):
        #command = 'echo ' + colorHex.strip() + '| clip'
        #os.system(command)
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        clip = subprocess.Popen(['clip'], stdin=subprocess.PIPE, encoding='utf-8', startupinfo=startupinfo)
        clip.communicate(input = colorHex.strip())


if __name__ == "__main__":
    ColorsViewer()
