import os
import sys

import modules.logic.conversation.os.const as constant

def SYSTEM__OFF():
    os.system('shutdown -s')

def CREATE__DIR(dir_name):
    os.mkdir(constant.dir_path_core + dir_name)

def REMOVE__DIR(dir_name):
    print(constant.dir_path_core + dir_name)
    if os.path.exists(constant.dir_path_core + dir_name):
        os.rmdir(constant.dir_path_core + dir_name)
        return 'Требуемая директория была успешно удалена'
    else:
        return 'Такой директории не существует в моём хранилище'

def START__BROWSER(browser_name):
    if browser_name == 'опера':
        os.startfile(r"C:\Users\King of sweets\AppData\Local\Programs\Opera GX\launcher.exe")
        return 'Браузер Opera GX был успешно запущен'

    else:
        return 'Такого браузера нет на вашей системе'