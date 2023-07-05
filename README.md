**NHÓM ThreeSome LỚP CS114.N21**

Thành viên nhóm <br> 
Họ và tên: Hàn Phi Trường (Nhóm trưởng) <br>
MSSV: 20522081 <br>
Lớp: KHMT2020 <br>

Họ và tên: Nguyễn Thành Đạt <br>
MSSV: 20520154 <br>
Lớp: KHMT2020 <br>

Họ và tên: Lê Duy Trường <br>
MSSV: 20522083 <br>
Lớp: KHMT2020 <br>

** Hướng dẫn sử dụng thư viện chat-downloader để tải comment trên you tube về**
<br>Tìm hiểu thêm về thư viện tại đây: https://github.com/xenova/chat-downloader<br>
<br>Cài đặt thư viện bằng cách<br>
```
   $ pip install chat-downloader
```
<br>Chạy file chat_live_on_youtube.py<br>
<br>Thay đổi link và thời gian để có thể thu thập data vào những thời điểm cao trào (tham khảo chat-downloader github của xenova phía trên)<br>
<br>![image](https://github.com/TruongNoDame/Comments-Esport-Livestream-Gam-R7/blob/main/images/1.png)<br>
<br>Thu được file dataset dạng .xlsx<br>
<br>![image](https://github.com/TruongNoDame/Comments-Esport-Livestream-Gam-R7/blob/main/images/2.png)<br>
<br>Lấy data vừa thu thập gán nhãn<br>
<br>![image](https://github.com/TruongNoDame/Comments-Esport-Livestream-Gam-R7/blob/main/images/3.png)<br>

**Hướng dẫn sử dụng api của chatGPT để gán nhãn**
<br>Ta sẽ chạy file `data_labeling_chatgpt.py`
```
  python data_labeling_chatgpt.py
```

<br>Chạy trên file notebook Toxic_comment_on_Esports_livestream.ipynb trên Google Colab và chờ đợi kết quả<br>
<br>![image](https://github.com/TruongNoDame/Comments-Esport-Livestream-Gam-R7/blob/main/images/4.png)<br>
