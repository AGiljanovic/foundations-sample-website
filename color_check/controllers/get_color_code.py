# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json, os
# import logging
# logging.basicConfig(handlers=[logging.FileHandler(os.path.dirname
#                     (__file__) + '/../data/log.txt', 'w', 'utf-8')])


def get_color_code(color_name):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    with open(os.path.dirname(__file__) + '/../data/css-color-names.json') as colors_list:

        # logging.debug('This is a debug message')
        # logging.info('Info:')
        # logging.warning('Warnings:')
        # logging.error('Errors:')

        colors = json.load(colors_list)
        try:
            color_code = colors.get(color_name)
        except:
            color_code = f"The color '{color_name}' Doesn’t seem to exist :/"

        return color_code


print(get_color_code("blue"))
