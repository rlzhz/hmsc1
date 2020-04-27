from flask import Blueprint

from common.libs.Helper import ops_render
from common.models.User import User


router_account = Blueprint("account_page",__name__)

@router_account.route('/index',)
def index():
    resp_data ={}
    list = User.query.all()
    resp_data['list'] = list
    return ops_render('account/index.html',resp_data)

@router_account.route('/info',)
def info():
    return ops_render('account/info.html')

@router_account.route('/set',)
def set():
    return ops_render('account/set.html')