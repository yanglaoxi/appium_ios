# coding=utf-8
class page_yike(object):
    take_lesson = "上课"
    Close_Windows = "ATHome Guide AlertCloseButton"
    enter_classroom = "进入教室"
    grade = "lc_lcContainer_gradeArrow"

    yike_back = "nav bar back white"

    # 首次启动作业帮时弹窗
    # 发送通知 = "//XCUIElementTypeAlert[@name="“作业帮”想给您发送通知"]"
    # 使用位置 = "//XCUIElementTypeAlert[@name="允许“作业帮”在您使用该应用时访问您的位置吗？"]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]"
    # 处理权限弹窗
    not_allow = "不允许"
    allow = "允许"

    # 首次启动app 的引导页面，第一个
    Photo_hands = "ask_home_guide_handle"
    Photo_hands_iPhone5s = "ask_home_guide_handle_5s"     # 适配5s的元素
    Photo_text = "ask_home_guide_Camera"

    # 第2个 百宝箱
    Photo_2_guide = "ask_home_guide_BaiBaoXiang"
    # 第三个  下拉刷新
    Photo_3_guide = "ask_home_guide_refreshDown"

    # 未知东东
    Photo_unknow = "ask_home_guide_decorate"
    # tab
    yike = "一课"
    one_to_one = "1对1"
    middle_button = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeTabBar/XCUIElementTypeButton[3]"
    found = "发现"
    my = "我"
    my_unLogin = "未登录"

    # 没有登录时 打开首次有
    Welcome_to_homework = "欢迎来到作业帮"

    # 首次打开即登录
    skip = "跳过"
    please_enter_cell_number_p = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField"
    next_step = "下一步"
    Keyboard_switch = "more"
    enter_password_p = "//XCUIElementTypeApplication[@name=\"作业帮\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField"
    Login = "登录"


    精选 = "精选"
    语文 = "语文"
    数学 = "数学"
    英语 = "英语"
    物理 = "物理"
    化学 = "化学"
    生物 = "生物"
    政治 = "政治"
    历史 = "历史"
    地理 = "地理"
    讲座 = "讲座"

    长期班 = "长期班"
    专题课 = "专题课"
    精品课 = "精品课"
    老师说 = "老师说"

    状态 = "状态"
    全部 = "全部"
    已完结p = "//XCUIElementTypeButton[@name=\"已完结\"]"
    未完结 = "未完结"
    未完结p = "//XCUIElementTypeButton[@name=\"未完结\"]"

    学科 = "学科"
    学科p = "//XCUIElementTypeStaticText[@name=\"学科\"]"
    兴趣课 = "//XCUIElementTypeButton[@name=\"兴趣课\"]"
    语文 = "//XCUIElementTypeButton[@name=\"语文\"]"
    物理 = "//XCUIElementTypeButton[@name=\"物理\"]"
    英语 = "//XCUIElementTypeButton[@name=\"英语\"]"
    数学 = "//XCUIElementTypeButton[@name=\"数学\"]"
    化学 = "//XCUIElementTypeButton[@name=\"化学\"]"
    讲座 = "//XCUIElementTypeButton[@name=\"讲座\"]"
    思想品德 = "//XCUIElementTypeButton[@name=\"思想品德\"]"

    类型 = "类型"
    类型p = "//XCUIElementTypeStaticText[@name=\"类型\"]"
    专题课 = "专题课"
    专题课p = "//XCUIElementTypeButton[@name=\"专题课\"]"
    长期班 = "//XCUIElementTypeButton[@name=\"长期班\"]"

    enter_classroom_detail = "进入教室(正在上课)"
    Pause_live = "lc_class_haverest"
    Pause_live_p = "//XCUIElementTypeImage[@name=\"lc_class_haverest\"]"


