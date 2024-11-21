from flask import Blueprint, jsonify,request
from config.constants import SHARED_USER_ID,SHARED_KEY,SHARED_TOKEN
from utils.tools import get_current_timestamp

fakelocation_blueprint = Blueprint('fakelocation', __name__)

@fakelocation_blueprint.route('/app/getAppConfigs', methods=['POST'])
def get_app_configs():

    response_body = {
        "body": {
            "createTime": get_current_timestamp(),
            "disabledApps": [],
            "disabledFuncs": [],
            "disabledInfos": [],
            "isAllowRun": 1,
            "isAvailable": 1,
            "notice": "",
            "updateTime": 0
        },
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }

    data = request.json
    print(f"Received POST data: {data}")
    return jsonify(response_body)

@fakelocation_blueprint.route('/version/checkApkUpdate', methods=['POST'])
def check_apk_update():
    response_body = {
        "code": 1,
        "message": "??????",
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return jsonify(response_body)

@fakelocation_blueprint.route('/goods/getRenewalGoodsList', methods=['POST'])
def get_renewal_goods_list():
    response_body = {
        "body": [
            {
                "createTime": 0,
                "description": "",
                "id": "0011",
                "isAvailable": 1,
                "locale": "*",
                "name": "永久使用无限制",
                "price": 0,
                "priceUnit": "¥",
                "recommend": "BobH",
                "updateTime": 0,
                "value": 30,
                "weight": 4
            }
        ],
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return jsonify(response_body)

@fakelocation_blueprint.route('/user/get', methods=['POST'])
def user_get():
    response_body = {
        "body": {
            "regtime": get_current_timestamp() - 1000 * 60 * 60,
            "proindate": get_current_timestamp() + 1000 * 60 * 60 * 24 * 365,
            "createTime": get_current_timestamp() - 1000 * 60 * 60 - 1,
            "loginType": "email",
            "loginName": "BobH" + "Crack",
            "updateTime": 0,
            "type": 1,
            "key": SHARED_KEY,
            "token": SHARED_TOKEN
        },
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return jsonify(response_body)

@fakelocation_blueprint.route('/user/login', methods=['POST'])
def user_login():
    response_body = {
            "body": {
                "regtime": get_current_timestamp() - 1000 * 60 * 60,
                "proindate": get_current_timestamp() + 1000 * 60 * 60 * 24 * 365,
                "createTime": get_current_timestamp() - 1000 * 60 * 60 - 1,
                "loginType": "email",
                "loginName": "BobH" + "Crack",
                "updateTime": 0,
                "type": 1,
                "userId": SHARED_USER_ID,
                "key": SHARED_KEY,
                "token": SHARED_TOKEN
            },
            "code": 200,
            "returnTime": get_current_timestamp(),
            "success": True
        }
    return jsonify(response_body)

@fakelocation_blueprint.route('/user/checkUserExist', methods=['POST'])
@fakelocation_blueprint.route('/user/checkPwdExist', methods=['POST'])
def user_check_user_exist():
    response_body = {
        "body": True,
        "code": 200,
        "returnTime": get_current_timestamp(),
        "success": True
    }
    return jsonify(response_body)

@fakelocation_blueprint.route('cell/queryNearby', methods=['POST'])
def cell_query_nearby():
    data = request.data
    print(data)
    return jsonify()