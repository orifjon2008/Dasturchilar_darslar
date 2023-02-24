# l = [500, 800, 15, 4156, 15, 456, 156, 782, 7000]
# natija = 0

## 1 - vazifa
## Listning ichidagi hamma elementlarni bir biriga qo'shib chiqoring
# for i in l:
#     natija += i
# print(natija)

## Sum, min, max buint-in funtions
# ---------------------
# print(sum(l)) #
# print(max(l)) #
# print(min(l)) #
# -----------------------

## 2 - vaziyfa
## list ichidagi tog' sonlarni bir biriga qo'shib chiqoring
# l = [500, 800, 15, 4156, 15, 456, 156, 782, 70001, 5, 853, 1, 57]
# natija = 0
# for i in l:
#     if i % 2 == 1:
#         natija += i
# print(natija)


## 3 - vaziyfa
## list ichidagi 3 xonalik sonlarni bir biriga qo'shib chiqoring
#
# l = [500, 800, 15, 4156, 15, 456, 156, 782, 70001, 5, 853, 1, 57]
# natija = 0
# for item in l:
#     if item in range(100, 999):
#         natija += item
# print(natija)
#
# l = [500, 800, 15, 4156, 15, 456, 156, 782, 70001, 5, 853, 1, 57]
# natija = 0
# for i in l:
#     if i >= 100 or i <= 999:
#         natija += i
# print(natija)


# 4 - chi vaziyfa
# # minimum va maximum elementlarni chiqoring
l = [500, 800, 15, 4156, 15, 456, 156, 782, 70001, 5, 853, 1, 57]
yangi_list = []
for i in l:
    if i in range(min(l), max(l)):
        yangi_list.append()
print(yangi_list)