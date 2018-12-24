# coding=utf-8
class player_Page(object):
    Traffic_tips = "提示"
    Continue_play = "继续播放"
    Pause_play = "暂停播放"

    # 签到
    sign = "//XCUIElementTypeOther[@name=\"课前签到\"]/XCUIElementTypeOther[1]/XCUIElementTypeButton"
    Sign_before_class = "课前签到"

    # 单点互踢
    Single_point_kick = "账号已在别处登录，无法继续观看直播，请退出教室"
    out_classroom = "退出教室"
    out_classroom_p = "//XCUIElementTypeButton[@name=\"退出教室\"]"

    # 退出教室
    is_out_classroom = "确认要退出教室吗？"
    Leave_classroom = "live zhibo back icon"
    exit = "退出"
    cancel = "取消"

    # 聊天
    Only_see_teacher = "live video chat filtermsg"
    hot_word = "live video chat hotword"
    hot_word_list = ['11111', '懂啦～赞～', '666666', '老师棒棒哒', '谢谢老师～', '老师再见，么么哒～']
    type_word = "输入文字"
    have_content = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeButton"
    send = "发送"

    # 自带功能
    screenshots = "live zhibo cut icon"
    tag = "live zhibo mark icon"
    Select_label = "请选择标签"
    important = "很重要"
    not_understand = "我没懂"

    full_screen = "live_zhibo_fullscreen_icon"

    help = "live zhibo help icon"
    refresh = "刷新"
    recharge = "重新收取"

    more = "liveCourse video detail button"
    Civilization_convention = "文明公约"
    Eye_protection_mode = "护眼模式"

    HD = "高清"
    Standard = "标清"

    # 连麦   元素是由3个图片组成
    isMic = "ZYBLive-Homework-Resource.bundle/mic_back"
    isMicp = '//XCUIElementTypeImage[@name="ZYBLive-Homework-Resource.bundle/mic_back"]'

    Raise_hand_p = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]"
    I_know = "朕知道了"

    # 连麦状态公共图片
    micCommon = "ZYBLive-Homework-Resource.bundle/mic_back"
    minCommonP = '//XCUIElementTypeImage[@name="\ZYBLive-Homework-Resource.bundle/mic_back"]'

    # 举手状态其他2个图片
    jushou1 = "/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_circulation_13@2x"
    jushou1P = '//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_circulation_13@2x"]'
    jushou2 = "ZYBLive-Homework-Resource.bundle/live_mic_hand_up_did_word"
    jushou2P = '//XCUIElementTypeImage[@name="ZYBLive-Homework-Resource.bundle/live_mic_hand_up_did_word"]'

    # 已举手时其他2个图片
    yijushou1 = "/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_connect_72@2x"
    yijushou1P = '//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_connect_72@2x"]'
    yijushou2 = "/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_loadingwenzi_44@2x"
    yijushou2P = '//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_loadingwenzi_44@2x"]'

    # 上麦时其他2个元素    上麦2元素和已举手2元素相同，要用元素1去就课识别举手，已举手，上麦的状态
    shangmai1 = "/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_connect_success_95@2x"
    shangmai1P = '//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_connect_success_95@2x"]'
    shangmai2 = "/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_loadingwenzi_44@2x"
    shangmai2P = '//XCUIElementTypeImage[@name="/var/containers/Bundle/Application/98B18FD2-EDFC-4875-A092-3D96D7752114/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_loadingwenzi_44@2x"]'

    Hands_up = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]"
    Whether_or_not = '是否要“取消举手"'
    think_again = "我再想想"
    Cancel_hands = "取消举手"

    isJushou = "/var/containers/Bundle/Application/14460C96-30C3-4BE3-A69D-3C4899AD258E/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_connect_huatongdaochushi_116@2x"
    isYiushou = "/var/containers/Bundle/Application/14460C96-30C3-4BE3-A69D-3C4899AD258E/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_hand_up_wait_connect_72@2x"
    mic_phone = "/var/containers/Bundle/Application/14460C96-30C3-4BE3-A69D-3C4899AD258E/homework.app/ZYBLive-Homework-Resource.bundle/live_mic_connect_success_90@2x"

    # 选项卡
    isTabShow = "live option handle up"               # 选项卡展示或隐藏
    Choose_card = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    commit = "提交"

    # 是否卡
    isShiFou = "live_yescard_yes_bg"
    isShiFou_yes = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton[1"
    isShiFou_no = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeButton[2]"
