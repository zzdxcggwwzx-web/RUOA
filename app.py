import numpy as np
from sklearn.linear_model import LinearRegression

# 1. เตรียมข้อมูลสมมติ (เช่น x คือชั่วโมงอ่านหนังสือ, y คือคะแนนสอบ)
# รูปแบบข้อมูลต้องเป็น 2D array สำหรับ X
X = np.array([[1], [2], [3], [4], [5]]) 
y = np.array([2, 4, 5, 4, 5])

# 2. สร้าง Model
model = LinearRegression()

# 3. สอน AI (Training)
model.fit(X, y)

# 4. ลองให้ AI ทำนายดู (Prediction)
# อยากรู้ว่าถ้าอ่านหนังสือ 6 ชั่วโมง จะได้คะแนนเท่าไหร่?
hours = np.array([[6]])
prediction = model.predict(hours)

print(f"ถ้าอ่าน 6 ชม. AI บอกว่าน่าจะได้คะแนนประมาณ: {prediction[0]:.2f}")
