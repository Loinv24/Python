import json
from google.colab import files
import csv
import matplotlib.pyplot as plt
from collections import Counter

# Hàm đọc file CSV
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề
        data = []
        for row in reader:
            data.append(row)
    return data

# Hàm đọc file JSON
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON file: {e}")
        print(f"Please check the file for syntax errors, especially around line {e.lineno}, column {e.colno}.")
        return None

# Chức năng 1: Thống kê số lượng anh trai theo nghề nghiệp
def anh_trai_job(filename):
    data = read_csv(filename)
    jobs = [row[2] for row in data]  # Giả sử cột nghề nghiệp là cột thứ 3
    job_count = Counter(jobs)

    # Vẽ biểu đồ quạt
    plt.figure(figsize=(8, 6))
    plt.pie(job_count.values(), labels=job_count.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Thống kê số lượng anh trai theo nghề nghiệp')
    plt.show()

# Chức năng 2: Thống kê số lượng anh trai theo năm sinh
def anh_trai_dob(filename):
    data = read_csv(filename)
    years_of_birth = [row[1] for row in data]  # Giả sử cột năm sinh là cột thứ 2
    year_count = Counter(years_of_birth)

    # Vẽ biểu đồ cột
    plt.figure(figsize=(10, 6))
    plt.bar(year_count.keys(), year_count.values(), color='skyblue')
    plt.xlabel('Năm sinh')
    plt.ylabel('Số lượng')
    plt.title('Thống kê số lượng anh trai theo năm sinh')
    plt.xticks(rotation=45)
    plt.show()

# Chức năng 3: Hiển thị danh sách các anh trai sinh năm 1997
def anh_trai_sinh_1997(filename):
    data = read_csv(filename)
    result = [row for row in data if row[1] == '1997']  # Giả sử cột năm sinh là cột thứ 2
    print("Danh sách các anh trai sinh năm 1997:")
    for row in result:
        print(row)

# Chức năng 4: Tính điểm trung bình của 'Đức Phúc' và tìm anh trai có điểm cao nhất
def diem_duc_phuc(filename):
    data = read_json(filename)

    # Kiểm tra nếu không đọc được dữ liệu
    if data is None:
        print(f"Error: Could not read or parse the JSON file '{filename}'. Please check if the file exists and is valid JSON.")
        return

    # Tính điểm trung bình của Đức Phúc
    diem_duc_phuc = None
    for item in data:
        if item.get('name') == 'Đức Phúc':
            diem_duc_phuc = item.get('scores', [])

    if diem_duc_phuc:
        diem_trung_binh = sum(diem_duc_phuc) / len(diem_duc_phuc)
        print(f"Điểm trung bình của Đức Phúc là: {diem_trung_binh:.2f}")
    else:
        print("Không tìm thấy dữ liệu của 'Đức Phúc' trong file JSON.")

    # Tìm anh trai có điểm cao nhất qua 5 vòng đầu tiên
    max_score = 0
    max_name = ''
    for item in data:
        name = item.get('name')
        scores = item.get('scores')
        if name and scores:
            score_sum = sum(scores[:5])  # Tổng điểm qua 5 vòng đầu
            if score_sum > max_score:
                max_score = score_sum
                max_name = name

    print(f"Anh trai có số điểm cao nhất qua 5 vòng đầu tiên là: {max_name} với {max_score} điểm")

# Chức năng 5: Dừng chương trình
def stop_program():
    print("Chương trình đã dừng.")
    exit()

# Tạo menu
def main():
    while True:
        print("\nMenu:")
        print("1. Thống kê số lượng anh trai theo nghề nghiệp và hiển thị biểu đồ quạt")
        print("2. Thống kê số lượng anh trai theo năm sinh và hiển thị biểu đồ cột")
        print("3. Hiển thị danh sách các anh trai sinh năm 1997")
        print("4. Tính điểm trung bình của 'Đức Phúc' và tìm anh trai có điểm cao nhất")
        print("5. Dừng chương trình")

        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            print("Hãy tải file CSV lên.")
            uploaded = files.upload()
            filename = list(uploaded.keys())[0]
            anh_trai_job(filename)
        elif choice == '2':
            print("Hãy tải file CSV lên.")
            uploaded = files.upload()
            filename = list(uploaded.keys())[0]
            anh_trai_dob(filename)
        elif choice == '3':
            print("Hãy tải file CSV lên.")
            uploaded = files.upload()
            filename = list(uploaded.keys())[0]
            anh_trai_sinh_1997(filename)
        elif choice == '4':
            print("Hãy tải file JSON lên.")
            uploaded = files.upload()
            filename = list(uploaded.keys())[0]
            diem_duc_phuc(filename)
        elif choice == '5':
            stop_program()
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Gọi hàm main để chạy chương trình
main()
