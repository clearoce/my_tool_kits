# pip install matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default='input')
parser.add_argument('-n', '--name', default='now')
args = parser.parse_args()

# 从文件中读取矩形坐标
with open(f'{args.input}.txt', 'r') as f:
    n = int(f.readline().strip())
    rects = []
    for i in range(n):
        x1, y1, x2, y2 = map(int, f.readline().split())
        rects.append((x1, y1, x2 - x1, y2 - y1))

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 使用不同颜色绘制每个矩形
for i, rect in enumerate(rects):
    color = plt.cm.viridis(i / n)  # 使用viridis颜色映射
    rect_patch = patches.Rectangle(rect[:2], rect[2], rect[3], edgecolor='black', linewidth=1, facecolor=color)
    ax.add_patch(rect_patch)
    ax.text(rect[0] + rect[2] / 2, rect[1] + rect[3] / 2, str(i + 1), ha='center', va='center', color='red')

plt.xlim(0, 1920)
plt.ylim(1080, 0)

fig.set_size_inches(20, 12)
fig.set_dpi(100)
plt.savefig(f'{args.name}.png')
