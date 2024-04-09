def main():
    path = 'books/frankenstein.txt'
    with open(path) as f:
        file_contents = f.read()    
    #print(count_words(file_contents))
    #print(count_characters(file_contents))
    create_report(count_characters(file_contents), count_words(file_contents), path)

def count_words(text:str):
    words = text.split()
    return len(words)


def count_characters(text:str):
    cha_counts = dict()
    for c in text.lower():
        if c in cha_counts:
            cha_counts[c] += 1
        else:
            cha_counts[c] = 1
    return cha_counts


def create_report(cha_counts:dict, words:int, path):
    print(f'--- START REPORT of {path} ---')
    print(f'{words} words found in document\n\n')
    lst_cha_counts = [{'name':i, 'num':cha_counts[i]} for i in cha_counts.keys() if i.isalpha()]
    lst_cha_counts.sort(reverse=True, key=lambda lst_cha_counts:lst_cha_counts['num'])
    for c_pair in lst_cha_counts:
        print(f"The '{c_pair['name']}' character was found {c_pair['num']} times")
    print('--- END REPORT ---')
main()