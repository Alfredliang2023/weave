# Weave Generator - 纺织组织生成器

一个功能强大的 Python 库，用于生成各种纺织组织结构。

## 支持的组织类型

- **斜纹** (Twill) - 基础斜纹组织
- **曲线斜纹** (Curved Twill) - 经向/纬向曲线斜纹
- **角度斜纹** (Angle Twill) - 带角度的斜纹组织
- **山形斜纹** (Waved Twill) - 山形斜纹组织
- **锯齿斜纹** (Zigzag Twill) - 锯齿斜纹组织
- **菱形斜纹** (Diamond Twill) - 菱形斜纹组织
- **缎纹** (Satin) - 经面/纬面缎纹
- **重平** (Rib Weave) - 经重平/纬重平
- **方平** (Basket Weave) - 方平组织

## 安装

```bash
pip install weave-generator
```

## 快速开始

### 基本使用

```python
from weave_generator import generate_weave

# 生成一个 3/5 的右斜纹
matrix = generate_weave(
    '斜纹',
    numerator=[3],
    denominator=[5],
    direction='右'
)

# 打印组织矩阵
for row in matrix:
    print(' '.join(map(str, row)))
```

### 命令行使用

```bash
# 生成斜纹组织
weave-gen --type 斜纹 --numerator 3 --denominator 5 --direction 右
```

## API 文档

### `generate_weave(weave_type, **params)`

生成指定的纺织组织。

**参数：**
- `weave_type` (str): 组织类型
- `**params`: 组织特定参数

**返回：**
- List[List[int]]: 组织矩阵 (1=经浮点, 0=纬浮点)

### 支持的参数

| 组织类型 | 必需参数 | 可选参数 |
|---------|---------|---------|
| 斜纹 | numerator, denominator, direction | - |
| 曲线斜纹 | numerator, denominator, direction, fly | - |
| 角度斜纹 | numerator, denominator, direction, fly | - |
| 山形斜纹 | numerator, denominator, k_value, direction | - |
| 锯齿斜纹 | numerator, denominator, k_value, s_value, direction | - |
| 菱形斜纹 | numerator, denominator, kj, kw | - |
| 缎纹 | size, fly, direction | - |
| 重平 | numerator, denominator, direction | - |
| 方平 | numerator, denominator | - |

## 使用示例

### 1. 斜纹

```python
matrix = generate_weave('斜纹', numerator=[3], denominator=[5], direction='右')
```

### 2. 曲线斜纹

```python
matrix = generate_weave(
    '曲线斜纹',
    numerator=[1, 2],
    denominator=[3, 4],
    direction='经',
    fly=[1, 1, 0, -1, -1]
)
```

### 3. 菱形斜纹

```python
matrix = generate_weave(
    '菱形斜纹',
    numerator=[3],
    denominator=[5],
    kj=4,
    kw=4
)
```

### 4. 缎纹

```python
matrix = generate_weave('缎纹', size=8, fly=3, direction='经面')
```

## 参数说明

- **numerator**: 组织分母列表（整数或列表）
- **denominator**: 组织分子列表（整数或列表）
- **direction**: 方向（"左"/"右", "经"/"纬", "经面"/"纬面"）
- **fly**: 飞数或移位数（整数或列表）
- **k_value**: 山形参数
- **s_value**: 锯齿参数
- **kj/kw**: 经/纬循环数
- **size**: 缎纹大小/枚数

## 许可证

MIT License
