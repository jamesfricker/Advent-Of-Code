with open("input.txt") as f:
    lines = f.read().splitlines()


numbers = list(map(int, lines[0].split(",")))

lines = lines[2:]
lines = [x for x in lines if x != ""]


def check_mate(list_of_lists):
    for row in range(len(list_of_lists[0])):
        check_rows = True if all(val == -1 for val in list_of_lists[row]) else False
        if check_rows == True:
            return check_rows
    for col in range(len(list_of_lists)):
        check_cols = True if all(val[col] == -1 for val in list_of_lists) else False
        if check_cols == True:
            return check_cols


all_matrix = []
for i in range(0, len(lines), 5):
    # print(lines[i : i + 5])
    rows = " ".join(lines[i : i + 5])
    rows_int = list(map(int, rows.split()))
    list1 = [rows_int[i] for i in range(0, 5)]
    list2 = [rows_int[i] for i in range(5, 10)]
    list3 = [rows_int[i] for i in range(10, 15)]
    list4 = [rows_int[i] for i in range(15, 20)]
    list5 = [rows_int[i] for i in range(20, 25)]
    all_rows = [list1, list2, list3, list4, list5]
    all_matrix.append(all_rows)


def find_p1_solution(numbers, all_matrix):
    for num in numbers:
        for index, matrix in enumerate(all_matrix):
            new_matrix = list(
                map(
                    lambda sublist: list(
                        map(lambda val: -1 if val == num else val, sublist)
                    ),
                    matrix,
                )
            )
            all_matrix[index] = new_matrix
            if check_mate(new_matrix):
                flat_list = [val for sublist in new_matrix for val in sublist]
                result = sum(val for val in flat_list if val != -1)
                return result * num


p = find_p1_solution(numbers, all_matrix)
print(p)


def find_p2_solution(numbers, all_matrix):
    for num in numbers:
        for index, matrix in enumerate(all_matrix):
            if matrix == 0:
                continue
            new_matrix = list(
                map(
                    lambda sublist: list(
                        map(lambda val: -1 if val == num else val, sublist)
                    ),
                    matrix,
                )
            )
            all_matrix[index] = new_matrix
            if check_mate(new_matrix):
                if (
                    sum([1 if val == 0 else 0 for val in all_matrix])
                    == len(all_matrix) - 1
                ):
                    flat_list = [val for sublist in new_matrix for val in sublist]
                    result = sum(val for val in flat_list if val != -1)
                    return result * num
                all_matrix[index] = 0


p = find_p2_solution(numbers, all_matrix)
print(p)
