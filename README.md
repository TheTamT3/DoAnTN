# 1. Giới thiệu
Xây dựng 1 ứng dụng nhằm theo dõi tin tức từ các trang báo online tại Việt Nam bằng cách áp dụng mô hình chủ đềE Với ứng dụng này, người đọc có thềEnắm bắt các 
chủ đềEnóng thông qua các từ khóa được xác định từ việc áp dụng mô hình chủ đềE Không chềEvậy, người dùng còn có thềExem các bài báo liên quan đến từng chủ đềEvà được gợI 
ý các bài báo có nội dung tương tự với bài báo vừa xem.

# 2. Mô hình chủ đềE(Topic modelling)
Top2vec là một phương pháp mới với cách tiếp cận hoàn toàn khác so với các phương pháp truyền thống như LDA, PLSA… Với các phương pháp truyền thống, đó là các mô hình sinh xác suất trong đó mỗi tài liệu như một hỗn hợp các chủ đềEvà mỗi chủ đềEnhư một sự phân phối của các từ. Ngược lại, top2vec tìm ra các vec-tơ chủ đềEbằng cách nhúng các vec-tơ từ và tài liệu vào trong cùng không gian ngữ nghĩa, và những từ gần nhất với vec-tơ chủ đềEđó sẽ là những từ mô tả tốt nhất chủ đềEđó.
# 3. Nguyên lý hoạt động Top2vec
Thuật toán sẽ giả định nhiều tài liệu giống nhau vềEmặt ngữ nghĩa sẽ là dấu hiệu của một chủ đềEcơ bản. Bước đầu tiên là tạo ra một không gian nhúng chung cá vec-tơ tài liệu và từ. 
Sau khi nằm trong cùng không gian đó, mục tiêu của thuật toán là tìm các cụm tài liệu dày đặc, sau đó xác định những từ nào đã thu hút các liệu đó lại với nhau. 
Mỗi khu vực dày đặc là một chủ đềEvà các từ thu hút các tài liệu đến các khu vực dày đặc là các từ chủ đềE
 # 4. Chức năng ứng dụng
Ứng dụng sẽ bao gồm một sềEchức năng:

• Theo dõi các chủ đềEtheo thời gian từ các trang tin tức online

• Tìm kiếm các bài báo liên quan đến từng chủ đềE

• Gợi ý các bài báo liên quan từ một bài báo cụ thềE

• Tự động cập nhật theo thời gian



 

 


 



