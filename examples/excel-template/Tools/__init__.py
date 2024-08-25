# coding: UTF-8
from .OtherTools import *
from .LogTools import LogTools
from .TkTools import TkTools
from .SysTools import SysTools
from .ExcelTools import ExcelTools
from .JsonTools import JsonTools




class _Tools():
    def __init__(self):
        self.logTools  = LogTools()
        _log = self.logTools.getlogger()
        self.log = _log
        # 全局参数
        self.gdata = {}
        self.tmp = {}
        self.commonStatic = CommonStatic
        self.render = web.template.render(CommonStatic.root_path + '/static/pages/')

        self.out = OutTools(log=_log)
        self.sys = SysTools(log=_log)
        self.tk = TkTools()
        self.excel = ExcelTools(log=_log)
        
        self.json = JsonTools(log=_log)
        print ( "xxxxxxxxxxxxx_Tools init json" + str(self.json))
        self.returnData = ReturnData( jsonTools =  self.json )
        # self.init_log_file("/tmp/main.log")


    def init_log_file(self,file_path):
        directory_path = os.path.dirname(os.path.abspath(file_path))
        print(directory_path)
        self.sys.cdir(directory_path)
        self.logTools.set_log_file(file_path)


tools = _Tools()

__all__ = ["WebApp","tools","LogTools"]
