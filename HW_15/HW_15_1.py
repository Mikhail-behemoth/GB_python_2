import argparse
from random import randint
import logging

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


FORMAT = "{levelname} - {asctime} - {funcName}: {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='check_triangle.log', level=logging.INFO, encoding="UTF-8")

logger = logging.getLogger(__name__)


def check_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        logger.info(f'Треугольник {a}/{b}/{b} существует')
        if a == b == c:
            logger.info(f'Треугольник {a}/{b}/{b} равносторонний')
        elif a == b or b == c or c == a:
            logger.info(f'Треугольник {a}/{b}/{b} равнобедренный')

        else:
            logger.info(f'Треугольник {a}/{b}/{b} разносторонний')
    else:
        logger.error(f'Треугольника {a}/{b}/{b} не существует')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка треугольника")
    parser.add_argument("param", metavar="a b c", type=int, nargs=3, help="Введите a b c через пробел")
    args = parser.parse_args()
    check_triangle(*args.param)