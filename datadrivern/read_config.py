import configparser

config = configparser.ConfigParser()
config.read("datadrivern/config.ini")  
def get_config(category, key):
    return config.get(category, key)
