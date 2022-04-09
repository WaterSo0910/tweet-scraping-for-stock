import argparse

def parse_args():
    parser = argparse.ArgumentParser(prog='args_template.py', description='Twitter scrapying') 
    parser.add_argument('--search', '-s' , type=str, required=True, help='Which search string to scrapy')
    parser.add_argument('--year', '-y' , type=int, required=True, help='Which year to scrapy')
    parser.add_argument('--month', '-m' , type=int, required=True, help='Which month to scrapy')
    parser.add_argument('--max_nums', '-M', type=int, required=True, help='Max numbers to scrapy')

    return parser.parse_args()


def main():
    print(args)


if __name__ == '__main__':
    args = parse_args()
    main()