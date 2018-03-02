import re

if __name__ == "__main__":
    # f = open('./regex_sum_75940.txt')
    # a = f.read()
    # f.close()
    # num_list = re.findall(r"[0-9]+", a)
    # total = 0
    # for i in num_list:
    #     total += int(i)
    #print(total)
    print(sum([int(i) for i in re.findall(r"[0-9]+",open('./regex_sum_75940.txt').read())]))
