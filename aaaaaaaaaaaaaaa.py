
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                   #datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='ceshi1.log',
                   filemode='w')

logging.debug('====This is debug message')
logging.info('====This is info message')
logging.warning('====This is warning message')

'''
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n=%d'%n)
print(10 / n)
'''
