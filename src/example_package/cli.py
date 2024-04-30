from dataclasses import dataclass
from . import salstat
import argparse


@dataclass
class ProgArguments():
    file: str
    year: list[int]


def parse_args() -> ProgArguments:
    parser = argparse.ArgumentParser(
        prog='salstat',
        description='Počítání rozdílů průměrné mzdy za 2 roky')

    parser.add_argument('--file', nargs="?", help='soubor', type=str)
    parser.add_argument('--year', nargs=2, help='roky', type=int)

    args = parser.parse_args()
    
    if not args.file and not args.year:
        parser.print_help()
        exit(1)

    return ProgArguments(**vars(args))


def main():
    args = parse_args()
    if args.year[0] == args.year[1]:
        print("Roky musí být různé")
        exit(1)

    if args.year[0] > args.year[1]:
        print(f"Roky se otočí {args.year[1]} -> {args.year[0]}")
        args.year[0], args.year[1] = args.year[1], args.year[0]
    year1 = salstat.count_average_salary(salstat.load_data_file(args.file, args.year[0]))
    year2 = salstat.count_average_salary(salstat.load_data_file(args.file, args.year[1]))
    print(f"Prumerna mzda se pro rok {args.year[0]} a {args.year[1]} změnila z {year1} na {year2} to je o {year2-year1} Kč")
