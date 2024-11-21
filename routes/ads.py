from flask import Blueprint, jsonify

ads_blueprint = Blueprint('ads', __name__)
@ads_blueprint.route('/getAds', methods=['POST'])
def ads_getads():
    response_body =  [
        {
            "available": True,
            "createTime": 0,
            "intervalTime": 30000,
            "isAvailable": True,
            "isRandom": True,
            "language": "*",
            "provider": "BobH",
            "random": False,
            "texts": "此软件已经连接破解版服务器，无需再进行购买即可免费不限制使用",
            "urls": "#",
            "weight": 3
        },
        {
            "available": True,
            "createTime": 0,
            "intervalTime": 16000,
            "isAvailable": True,
            "isRandom": False,
            "language": "*",
            "provider": "BobH",
            "random": False,
            "texts": "已经解锁了软件的全部应用模拟功能，不再有特定应用无法使用的问题",
            "urls": "#",
            "weight": 2
        }
    ]
    return jsonify(response_body)