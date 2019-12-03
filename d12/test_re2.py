import re

def main():
    poem = "this, is. a， poem。"
    sentence_list = re.split(r'[,.，。]', poem)
    print(sentence_list)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == "__main__":
    main()
