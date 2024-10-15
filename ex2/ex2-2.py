import pandas as pd
import numpy as np

# ویژگی‌های افراد: جنسیت، رنگ مو، قد، ملیت
attributes = [
    ['Male', 'Female'], 
    ['Black', 'Brown', 'Blonde'], 
    ['Tall', 'Medium', 'Short'], 
    ['US', 'French', 'German', 'Irish', 'Indian', 'Japanese', 'Portuguese']
]

# نمونه‌های مثبت و منفی
examples = [
    (['Male', 'Black', 'Tall', 'US'], 'Positive'),
    (['Female', 'Brown', 'Medium', 'French'], 'Negative'),
    (['Male', 'Blonde', 'Short', 'German'], 'Positive'),
    (['Female', 'Black', 'Tall', 'Japanese'], 'Negative')
]

# تابع برای به‌روزرسانی مرز خاص (S) با یک نمونه مثبت
def update_S(s, example):
    for i in range(len(s)):
        if s[i] == 'Φ':  # اگر در حالت خاص‌ترین باشد
            s[i] = example[i]
        elif s[i] != example[i]:  # اگر با نمونه مثبت مطابقت نداشته باشد
            s[i] = '?'
    return s

# تابع برای به‌روزرسانی مرز عمومی (G) با یک نمونه منفی
def update_G(g, example):
    new_G = []
    for hypothesis in g:
        consistent = True
        for i in range(len(hypothesis)):
            if hypothesis[i] != '?' and hypothesis[i] != example[i]:
                consistent = False
        if consistent:
            for i in range(len(hypothesis)):
                if hypothesis[i] == '?':
                    new_hypothesis = hypothesis.copy()
                    new_hypothesis[i] = example[i]
                    new_G.append(new_hypothesis)
    return new_G

# مرزهای اولیه S و G
S = ['Φ'] * len(attributes)
G = [['?'] * len(attributes)]

# پیاده‌سازی الگوریتم CANDIDATE-ELIMINATION
for example, label in examples:
    if label == 'Positive':
        S = update_S(S, example[0])
        G = [g for g in G if all(s == '?' or g[i] == '?' or s == g[i] for i, s in enumerate(S))]
    elif label == 'Negative':
        G = update_G(G, example[0])
        G = [g for g in G if not all(s == '?' or s == g[i] for i, s in enumerate(S))]

    print(f"S: {S}")
    print(f"G: {G}")
