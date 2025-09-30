import pandas as pd
import chinese_calendar as calendar
from datetime import date, timedelta

# --- 1. 定义数据的时间范围 ---
# 受chinesecalendar限制，时间范围只能从2004年开始
start_date = date(2004, 1, 1)
end_date = date(2025, 12, 31)

print(f"正在生成从 {start_date} 到 {end_date} 的工作日数据...")

# --- 2. 生成日期序列 ---
all_dates = []
current_date = start_date
while current_date <= end_date:
    all_dates.append(current_date)
    current_date += timedelta(days=1)

# --- 3. 判断每一天是否为工作日 ---
results = []
for dt in all_dates:
    # 使用"calendar" 来调用函数
    is_workday = calendar.is_workday(dt)
    on_holiday, holiday_name = calendar.get_holiday_detail(dt)

    results.append({
        'date': dt,
        'is_workday': 1 if is_workday else 0,
        'day_of_week': dt.weekday() + 1,
        # holiday_name 现在可能是 Holiday.xxx 的枚举类型，我们取它的值
        'holiday_name': holiday_name
    })

# --- 4. 转换为 Pandas DataFrame ---
df = pd.DataFrame(results)

print("\n数据生成完毕！")

# --- 5. 检查数据样本 ---
print("\n数据示例 (前5行):")
print(df.head())

# --- 6. 保存为CSV文件 ---
output_filename = f'china_workdays_{start_date.year}_{end_date.year}.csv'
df.to_csv(output_filename, index=False, encoding='utf-8-sig')

print(f"\n数据已成功保存到文件: {output_filename}")