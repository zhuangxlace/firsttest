import logging
class print_log():
    def printlog_fun(self):
        logging.basicConfig(
                level=logging.INFO,  # 定义输出到文件的log级别，大于此级别的都被输出  CRITICAL:50;ERROR:40;ARNING:30;INFO:20;DEBUG:10
                #format='%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s',
                format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
                datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
                filename="d:/pythonworkspace/interfaceframework/util/logfile.log",  # log文件名
                filemode='w')  # 写入模式“w”或“a”
        
        console = logging.StreamHandler()  # 定义stream handler 输出到控制台
        console.setLevel(logging.INFO)  # 定义该handler级别
        formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
        console.setFormatter(formatter)
        # Create an instance
        logging.getLogger().addHandler(console)  # 实例化添加handler
        
        # Print information              # 输出日志级别
        logging.debug('logger debug message')
        logging.info('logger info message')
        logging.warning('logger warning message')
        logging.error('logger error message')
        logging.critical('logger critical message')

if __name__=="__main__":
    pl=print_log()
    pl.printlog_fun()