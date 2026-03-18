def Curved_twill_matrix(params1, params2, direction, fly):
    """
    曲线斜纹组织矩阵

    参数:
        params1 (list): 第一组参数列表（分子），如 [1, 2]
        params2 (list): 第二组参数列表（分母），如 [3, 4]
        direction (str): 方向，'经' 或 '纬'
        fly (list): 移位参数列表，如 [1, 1, 0, -1, -1]（经向）或 [-1, -2, -2, -1, 0]（纬向）

    返回:
        list: 二维矩阵
    """
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