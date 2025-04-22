# 🌍 FakeLocation-server

**FakeLocation-server** 是一个基于 Flask 的轻量级虚拟定位服务端项目，旨在为开发和测试环境提供灵活的伪定位接口，并支持公告与广告的管理功能。该项目采用 Flask Blueprint 进行模块化设计，结构清晰，易于扩展和维护。

## ✨ 功能特色

- 📍 **虚拟定位接口** – 模拟 GPS 坐标，方便测试基于位置的应用功能。
- 📢 **公告接口** – 提供系统公告或应用通知的管理与获取。
- 📺 **广告接口** – 支持测试广告的推送与展示。
- 🔧 基于 Flask Blueprint 的模块化架构。
- 🚀 支持本地或服务器环境快速部署。

## 🛠 技术栈

- Python 3
- Flask 框架
- RESTful API 设计风格

## 📂 项目结构

```bash
FakeLocation-server/
├── app.py
├── README.md
├── apk
│   └── FakeLocation1.3.0.2.apk
├── config
│   └── constants.py
├── routes
│   ├── ads.py
│   ├── fakelocations.py
│   └── notices.py
└── utils
    └── tools.py
```


## 🚀 快速开始

### 环境要求

- Python 3.7+
- pip（Python 包管理器）

### 安装依赖

```bash
git clone https://github.com/yourusername/FakeLocation-server.git
cd FakeLocation-server
pip install -r requirements.txt
```



## 启动服务

```bash
python app.py
```

