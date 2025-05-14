from configparser import ConfigParser


def get_config(category, key):
    config = ConfigParser()
    config.read("D:\\pythonselenium\\assignmentSeleniumPython\\ass\\datadriven_assignes_pro\\config.ini")  
    return config.get(category, key)
