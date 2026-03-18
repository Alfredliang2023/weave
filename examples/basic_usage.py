"""
Weave Generator 基本使用示例
"""

from weave_generator import generate_weave

print("=" * 60)
print("Weave Generator - 基本使用示例")
print("=" * 60)

# 示例 1: 生成一个简单的 3/5 斜纹
print("\n示例 1: 3/5 右斜纹")
print("-" * 60)
matrix = generate_weave('斜纹', numerator=[3], denominator=[5], direction='右')
for i, row in enumerate(matrix):
    row_display = '●' if cell == 1 else '○' for cell in row
    print(f"{i:2d}: {' '.join(row_display)}")

# 示例 2: 生成一个 8 飞缎纹
print("\n示例 2: 8 飞经面缎纹")
print("-" * 60)
matrix = generate_weave('缎纹', size=8, fly=3, direction='经面')
for i, row in enumerate(matrix):
    row_display = '●' if cell == 1 else '○' for cell in row
    print(f"{i:2d}: {' '.join(row_display)}")

# 示例 3: 生成曲线斜纹
print("\n示例 3: 曲线斜纹")
print("-" * 60)
matrix = generate_weave(
    '曲线斜纹',
    numerator=[1, 2],
    denominator=[3, 4],
    direction='经',
    fly=[1, 1, 0, -1, -1]
)
for i, row in enumerate(matrix):
    row_display = '●' if cell == 1 else '○' for cell in row
    print(f"{i:2d}: {' '.join(row_display)}")

# 示例 4: 生成菱形斜纹
print("\n示例 4: 菱形斜纹")
print("-" * 60)
matrix = generate_weave(
    '菱形斜纹',
    numerator=[3],
    denominator=[5],
    kj=4,
    kw=4
)
for i, row in enumerate(matrix):
    row_display = '●' if cell == 1 else '○' for cell in row
    print(f"{i:2d}: {' '.join(row_display)}")

print("\n" + "=" * 60)
print("示例运行完成！")
print("=" * 60)
