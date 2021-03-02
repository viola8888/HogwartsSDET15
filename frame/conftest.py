"""录屏"""
import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def record_vedio():
    print("录制准备")
    # 使用 scrcpy 工具录屏
    command = "scrcpy --record D:\code_hogwarts\/actual_combat\/frame\/tmp.mp4"
    # 使用 cmd 命令
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.STDOUT)
    print("录制开始")
    print(p)
    yield
    # 结束录制，生成视频
    print("结束录制，生成视频")
    os.kill(p.pid, signal.CTRL_C_EVENT)