import logging

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("Student.log",mode = 'a'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
