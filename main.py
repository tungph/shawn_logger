import logging

import shawn_logger

shawn_logger.job_id = 'SHAWN_TASK_ID'
shawn_logger.task_name = 'SHAWN_TASK_NAME'

logger = logging.getLogger(__name__)
logging.basicConfig(format='', level=logging.DEBUG)


def demo():
    logger.info('message')
    logging.debug('debug message')


if __name__ == '__main__':
    demo()
