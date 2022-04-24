#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://realpython.com/lessons/import-statement/
# https://realpython.com/python-logging/
#
#  https://pyyaml.org/wiki/PyYAMLDocumentation
#
# from <module_name> import <name(s)>
# An alternate form of the import statement allows individual 
# objects from the module to be imported directly into the caller’s symbol table:
#
#>>> try:
#...     # Non-existent module
#...     import foo
#... except ImportError:
#...     print('Module not found')
# 
import logging
import logging.config
import yaml

myFruits = ["Apple", "Orange", "Banana", "Strawberry", "Mango"]

def functionInfo():
    logger = logging.getLogger(__name__ + ":" + functionInfo.__name__)
    logger.info('This is a info message')

def functionWarning():
    logger = logging.getLogger(__name__ + ":" + functionWarning.__name__)
    logger.warning('This is a warn message')

def printFruits( fruits):
    logger = logging.getLogger(__name__ + ":" + printFruits.__name__)

    logger.info("print fruits 1 way:")
    for fruit in fruits:
       logger.info(fruit)
 
    logger.info("\n\nprint fruits 2 way:")
    logger.info("Fruits: %s", fruits)

    logger.info("\n\nprint fruits 3 way:")
    logger.info("Fruits: " + " ".join(fruits))

    logger.info("\n\nprint fruits 4 way:")
    logger.info("Fruits:" + '\n'.join(map(str, fruits)))

def main():
    with open('./resources/logging_config.yml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message')

    functionInfo()
    functionWarning()
    printFruits(myFruits)

if __name__ == "__main__":
    main()