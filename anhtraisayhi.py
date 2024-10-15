import json
from google.colab import files
import csv
import matplotlib.pyplot as plt
from collections import Counter

# Hàm đọc file CSV
def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Bỏ qua dòng tiêu đề
        data = []
        for row in reader:
            data.append(row)
    return data

# Hàm đọc file JSON
def read_json(filename):
    """Đọc dữ liệu từ tệp JSON và trả về nội dung."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error decoding JSON file: {e}")
        return None

# Chức năng 1: Thống kê số lượng anh trai theo nghề nghiệp
def anh_trai_job(filename):
    data = read_csv(filename)
    jobs = [row[1] for row in data]  # Giả sử cột nghề nghiệp là cột thứ 3
    job_count = Counter(jobs)

    # Vẽ biểu đồ quạt
    plt.figure(figsize=(8, 6))
    plt.pie(job_count.values(), labels=job_count.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Thống kê số lượng anh trai theo nghề nghiệp')
    plt.show()

# Chức năng 2: Thống kê số lượng anh trai theo năm sinh
def anh_trai_dob(filename):
    data = read_csv(filename)
    years_of_birth = [row[3] for row in data]  # Giả sử cột năm sinh là cột thứ 2
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
    result = [row for row in data if row[3] == '1997']  
    print("Danh sách các anh trai sinh năm 1997:")
    for row in result:
        print(row)

# Chức năng 4: Tính điểm trung bình của 'Đức Phúc' và tìm anh trai có điểm cao nhất
def diem_duc_phuc(filename):
    # Đọc dữ liệu từ tệp JSON
    data = read_json(filename)

    # Kiểm tra nếu không đọc được dữ liệu
    if data is None:
        print(f"Error: Could not read or parse the JSON file '{filename}'. Please check if the file exists and is valid JSON.")
        return

    # Khởi tạo các biến để lưu trữ tổng điểm, số lượng đội của Đức Phúc, và điểm cao nhất
    total_score = 0
    team_count = 0
    highest_score = 0
    highest_team = None
    round_count = 0  # Đếm số vòng đã thêm vào

    # Hàm thêm dữ liệu đội
    def add_team_data(team_name, members, score):
        nonlocal total_score, team_count, highest_score, highest_team, round_count
        # Kiểm tra xem Đức Phúc có trong đội không
        if "Đức Phúc" in members:
            total_score += score
            team_count += 1
        # Kiểm tra số vòng, cập nhật điểm cao nhất trong 5 vòng đầu tiên
        if round_count < 5:  # Chỉ xem xét trong 5 vòng đầu tiên
            if score > highest_score:
                highest_score = score
                highest_team = team_name
        round_count += 1  # Tăng số vòng

    # Thêm dữ liệu các đội lần lượt
    for team in data:
        if "team_name" in team and "members" in team and "score" in team:
            add_team_data(team["team_name"], team["members"], team["score"])

    # Tính điểm trung bình của Đức Phúc
    average_score = total_score / team_count if team_count > 0 else 0

    # Hiển thị kết quả
    print(f"Điểm trung bình của Đức Phúc là {average_score:.2f}")
    if highest_team:
        print(f"Đội có điểm cao nhất trong 5 vòng đầu tiên là {highest_team} với số điểm {highest_score}")

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
