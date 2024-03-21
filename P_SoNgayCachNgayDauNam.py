ngay = int(input("Nhập ngày : "))
thang = int(input("Nhập tháng : "))

so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Số ngày trong từng tháng của năm không nhuận

so_ngay = sum(so_ngay_trong_thang[:thang - 1]) + ngay  # Tính số ngày từ đầu năm đến ngày nhập vào

print("Ngày", ngay, "tháng", thang, "cách ngày đầu năm", so_ngay, "ngày")  # In ra kết quả
