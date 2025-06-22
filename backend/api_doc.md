### api đăng ký user mới
response = requests.post("http://127.0.0.1:8000/register", json={
    "username": "ddddd@gmail.com",
    "full_name": "Nguyễn Văn A",
    "password": "123456"
})
print(response.json())

### api đăng nhập, sau khi đăng nhập sẽ trả về session, các thao tác gọi api sau sẽ gửi kém session để lưu vào lịch sử trò chuyện của user
response = requests.post("http://127.0.0.1:8000/login", json={
        "username": email,
        "password": password
    })
print(response.json())


### Phân tích câu tiếng việt và trả về độ khó
### Mô tả:
trường session_id là khi đăng nhập sẽ được cấp, nếu gửi kèm theo trường này thì dữ liệu sẽ được lưu lại cho user
trường conversation_id là mã cuộc trò chuyện, nếu gửi thì cuộc trò chuyện sẽ được ghi tiếp, nếu không gửi thì sẽ tạo một cuộc trò chuyện mới
response = requests.post("http://127.0.0.1:8000/analyze", json={
    "text": "Học sinh cần làm bài tập về nhà mỗi ngày.",
    "session_id": "d610aef7-c579-4148-8e21-23f19e0d8ecb",
    "conversation_id": 2
})
print(response.json())

### Đăng xuất
response = requests.post("http://127.0.0.1:8000/logout", json={
    "session_id": "d610aef7-c579-4148-8e21-23f19e0d8ecb"
})
print(response.json())

### Lấy danh sách cuộc trò chuyện của user
response = requests.post("http://127.0.0.1:8000/conversations", json={
    "session_id": "1a2340e5-9e23-4f96-9017-c06a8064762f"
})
print(response.json())

### Lấy các toàn bộ câu hỏi và trả lời trong 1 cuộc trò chuyện
response = requests.post("http://127.0.0.1:8000/conversation_detail", json={
    "session_id": "7098ede7-8cc2-4baa-b108-84d77e9ea711"
})
print(response.json())