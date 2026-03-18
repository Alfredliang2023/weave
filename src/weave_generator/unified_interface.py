#!/usr/bin/env python3
"""
织物组织生成器统一接口
解决各生成器函数参数不统一的问题，提供统一的调用方式
"""

from .Twill_weave_generator import Twill_weave_matrix
from .Curved_Twill_generator import Curved_twill_matrix
from .Angle_Twill_generator import Angle_weave_matrix
from .Waved_twill import Waved_twill_generate
from .Zigzag_twill import zigzag_twill
from .diamond_weave_generator import diamond_weave_generator
from .Basket_weave_generator import Basket_weave_matrix
from .Rib_weave_generator import Rib_weave_matrix
from .Satin_weave_generator import Stain_weave_matrix

import numpy as np
import sys


class WeaveGenerator:
    """织物组织统一生成器"""
    
    # 支持的组织类型及其参数规范
    WEAVE_TYPES = {
        '斜纹': {
            'params': ['numerator', 'denominator', 'direction'],
            'directions': ['左', '右'],
            'description': '基础斜纹、加强斜纹、复合斜纹'
        },
        '曲线斜纹': {
            'params': ['numerator', 'denominator', 'direction', 'fly'],
            'directions': ['经', '纬'],
            'description': '曲线斜纹，需要提供移位序列',
            'fly_type': 'list'  # 需要列表类型的飞数
        },
        '角度斜纹': {
            'params': ['numerator', 'denominator', 'direction', 'fly'],
            'directions': ['经', '纬'],
            'description': '角度斜纹，需要提供飞数值',
            'fly_type': 'int'  # 需要整数类型的飞数
        },
        '山形斜纹': {
            'params': ['numerator', 'denominator', 'direction', 'k_value'],
            'directions': ['Kj', 'Kw'],
            'description': '山形斜纹，需要提供K值'
        },
        '锯齿斜纹': {
            'params': ['numerator', 'denominator', 'direction', 'k_value', 's_value'],
            'directions': ['Kj', 'Kw'],
            'description': '锯齿斜纹，需要提供K值和S值'
        },
        '菱形斜纹': {
            'params': ['numerator', 'denominator', 'kj', 'kw'],
            'directions': None,
            'description': '菱形斜纹，需要提供Kj和Kw值'
        },
        '缎纹': {
            'params': ['size', 'fly', 'direction'],
            'directions': ['经面', '纬面'],
            'description': '缎纹组织，需要提供枚数和飞数'
        },
        '重平': {
            'params': ['numerator', 'denominator', 'direction'],
            'directions': ['经', '纬'],
            'description': '重平组织'
        },
        '方平': {
            'params': ['numerator', 'denominator'],
            'directions': None,
            'description': '方平组织'
        }
    }
    
    @classmethod
    def get_supported_types(cls):
        """获取所有支持的组织类型"""
        return list(cls.WEAVE_TYPES.keys())
    
    @classmethod
    def get_type_info(cls, weave_type):
        """获取特定组织类型的参数信息"""
        return cls.WEAVE_TYPES.get(weave_type)
    
    @classmethod
    def normalize_params(cls, weave_type, **params):
        """
        归一化参数，确保参数格式正确
        
        参数:
            weave_type: 组织类型
            **params: 参数字典
            
        返回:
            归一化后的参数字典
            
        异常:
            ValueError: 参数不合法时抛出
        """
        type_info = cls.WEAVE_TYPES.get(weave_type)
        if not type_info:
            raise ValueError(f"不支持的组织类型: {weave_type}")
        
        # 检查必需参数
        required_params = type_info['params']
        for param in required_params:
            if param not in params:
                raise ValueError(f"缺少必需参数: {param}")
        
        # 归一化 direction
        if 'direction' in required_params:
            direction = params['direction']
            valid_directions = type_info['directions']
            if direction not in valid_directions:
                raise ValueError(f"direction 必须是 {valid_directions} 之一，当前值: {direction}")
        
        # 归一化 numerator 和 denominator
        for key in ['numerator', 'denominator']:
            if key in params:
                value = params[key]
                if isinstance(value, int):
                    params[key] = [value]
                elif not isinstance(value, list):
                    raise ValueError(f"{key} 必须是整数或列表，当前类型: {type(value)}")
        
        # 归一化缎纹的特殊参数
        if weave_type == '缎纹':
            # 缎纹使用 size 和 fly 而不是 numerator/denominator
            if 'size' in params and isinstance(params['size'], list):
                params['size'] = params['size'][0] if params['size'] else 5
            if 'fly' in params and isinstance(params['fly'], list):
                params['fly'] = params['fly'][0] if params['fly'] else 2
        
        return params
    
    @classmethod
    def generate(cls, weave_type, **params):
        """
        统一的组织生成接口
        
        参数:
            weave_type: 组织类型，如 '斜纹', '曲线斜纹', '缎纹' 等
            **params: 根据组织类型需要的参数
            
        返回:
            组织矩阵（二维列表）
            
        异常:
            ValueError: 参数不合法或组织类型不支持
        """
        # 归一化参数
        params = cls.normalize_params(weave_type, **params)
        
        matrix = None
        
        try:
            if weave_type == '斜纹':
                matrix = Twill_weave_matrix(
                    params['numerator'],
                    params['denominator'],
                    params['direction']
                )
                
            elif weave_type == '曲线斜纹':
                matrix = Curved_twill_matrix(
                    params['numerator'],
                    params['denominator'],
                    params['direction'],
                    params['fly']
                )
                
            elif weave_type == '角度斜纹':
                matrix = Angle_weave_matrix(
                    params['numerator'],
                    params['denominator'],
                    params['direction'],
                    params['fly']
                )
                
            elif weave_type == '山形斜纹':
                matrix = Waved_twill_generate(
                    params['numerator'],
                    params['denominator'],
                    params['direction'],
                    params['k_value']
                )
                
            elif weave_type == '锯齿斜纹':
                matrix = zigzag_twill(
                    params['numerator'],
                    params['denominator'],
                    params['direction'],
                    params['k_value'],
                    params['s_value']
                )
                
            elif weave_type == '菱形斜纹':
                matrix = diamond_weave_generator(
                    params['numerator'],
                    params['denominator'],
                    params['kj'],
                    params['kw']
                )
                
            elif weave_type == '缎纹':
                matrix = Stain_weave_matrix(
                    params['size'],
                    params['fly'],
                    params['direction']
                )
                
            elif weave_type == '重平':
                matrix = Rib_weave_matrix(
                    params['numerator'],
                    params['denominator'],
                    params['direction']
                )
                
            elif weave_type == '方平':
                matrix = Basket_weave_matrix(
                    params['numerator'],
                    params['denominator']
                )
                
            else:
                raise ValueError(f"不支持的组织类型: {weave_type}")
            
            # 转换矩阵格式
            if matrix is not None:
                # 如果是 numpy 数组，转换为列表
                if hasattr(matrix, 'tolist'):
                    matrix = matrix.tolist()
                
                # 如果是元组的列表，转换为列表的列表
                if matrix and isinstance(matrix, list) and len(matrix) > 0:
                    if isinstance(matrix[0], tuple):
                        matrix = [list(row) for row in matrix]
                
                return matrix
            else:
                raise ValueError(f"生成 {weave_type} 组织失败")
                
        except Exception as e:
            raise ValueError(f"生成 {weave_type} 组织时发生错误: {str(e)}")


