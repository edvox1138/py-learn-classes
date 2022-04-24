#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
    # set up logging to file 
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='./logs-are-here.log',
                        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logger = logging.getLogger(__name__)

    logger.debug('This is a debug message')

    functionInfo()
    functionWarning()
    printFruits(myFruits)

if __name__ == "__main__":
    main()