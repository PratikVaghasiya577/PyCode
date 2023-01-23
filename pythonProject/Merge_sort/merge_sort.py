import random


def split(list):
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]
    # print(f'{left}  {right}')
    return left, right


def merge(left, right):
    out = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            out.append(left[i])
            i += 1
        else:
            out.append(right[j])
            j += 1
    print(f'{left}   {right}')
    while i < len(left):
        out.append(left[i])
        i += 1
    while j < len(right):
        out.append(right[j])
        j += 1
    return out


class MergeSort:

    def merge_sort(self, list):
        if len(list) <= 1:
            return list
        left_half, right_half = split(list)
        left = self.merge_sort(left_half)
        right = self.merge_sort(right_half)

        return merge(left, right)


b = random.sample(range(1, 1000),100)
print(b)
a = MergeSort()
print(a.merge_sort(b))
