# 体检自动化预约系统

## How it works
该程序会根据你提供的信息，登录系统并且在指定体检中心中循环，如果新的时间早于当前时间，会给你一个声音提醒。

## 运行之前

- 请确保你已经有初始预约

- 请确保 `automate.py` 里的这些信息准确无误
  - HAPI id
  - first name
  - last name
  - DOB

- 如果所属地区不是Sydney, 请修改以下信息
  - 想要预约的centers ids/names
  - 需要点弹窗才能继续预约的center(s)名称

- 安装dependencies
  `pip3 install -r requirements.txt`

## 运行代码

```
python3 automate.py
```

## 常见问题

1. 如果出现 `stale element reference: element is not attached to the page document` 报错，`ctrl+c`退出进程，并再次运行代码
2. 该bot暂时不考虑一些edge cases，本人精力有限，如有需要，请自行fork