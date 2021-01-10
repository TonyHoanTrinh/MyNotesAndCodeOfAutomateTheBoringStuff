#! /usr/bin/env python3
import logging
logging.basicConfig(level=logging.DEBUG, format = ' %(asctime)s - %(levelname)s -%(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial (%s%%)' % (n))
    return total

print(factorial(5))
logging.debug('End of program')

# Logging Levels
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# logging.dsiable(logging.CRITICAL) to remove logs 
# logging to a file - logging.basicConfig(filename = 'myProgramLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')