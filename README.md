# 江苏省第十四届大学生知识竞赛（理工科组）现场照片下载脚本

- 该脚本用于下载2024年江苏省第十四届大学生知识竞赛（理工科组）现场照片。
-  [script1.py](./script1.py) 和 [script2.py](./script2.py) 下载方式不同：
   - [script1.py](./script1.py) 点击 `下载` 按钮后再点击 `下一张` 按钮；
   - [script2.py](./script2.py) 找到 `下载` 按钮并设置 `onclick` 属性为 `downloadPhoto({})` ，其中 `{}` 是当前图片的索引。

## 安装

1. 克隆仓库：
   ```sh
   git clone https://github.com/tinsyding/Jiangsu-14th-Knowledge-Competition.git
   cd jiangsu-14th-knowledge-competition
   ```

2. 安装所需的Python包：
   ```sh
   pip install selenium webdriver-manager
   ```

## 使用方法

1. 打开 [script1.py](./script1.py) 文件并检查浏览器、暂停时间等配置。

2. 运行脚本：
   ```sh
   python script1.py
   ```