from application import app, manager
from flask_script import Server

# 配置runserver指令
manager.add_command('runserver',Server(use_debugger=True,use_reloader=True,host='0.0.0.0',port="6000"))
def main():
    manager.run()
if __name__ == '__main__':

    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()