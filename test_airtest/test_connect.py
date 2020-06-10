from airtest.core.api import auto_setup, connect_device, set_current, init_device


class Test_connect:

    #auto_setup 是一个用来 初始化环境 的接口，它接受5个参数:
    #我们可以设置当前脚本所在的路径、 指定运行脚本的设备 、设置默认的log路径、设置脚本父路径和指定截图精度：
    def test_auto_setup(self):
        # 连接本机默认端口连的一台设备号为SJE5T17B17的手机
        auto_setup(__file__, devices=["Android://127.0.0.1:5037/SJE5T17B17"])
        ## 连接本机默认端口连的设备号为123和456的两台手机
        auto_setup(__file__, devices=["Android://127.0.0.1:5037/123", "Android://127.0.0.1:5037/456"])

    def test_connect_device(self):
        # 连上第一台手机
        dev1 = connect_device("Android://127.0.0.1:5037/serialno1")
        # 连上第二台手机
        dev2 = connect_device("Android://127.0.0.1:5037/serialno2")

        # 切换当前操作的手机到序列号为serialno1的手机
        set_current("serialno1")

    def test_init_device(self):
        #init_device 接口只需要传入 设备平台和设备的uuid 即可，参数详情可以查看下图：
        init_device(platform="Android", uuid="SJE5T17B17")

    def test_setcurrent(self):
        pass