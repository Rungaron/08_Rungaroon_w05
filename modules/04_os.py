import os
from pathlib import Path

# ข้อมูลระบบ
os_name = os.name
os_path = os.getcwd()
os_user = os.getenv("USERNAME")

# ทำงานใน path
current_path = Path.cwd()

# สร้างโฟลเดอร์
make_folder = current_path / "test123"
make_folder.mkdir(exist_ok=True)

# สร้างไฟล์
make_file = current_path / "test.txt"
make_file.write_text("Hello word!!!!")

print(f"ขนาดไฟล์ คือ {make_file.stat().st_size} ไบต์")

content = make_file.read_text()
print(content)

content_test = make_file
content =content_test.read_text()
print(content)