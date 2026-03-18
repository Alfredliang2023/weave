"""
快速测试脚本 - 验证包是否可以正常导入和使用
"""

import sys
import os

# 添加 src 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from weave_generator import generate_weave, get_weave_types

print("=" * 60)
print("Weave Generator 包测试")
print("=" * 60)

# 测试 1: 列出所有支持的组织类型
print("\n[OK] 测试 1: 获取支持的组织类型")
types = get_weave_types()
print(f"  支持 {len(types)} 种组织类型:")
for t in types:
    print(f"    - {t}")

# 测试 2: 生成斜纹
print("\n[OK] 测试 2: 生成斜纹组织")
try:
    matrix = generate_weave('斜纹', numerator=[3], denominator=[5], direction='右')
    print(f"  成功生成 {len(matrix)}x{len(matrix[0])} 矩阵")
    print("  前 3 行:")
    for i in range(min(3, len(matrix))):
        print(f"    {matrix[i]}")
except Exception as e:
    print(f"  [FAIL] 失败: {e}")

# 测试 3: 生成缎纹
print("\n[OK] 测试 3: 生成缎纹组织")
try:
    matrix = generate_weave('缎纹', size=8, fly=3, direction='经面')
    print(f"  成功生成 {len(matrix)}x{len(matrix[0])} 矩阵")
    print("  前 3 行:")
    for i in range(min(3, len(matrix))):
        print(f"    {matrix[i]}")
except Exception as e:
    print(f"  [FAIL] 失败: {e}")

# 测试 4: 生成菱形斜纹
print("\n[OK] 测试 4: 生成菱形斜纹")
try:
    matrix = generate_weave('菱形斜纹', numerator=[3], denominator=[5], kj=4, kw=4)
    print(f"  成功生成 {len(matrix)}x{len(matrix[0])} 矩阵")
    print("  前 3 行:")
    for i in range(min(3, len(matrix))):
        print(f"    {matrix[i]}")
except Exception as e:
    print(f"  [FAIL] 失败: {e}")

print("\n" + "=" * 60)
print("所有测试完成！")
print("=" * 60)
