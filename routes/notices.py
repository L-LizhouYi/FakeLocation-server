from flask import Blueprint, jsonify

notices_blueprint = Blueprint('notice', __name__)

@notices_blueprint.route('/getNotices', methods=['POST'])
def notice_getNotices():
    notice_data = [
        {
            "content": "<p><strong>这是由BobH破解的FakeLocationApp的服务端发送的消息</strong></p>\r\n\r\n<p><strong>请勿将此软件用于非法用途，请勿用于出售或非法盈利</strong></p>\r\n\r\n",
            "createTime": 0,
            "flavor": "*",
            "id": "00008",
            "isAvailable": True,
            "isNeedAgree": True,
            "language": "*",
            "needAgree": True,
            "title": "破解说明",
            "type": "text",
            "weight": 100001
        }
    ]
    return jsonify(notice_data)