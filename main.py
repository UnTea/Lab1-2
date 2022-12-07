from apriori_python import apriori
from efficient_apriori import apriori as eff_apriori
from fpgrowth_py import fpgrowth
from PyARMViz import PyARMViz
import timeit

transactions = [
    ['Масло', 'Хлеб', 'Сыр'],
    ['Соль', 'Масло', 'Хлеб'],
    ['Хлеб', 'Соль'],
    ['Кефир', 'Ряженка', 'Масло'],
    ['Масло', 'Хлеб', 'Сыр', 'Соль', 'Ряженка'],
    ['Ряженка', 'Кефир'],
    ['Кефир', 'Масло', 'Хлеб', 'Сыр'],
    ['Масло', 'Хлеб'],
    ['Сыр', 'Соль', 'Хлеб'],
    ['Хлеб', 'Масло', 'Сыр', 'Молоко', 'Ряженка'],
    ['Хлеб', 'Сыр'],
    ['Молоко', 'Хлеб', 'Сыр', 'Масло'],
    ['Соль', 'Масло'],
    ['Соль', 'Сыр', 'Хлеб'],
    ['Сыр', 'Масло', 'Хлеб'],
    ['Масло', 'Хлеб', 'Соль', 'Сыр'],
    ['Кефир', 'Хлеб', 'Молоко'],
    ['Масло', 'Хлеб', 'Кефир', 'Ряженка'],
    ['Молоко', 'Ряженка'],
    ['Масло', 'Соль', 'Сыр', 'Хлеб', 'Ряженка', 'Молоко'],
]

# stat = {}
#
# for transaction in transactions:
#     for item in transaction:
#         try:
#             stat[item] += 1
#         except KeyError:
#             stat[item] = 1
#
# sort_transactions = []
#
# for transaction in transactions:
#     sort_transaction = {}
#
#     for item in transaction:
#         sort_transaction[item] = stat[item]
#
#     sort_transactions.append(dict(sorted(sort_transaction.items(), key=lambda item: item[1], reverse=True)))
#
# for sort_transaction in sort_transactions:
#     print(sort_transaction)
#
# print('\nApriori: ', timeit.timeit('lambda: apriori(data, minSup=0.5, minConf=0.8)'))
# print('Efficient Apriori: ', timeit.timeit('lambda: eff_apriori(data, min_support=0.5, min_confidence=0.8)'))
# print('FPGrowth: ', timeit.timeit('lambda: fpgrowth(data, minSupRatio=0.5, minConf=0.8)'))

rules = apriori(transactions, minSup=0.5, minConf=0.8)[1]
print('\nApriori:')
for rule in rules:
    print(rule)

rules = eff_apriori(transactions, min_support=0.3, min_confidence=0.6)[1]
print('\nEfficient Apriori:')
rules_rhs = filter(lambda rule: len(rule.lhs) == 1 and len(rule.rhs) == 1, rules)
for rule in sorted(rules_rhs, key=lambda rule: rule.confidence):
    print(rule)

# PyARMViz.adjacency_graph_plotly(rules)
# PyARMViz.metadata_scatter_plot(rules)

rules = fpgrowth(transactions, minSupRatio=0.5, minConf=0.8)[1]
print('\nFPGrowth:')
for rule in rules:
    print(rule)
