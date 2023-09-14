#!/usr/bin/python3
def worst_fit(memory_holes, request_size):
    available_holes = []

    for size in memory_holes:
        available_holes.append(size)

    worst_fit_index = -1
    worst_fit_size = -1

    for i, hole_size in enumerate(available_holes):
        if request_size <= hole_size and hole_size > worst_fit_size:
            worst_fit_size = hole_size
            worst_fit_index = i

    if worst_fit_index >= 0:
        # Phân bổ yêu cầu vào hole lớn nhất
        allocated_hole_size = available_holes[worst_fit_index]
        available_holes[worst_fit_index] -= request_size
        return allocated_hole_size
    else:
        return None

if __name__ == "__main__":

    memory_holes = [int(x) for x in input("Nhập danh sách kích thước hole ban đầu (KB), các số cách nhau bằng dấu cách: ").split()]

    request_sizes = input("Nhập kích thước yêu cầu (KB), các số cách nhau bằng dấu cách: ").split()

    for request_size_str in request_sizes:
        try:
            request_size = int(request_size_str)
        except ValueError:
            print(f"Kích thước yêu cầu '{request_size_str}' không hợp lệ. Bỏ qua...")
            continue

        allocated_hole_size = worst_fit(memory_holes, request_size)

        if allocated_hole_size is not None:
            print(f"Yêu cầu {request_size}KB được phân bổ vào hole kích thước {allocated_hole_size} KB.")
            memory_holes.remove(allocated_hole_size)  # Loại bỏ hole đã được phân bổ
        else:
            print(f"Không có hole phù hợp cho yêu cầu {request_size}KB.")

    print("Kết thúc phân bổ.")
