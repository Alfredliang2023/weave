#!/usr/bin/env python3
"""
简化的组织生成器
不依赖numpy，只实现基础斜纹组织
"""

def Twill_weave_matrix(param1, param2, direction):
    """生成基础斜纹组织矩阵"""
    # 验证参数
    if not all(isinstance(x, int) and x > 0 for x in param1 + param2):
        raise ValueError("参数组必须包含正整数")
    
    # 计算矩阵大小
    rows = sum(param1) + sum(param2)
    cols = rows  # 行列数相同
    
    # 生成第一列
    first_col = []
    # 自下而上生成
    # 交替处理参数组1和参数组2的元素
    for i in range(max(len(param1), len(param2))):
        if i < len(param1) and param1[i] > 0:
            first_col = [1] * param1[i] + first_col
        if i < len(param2) and param2[i] > 0:
            first_col = [0] * param2[i] + first_col
    
    # 确保长度正确
    first_col = first_col[-rows:] if len(first_col) > rows else first_col
    
    # 根据方向生成矩阵
    matrix = []
    current_col = first_col.copy()
    
    for _ in range(cols):
        matrix.append(current_col.copy())
        if direction == "右":
            # 将最下面元素移到最上面
            current_col = current_col[1:] + [current_col[0]]
        elif direction == "左":
            # 将最上面元素移到最下面
            current_col = [current_col[-1]] + current_col[:-1]
    
    # 转置矩阵，使每行对应输出的一行
    matrix = list(zip(*matrix))
    
    return matrix

def Curved_twill_matrix(params1, params2, direction, fly):
    """生成曲线斜纹组织矩阵"""
    if len(params1) != len(params2):
        raise ValueError("params1 和 params2 的长度必须相同")

    if direction not in ['经', '纬']:
        raise ValueError("direction 必须是 '经' 或 '纬'")

    if not isinstance(fly, list) or len(fly) == 0:
        raise ValueError("fly 必须是非空列表")

    if direction == '经':
        # 经向：列移位（Sj）
        rows = sum(params1) + sum(params2)
        cols = len(fly)  # 列数等于 fly 长度

        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        # 生成第一列（从底部开始）
        current_row = rows - 1
        for i in range(len(params1)):
            # 填充1
            for _ in range(params1[i]):
                matrix[current_row][0] = 1
                current_row -= 1
            # 跳过0区域
            current_row -= params2[i]

        # 生成其他列
        for col in range(1, cols):
            prev_col = [matrix[r][col - 1] for r in range(rows)]
            shift = fly[col - 1]

            if shift > 0:
                top = prev_col[:shift]
                bottom = prev_col[shift:]
                new_col = bottom + top
            elif shift < 0:
                shift_abs = abs(shift)
                bottom = prev_col[-shift_abs:]
                top = prev_col[:-shift_abs]
                new_col = bottom + top
            else:
                new_col = prev_col

            for r in range(rows):
                matrix[r][col] = new_col[r]

    elif direction == '纬':
        # 纬向：行移位（Sw）
        cols = sum(params1) + sum(params2)
        rows = len(fly) + 1  # 行数等于 fly 长度 + 1

        matrix = []

        # 生成基准行（最后一行）
        base_row = [0] * cols
        current_col = 0
        for i in range(len(params1)):
            # 填充1
            for _ in range(params1[i]):
                base_row[current_col] = 1
                current_col += 1
            # 跳过0区域
            current_col += params2[i]
        matrix.append(base_row.copy())

        # 从下往上生成其他行
        current_base = base_row
        for i in range(len(fly) - 1):  # 不包含最后一个 fly
            new_row = [0] * cols
            shift = fly[i]

            for j in range(cols):
                shifted_pos = (j - shift) % cols
                new_row[j] = current_base[shifted_pos]

            matrix.insert(0, new_row)
            current_base = new_row

    return matrix

def Basket_weave_matrix(param1, param2):
    """生成重平组织矩阵"""
    def generate_column(param1, param2):
        """生成一个原始列，按 param1 和 param2 的节奏排列 1 和 0。"""
        col = []
        for p1, p2 in zip(param1, param2):
            col.extend([1] * p1)
            col.extend([0] * p2)
        return col

    def invert_column(col):
        """将原始列翻转（1变0，0变1）"""
        return [1 - c for c in col]

    def generate_columns(param1, param2):
        """按 param1 和 param2 定义的次数生成原始列和相反列"""
        original = generate_column(param1, param2)
        opposite = invert_column(original)
        col_block = []

        for p1, p2 in zip(param1, param2):
            col_block.extend([original] * p1)
            col_block.extend([opposite] * p2)
        return col_block

    # 步骤1：行数 = sum(param1) + sum(param2)
    num_rows = sum(param1) + sum(param2)

    # 步骤2-4：构造列块
    columns = generate_columns(param1, param2)

    # 按列转为矩阵（列转行），但顺序是自下而上
    matrix = []
    for i in range(num_rows):
        row = [col[-(i + 1)] for col in columns]  # 注意：负索引从末尾向前取
        matrix.append(row)

    return matrix

def Rib_weave_matrix(numerator, denominator, direction):
    """生成重平组织矩阵"""
    if len(numerator) != len(denominator):
        raise ValueError("分子和分母的数量必须相同")

    param_groups = list(zip(numerator, denominator))

    if direction == '经':
        # 计算行数（所有参数的和）
        total_rows = sum(sum(group) for group in param_groups)
        cols = 2
        matrix = [[0 for _ in range(cols)] for _ in range(total_rows)]

        # 生成第一列
        current_row = total_rows - 1  # 从底部开始

        # 处理每组参数
        for group in param_groups:
            # 放置1
            for _ in range(group[0]):
                matrix[current_row][0] = 1
                current_row -= 1
            # 放置0
            for _ in range(group[1]):
                matrix[current_row][0] = 0
                current_row -= 1

        # 生成第二列（反转第一列的值）
        for i in range(total_rows):
            matrix[i][1] = 1 - matrix[i][0]

    else:  # 纬面
        # 计算列数（所有参数的和）
        total_cols = sum(sum(group) for group in param_groups)
        rows = 2
        matrix = [[0 for _ in range(total_cols)] for _ in range(rows)]

        # 生成第一行
        current_col = 0

        # 处理每组参数
        for group in param_groups:
            # 放置0
            for _ in range(group[0]):
                matrix[0][current_col] = 0
                current_col += 1
            # 放置1
            for _ in range(group[1]):
                matrix[0][current_col] = 1
                current_col += 1

        # 生成第二行（反转第一行的值）
        for j in range(total_cols):
            matrix[1][j] = 1 - matrix[0][j]

    return matrix

