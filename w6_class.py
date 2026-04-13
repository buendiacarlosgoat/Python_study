import matplotlib.pyplot as plt
import numpy as np

#1
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10,6))
x=[1,2,3]
y=[1,2,3]
plt.plot(x,y,marker='o',linestyle='-',color='b',label='数据序列')
plt.title("折线图示例")
plt.xlabel("时间")
plt.ylabel("值")
plt.legend()
plt.grid(True)
plt.show()

#2
plt.figure(figsize=(10, 6))

categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]
colors = ['red', 'blue', 'green', 'purple']
# 绘制柱状图
# width 设置柱子宽度，默认0.8
bars = plt.bar(categories, values, color=colors, width=0.6, edgecolor='black')

plt.title("各类别数据对比")
plt.xlabel("类别")
plt.ylabel("数值")
# 添加数据标签 (在柱子上方显示具体数值)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

plt.savefig('bar_chart.png')
plt.show()
print("✅ 柱状图已保存为 bar_chart.png")


# (3) 绘制散点图
# ==========================================
plt.figure(figsize=(10, 6))

# 生成随机数据 (100个点)
np.random.seed(42) # 设置随机种子以保证结果可复现
x_random = np.random.rand(100) * 100
# 制造一些相关性：y 随 x 增加而增加，并加入一些噪声
y_random = x_random * 0.8 + np.random.randn(100) * 10 + 20

# 绘制散点
# c:颜色, s:大小, alpha:透明度, marker:形状
plt.scatter(x_random, y_random, c='skyblue', s=50, alpha=0.6, edgecolors='w', marker='o', label='观测点')

# 计算并绘制趋势线 (线性回归)
# polyfit 返回多项式拟合的系数，1 表示一次多项式 (直线)
z = np.polyfit(x_random, y_random, 1)
p = np.poly1d(z)

# 绘制红色的回归线
plt.plot(x_random, p(x_random), "r--", linewidth=2, label=f'趋势线: y={z[0]:.2f}x+{z[1]:.2f}')

plt.title("变量相关性散点图")
plt.xlabel("变量 X")
plt.ylabel("变量 Y")
plt.legend()

plt.savefig('scatter_chart.png')
plt.show()
print("✅ 散点图已保存为 scatter_chart.png")


# ==========================================
# (4) 绘制饼图
# ==========================================
plt.figure(figsize=(8, 8))

labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
# 自定义颜色
colors_pie = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
# 突出显示某一块 (例如突出显示最大的 C 块，0.1 表示突出的距离)
explode = (0, 0, 0.1, 0)

plt.pie(sizes,
        explode=explode,
        labels=labels,
        colors=colors_pie,
        autopct='%1.1f%%', # 显示百分比格式
        shadow=True,       # 添加阴影
        startangle=140,    # 起始角度
        textprops={'fontsize': 12}) # 字体大小

plt.title("各类别数据占比")
plt.axis('equal')  # 保证饼图是正圆

plt.savefig('pie_chart.png')
plt.show()
print("✅ 饼图已保存为 pie_chart.png")

import matplotlib.pyplot as plt
import numpy as np

# 1. 准备数据
np.random.seed(42)
x = np.random.rand(50) * 100  # 广告投入
y = x * 0.8 + np.random.randn(50) * 10 + 20 # 销售额
size = np.random.rand(50) * 500 + 50 # 利润 (映射为大小)
color_val = np.random.rand(50) # 满意度 (映射为颜色)

# 2. 设置画布
plt.figure(figsize=(10, 6))

# 3. 绘制进阶散点图
# c=color_val 表示颜色根据满意度数值变化
# cmap='coolwarm' 表示使用冷暖色系（蓝-白-红）
# alpha=0.6 增加透明度，看清重叠点
# edgecolors='black' 给点加上黑边，轮廓更清晰
scatter = plt.scatter(x, y,
                      s=size,
                      c=color_val,
                      cmap='coolwarm',
                      alpha=0.6,
                      edgecolors='black',
                      linewidth=1)

# 4. 添加颜色条 (Colorbar)
# 这是一个图例，告诉读者颜色代表什么
plt.colorbar(scatter, label='客户满意度')

# 5. 添加标签和标题
plt.title('多维度散点图：广告投入与销售额', fontsize=16)
plt.xlabel('广告投入 (万元)', fontsize=12)
plt.ylabel('销售额 (万元)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.show()