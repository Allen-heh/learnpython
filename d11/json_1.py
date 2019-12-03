import json

def main():
    mydict = {
        'name': 'heh',
        'age': 16,
        'friends': ['allen', 'hey'],
        'cars': [
            {'test1': 1},
            {'test2': 2},
            {'test3': 3}
        ]

    }

    try:
        with open('data.json', 'w', encoding='utf-8') as f1:
            json.dump(mydict, f1)
    except IOError as e:
        print(e)
        print('io error')
    print('ok!')

if __name__ == "__main__":
    main()
