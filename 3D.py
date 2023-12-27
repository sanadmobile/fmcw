import numpy as np

# تحديد عدد الهيدرات
num_headers = 3

# جمع البيانات من الملفات واسترجاع طول الهيدر الأول
first_header_path = f'C:\\Users\\GTR\\Desktop\\2\\Data_Header_1.txt'
first_header_data = np.loadtxt(first_header_path, delimiter=',')
desired_length = len(first_header_data)

# تحديد الطول المحدد للأبعاد في المحور 1
print(f"Desired Length: {desired_length}")

# جمع البيانات من الملفات ومعالجتها لتكون ذات أبعاد متساوية
all_data = []
for i in range(1, num_headers + 1):
    file_path = f'C:\\Users\\GTR\\Desktop\\2\\Data_Header_{i}.txt'
    data = np.loadtxt(file_path, delimiter=',')
    
    # جعل البيانات تحتوي على الطول المحدد في المحور 1
    if len(data) < desired_length:
        data = np.concatenate([data, np.zeros(desired_length - len(data))])
    elif len(data) > desired_length:
        data = data[:desired_length]
    
    all_data.append(data)

# عرض أبعاد البيانات بعد معالجتها
for i, data in enumerate(all_data):
    print(f"Dimensions of Data_Header_{i + 1}: {data.shape}")

# ادماج البيانات بتنسيق XYZ
merged_data = np.vstack(all_data).T

# حفظ البيانات المدمجة في ملف جديد
merged_file_path = 'C:\\Users\\GTR\\Desktop\\2\\Merged_Data.txt'
np.savetxt(merged_file_path, merged_data, fmt="%d", delimiter=',', header='X,Y,Z')

print(f"Data merged and saved to {merged_file_path}")
