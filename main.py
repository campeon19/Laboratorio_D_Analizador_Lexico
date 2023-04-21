from YALex_reader3 import Yalex_reader
from direct_afd1 import regex_to_afd, simular_afd2


def main():
    archivo_yalex = 'slr-2.yal'
    rule_token, token_dic = Yalex_reader(archivo_yalex)
    print(token_dic)
    # print(rule_token[4].val, rule_token[4].is_operator)
    # print(rule_token)
    # print val of every simbol in the rule_token
    # r = ''
    # for i in rule_token:
    #     r += i.val
    # print(r)
    afd = regex_to_afd(rule_token, token_dic)
    with open('validacion.txt', 'r') as f:
        validacion = f.read()
    simular_afd2(afd, validacion)


if __name__ == '__main__':
    main()
