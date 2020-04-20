from flask import Flask
from flask_script import Manager
import os

class Applciation(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super(Applciation,self).__init__(import_name,template_folder=template_folder,root_path=root_path)


app = Flask(__name__,template_folder=os.getcwd()+'/web/templates/',root_path=os.getcwd())
manager = Manager(app)

