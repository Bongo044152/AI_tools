import logging
flag=False
def init_printer():
    global flag
    if(flag==True):
        return
    flag=True
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - [%(levelname)s] - %(message)s'
    )
logger=logging.getLogger(__name__)
def printer(var_value):
    logger.debug(f"{var_value}")
    


