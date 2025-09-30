中国工作日数据生成器 (China Workday Generator)

##简介

这是一个 Python 脚本，用于生成指定年份范围内每一天是否为中国法定工作日的数据。它能够准确处理法定节假日和因调休而产生的周末工作日。

## 功能

- 生成包含日期、是否工作日、星期几、节假日名称的数据。
- 支持自定义年份范围。
- 输出为 CSV 格式文件，方便在其他数据分析软件中使用。

## 如何使用

1.  确保已安装 Python 和 `pandas`, `chinesecalendar` 库。
    ```bash
    pip install pandas chinesecalendar
    ```
2.  修改脚本中的 `start_date` 和 `end_date` 变量来定义你需要的日期范围。
3.  运行 Python 脚本。
    ```bash
    python workday_checker.py
    ```
4.  脚本将在同目录下生成一个 `china_workdays_xxxx_xxxx.csv` 文件。

##注意
1.由于使用的是chinesecalendar库，而该库支持的时间范围是2004-至今，所以无法获得2004年之前的数据。
