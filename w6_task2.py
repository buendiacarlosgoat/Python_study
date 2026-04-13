import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig = plt.figure(figsize=(18, 14))
plt.suptitle("Matplotlib 进阶综合展示", fontsize=24, fontweight='bold')

# --- 子图 1: 多折线图 ---
ax1 = plt.subplot(2, 2, 1)

x1 = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [3, 4, 6, 9, 13]

# 绘制两条折线，设置不同的颜色、线型、标记
ax1.plot(x1, y1, color='tab:blue', linestyle='-', marker='o', label='序列 1 (质数趋势)')
ax1.plot(x1, y2, color='tab:orange', linestyle='--', marker='s', label='序列 2 (增长趋势)')

ax1.set_title("多折线图趋势对比")
ax1.set_xlabel("时间")
ax1.set_ylabel("数值")
ax1.legend() # 显示图例
ax1.grid(True, linestyle=':', alpha=0.6)

# --- 子图 2: 堆叠柱状图 ---
ax2 = plt.subplot(2, 2, 2)

categories = ['A', 'B', 'C']
values1 = [10, 20, 30]
values2 = [5, 15, 25]

# 绘制底部柱子
bars1 = ax2.bar(categories, values1, label='部分 1', color='skyblue', width=0.6)
# 绘制顶部柱子，bottom 参数是关键，表示从 values1 的顶端开始堆叠
bars2 = ax2.bar(categories, values2, label='部分 2', bottom=values1, color='salmon', width=0.6)

ax2.set_title("堆叠柱状图 (含数据标签)")
ax2.set_xlabel("类别")
ax2.set_ylabel("总量")
ax2.legend()

# 添加数据标签 (显示数值和百分比)
for bar1, bar2 in zip(bars1, bars2):
    # 底部标签
    ax2.text(bar1.get_x() + bar1.get_width()/2, bar1.get_height()/2,
             f'{bar1.get_height()}', ha='center', va='center', color='white', fontsize=10)
    # 顶部标签
    total_val = bar1.get_height() + bar2.get_height()
    ax2.text(bar2.get_x() + bar2.get_width()/2, bar1.get_height() + bar2.get_height()/2,
             f'{bar2.get_height()}', ha='center', va='center', color='white', fontsize=10)
    # 也可以显示总和
    ax2.text(bar1.get_x() + bar1.get_width()/2, total_val + 1,
             f'Total: {total_val}', ha='center', va='bottom', fontsize=9, fontweight='bold')


# --- 子图 3: 环形图 ---
ax3 = plt.subplot(2, 2, 3)

labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
explode = (0, 0.1, 0, 0) # 突出显示 B

# 绘制饼图
wedges, texts, autotexts = ax3.pie(sizes, explode=explode, labels=labels, colors=colors,
                                   autopct='%1.1f%%', shadow=True, startangle=140,
                                   textprops={'fontsize': 12})

# 绘制中心白色圆圈，形成环形图效果
centre_circle = plt.Circle((0,0), 0.70, fc='white', linewidth=1.5)
ax3.add_artist(centre_circle)

# 美化字体
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax3.set_title("环形图 (甜甜圈图)")
ax3.legend(title="类别图例", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))


# --- 子图 4: 3D 曲面图 ---
ax4 = plt.subplot(2, 2, 4, projection='3d')

# 生成网格数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
# 计算 Z 值 (例如：sin(sqrt(x^2 + y^2)))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# 绘制曲面
# cmap='viridis' 设置颜色映射
# edgecolor='none' 去除网格线，使表面更平滑
surf = ax4.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)

ax4.set_title("3D 曲面图示例")
ax4.set_xlabel("X 轴")
ax4.set_ylabel("Y 轴")
ax4.set_zlabel("Z 轴")

# 添加颜色条
fig.colorbar(surf, ax=ax4, shrink=0.5, aspect=5)


# ==========================================
# 保存与显示
# ==========================================
# 调整子图间距，防止标题重叠
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('advanced_charts.png', dpi=300) # 保存高清图
plt.show()

print("✅ 进阶综合图表已生成并保存为 advanced_charts.png")