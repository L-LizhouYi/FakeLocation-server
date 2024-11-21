from flask import Flask

from routes.fakelocations import fakelocation_blueprint
from routes.notices import notices_blueprint
from routes.ads import ads_blueprint

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(fakelocation_blueprint, url_prefix='/FakeLocation')
app.register_blueprint(notices_blueprint, url_prefix='/Notice')
app.register_blueprint(ads_blueprint, url_prefix='/Ads')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


# fakelocation.api.lerist.cc
# notice.api.lerist.cc
# ads.api.lerist.cc