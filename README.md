# 1. Giới thiệu
Xây dựng 1 ứng dụng nhằm theo dõi tin tức từ các trang báo online tại Việt Nam bằng cách áp dụng mô hình chủ đề. Với ứng dụng này, người đọc có thể nắm bắt các 
chủ đề nóng thông qua các từ khóa được xác định từ việc áp dụng mô hình chủ đề. Không chỉ vậy, người dùng còn có thể xem các bài báo liên quan đến từng chủ đề và được gợI 
ý các bài báo có nội dung tương tự với bài báo vừa xem.
# 2. Mô hình chủ đề (Topic modelling)
Top2vec là một phương pháp mới với cách tiếp cận hoàn toàn khác so với các phương pháp truyền thống như LDA, PLSA… Với các phương pháp truyền thống, đó là các mô hình sinh xác suất trong đó mỗi tài liệu như một hỗn hợp các chủ đề và mỗi chủ đề như một sự phân phối của các từ. Ngược lại, top2vec tìm ra các vec-tơ chủ đề bằng cách nhúng các vec-tơ từ và tài liệu vào trong cùng không gian ngữ nghĩa, và những từ gần nhất với vec-tơ chủ đề đó sẽ là những từ mô tả tốt nhất chủ đề đó.
# 3. Nguyên lý hoạt động Top2vec
Thuật toán sẽ giả định nhiều tài liệu giống nhau về mặt ngữ nghĩa sẽ là dấu hiệu của một chủ đề cơ bản. Bước đầu tiên là tạo ra một không gian nhúng chung cá vec-tơ tài liệu và từ. 
Sau khi nằm trong cùng không gian đó, mục tiêu của thuật toán là tìm các cụm tài liệu dày đặc, sau đó xác định những từ nào đã thu hút các liệu đó lại với nhau. 
Mỗi khu vực dày đặc là một chủ đề và các từ thu hút các tài liệu đến các khu vực dày đặc là các từ chủ đề.
 # 4. Chức năng ứng dụng
Ứng dụng sẽ bao gồm một số chức năng:

• Theo dõi các chủ đề theo thời gian từ các trang tin tức online

• Tìm kiếm các bài báo liên quan đến từng chủ đề

• Gợi ý các bài báo liên quan từ một bài báo cụ thể

• Tự động cập nhật theo thời gian


