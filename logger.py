import logging

# 로거 생성
logger = logging.getLogger('goloop')
logger.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)-8s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 파일 핸들러 생성
file_handler = logging.FileHandler('my_log.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# 콘솔 핸들러 생성
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# 핸들러를 로거에 추가
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 로그 메시지 출력
logger.debug('Debug 메시지')
logger.info('Info 메시지')
logger.warning('Warning 메시지')
logger.error('Error 메시지')
logger.critical('Critical 메시지')
