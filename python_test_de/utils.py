""" Module containing useful python fonctions """

import yaml
import logging

def get_configuration(file_path):
    """Reads ans parses a yaml file configuration file

    :param yml_path: A string correspondig to path of yaml file
    :return: A disct
    """
    try:
        with open(file_path) as file:
            return yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        logging.exception('File does not exist or file path contains an error.')