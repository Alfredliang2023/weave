def Angle_weave_matrix(numerator, denominator, direction, fly):
    """
    生角度组织矩阵（支持经向/纬向角度织法）

    参数:
        numerator (list): 分子列表，如 [1, 2]
        denominator (list): 分母列表，如 [3, 4]
        direction (str): 方向，'经' 或 '纬'
        fly (int): 移位步长值（正负代表方向）

    返回:
        list: 二维矩阵
    """
    # 检查分子和分母长度是否一致
    if len(numerator) != len(denominator):
        raise ValueError("分子和分母的数量必须相同")

    # 最大公约数函数（内部使用）
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    total_sum = sum(numerator) + sum(denominator)

    if direction == '经':
        rows = total_sum
        cols = rows // gcd(rows, abs(fly))

        # 生成第一列（从底部开始）
        first_column = []
        for i in range(len(numerator)):
            first_column.extend([1] * numerator[i])
            first_column.extend([0] * denominator[i])
        first_column.reverse()

        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        # 填充第一列
        for i in range(rows):
            matrix[i][0] = first_column[i]

        # 生成其他列
        shift_value = abs(fly)
        dir_flag = 1 if fly < 0 else -1

        for j in range(1, cols):
            for i in range(rows):
                source_row = (i - j * shift_value * dir_flag) % rows
                matrix[i][j] = first_column[source_row]

    elif direction == '纬':
        cols = total_sum
        rows = cols // gcd(cols, abs(fly))

        # 生成最后一行
        last_row = []
        for i in range(len(numerator)):
            last_row.extend([1] * numerator[i])
            last_row.extend([0] * denominator[i])

        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        # 填充最后一行
        for j in range(cols):
            matrix[rows - 1][j] = last_row[j]

        # 生成其他行
        shift_value = abs(fly)
        dir_flag = -1 if fly < 0 else 1

        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                steps = (rows - 1 - i)
                source_col = (j - steps * shift_value * dir_flag) % cols
                matrix[i][j] = last_row[source_col]

    else:
        raise ValueError("direction 必须是 '经' 或 '纬'")

    return matrix