# 便捷函数
def generate_weave(weave_type, **params):
    """便捷的组织生成函数"""
    return WeaveGenerator.generate(weave_type, **params)


def get_weave_types():
    """获取所有支持的组织类型"""
    return WeaveGenerator.get_supported_types()


def get_type_description(weave_type):
    """获取组织类型的描述信息"""
    info = WeaveGenerator.get_type_info(weave_type)
    if info:
        return {
            'type': weave_type,
            'params': info['params'],
            'directions': info.get('directions'),
            'description': info.get('description')
        }
    return None


def main():
    """命令行入口函数"""
    import argparse

    parser = argparse.ArgumentParser(
        description='纺织组织生成器 - Weave Generator CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  weave-gen --type 斜纹 --numerator 3 --denominator 5 --direction 右
  weave-gen --type 缎纹 --size 8 --fly 3 --direction 经面
  weave-gen --list-types
        """
    )

    parser.add_argument('--type', '-t', help='组织类型')
    parser.add_argument('--list-types', action='store_true', help='列出所有支持的组织类型')
    parser.add_argument('--numerator', '-n', type=int, help='组织点上升数')
    parser.add_argument('--denominator', '-d', type=int, help='组织点下降数')
    parser.add_argument('--direction', help='方向 (左/右/经/纬/经面/纬面)')
    parser.add_argument('--size', type=int, help='缎纹大小')
    parser.add_argument('--fly', type=int, help='飞数')
    parser.add_argument('--k-value', type=int, help='K值')
    parser.add_argument('--s-value', type=int, help='S值')
    parser.add_argument('--kj', type=int, help='Kj (经循环数)')
    parser.add_argument('--kw', type=int, help='Kw (纬循环数)')
    parser.add_argument('--output', '-o', help='输出文件路径 (JSON格式)')

    args = parser.parse_args()

    # 列出所有类型
    if args.list_types:
        print("=" * 60)
        print("支持的组织类型:")
        print("=" * 60)
        for weave_type in get_weave_types():
            info = get_type_description(weave_type)
            print(f"\n{weave_type}: {info['description']}")
            print(f"  参数: {', '.join(info['params'])}")
            if info['directions']:
                print(f"  方向: {', '.join(info['directions'])}")
        return 0

    # 检查是否指定了类型
    if not args.type:
        parser.error("必须指定组织类型 (--type) 或使用 --list-types 查看所有类型")

    # 构建参数
    params = {}

    if args.numerator is not None:
        params['numerator'] = [args.numerator]
    if args.denominator is not None:
        params['denominator'] = [args.denominator]
    if args.direction:
        params['direction'] = args.direction
    if args.size is not None:
        params['size'] = args.size
    if args.fly is not None:
        params['fly'] = [args.fly]
    if args.k_value is not None:
        params['k_value'] = args.k_value
    if args.s_value is not None:
        params['s_value'] = args.s_value
    if args.kj is not None:
        params['kj'] = args.kj
    if args.kw is not None:
        params['kw'] = args.kw

    # 生成组织
    try:
        matrix = generate_weave(args.type, **params)

        # 打印矩阵
        print(f"\n{args.type} 组织矩阵:")
        print("=" * 60)
        for i, row in enumerate(matrix):
            row_str = ' '.join(str(cell) for cell in row)
            print(f"  {i:2d}: {row_str}")
        print("=" * 60)

        # 保存到文件
        if args.output:
            import json
            with open(args.output, 'w', encoding='utf-8') as f:
                json.dump({
                    'type': args.type,
                    'params': params,
                    'matrix': matrix
                }, f, indent=2, ensure_ascii=False)
            print(f"\n✓ 已保存到: {args.output}")

        return 0

    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        return 1


# 示例和测试代码
if __name__ == "__main__":
    sys.exit(main())
