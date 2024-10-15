import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# نمونه‌های مثبت و منفی فرضی
positive_examples = [(3, 4), (4, 6), (5, 7)]
negative_examples = [(1, 2), (7, 8)]

# تابع برای تعیین مرز خاص S
def get_S_boundary(pos_examples):
    x_min = min([p[0] for p in pos_examples])
    x_max = max([p[0] for p in pos_examples])
    y_min = min([p[1] for p in pos_examples])
    y_max = max([p[1] for p in pos_examples])
    return [(x_min, x_max, y_min, y_max)]

# تابع برای تعیین مرز عمومی G
def get_G_boundary(neg_examples):
    x_min = min([n[0] for n in neg_examples]) - 1  # گسترش فرضیه عمومی برای پوشش منفی‌ها
    x_max = max([n[0] for n in neg_examples]) + 1
    y_min = min([n[1] for n in neg_examples]) - 1
    y_max = max([n[1] for n in neg_examples]) + 1
    return [(x_min, x_max, y_min, y_max)]

# محاسبه مرزهای S و G
S_boundary = get_S_boundary(positive_examples)
G_boundary = get_G_boundary(negative_examples)

# رسم مستطیل‌ها بر اساس مرزهای S و G
def draw_rectangles(boundaries, color, label):
    for boundary in boundaries:
        x_min, x_max, y_min, y_max = boundary
        plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], color=color, label=label)
        label = ""  # برای نمایش فقط یک برچسب

# تنظیمات نمودار
plt.figure(figsize=(8, 8))
plt.title("S and G Boundary Rectangles")
plt.xlabel("x")
plt.ylabel("y")

# رسم مرز S با رنگ آبی
draw_rectangles(S_boundary, 'blue', 'S boundary')

# رسم مرز G با رنگ قرمز
draw_rectangles(G_boundary, 'red', 'G boundary')

# افزودن راهنما
plt.legend()

# نمایش نمودار
plt.grid(True)
plt.show()

# پیشنهاد یک نمونه جدید برای کاهش فضای نسخه‌ها
def suggest_query(S_boundary, G_boundary):
    # گرفتن مرکز بین مرزهای S و G برای پیشنهاد یک نقطه
    x_suggest = (S_boundary[0][0] + G_boundary[0][1]) // 2
    y_suggest = (S_boundary[0][2] + G_boundary[0][3]) // 2
    return (x_suggest, y_suggest)

# پیشنهاد یک نمونه جدید
query = suggest_query(S_boundary, G_boundary)
print(f"suggest: {query}")
