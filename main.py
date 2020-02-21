import logging

import shawn_logger

shawn_logger.set_job_id('testjobid')
shawn_logger.set_task_name('testtaskname')

logger = logging.getLogger(__name__)
logging.basicConfig(format='', level=logging.DEBUG)


def demo():
    logger.info('message')
    logging.debug('debug message')


if __name__ == '__main__':
    demo()
