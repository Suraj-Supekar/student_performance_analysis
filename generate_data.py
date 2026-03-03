import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Connection to your SQL
engine = create_engine('sqlite:///student_data.db')

def generate_bulk_data(n=100):
    np.random.seed(42)
    
    data = {
        'attendance_rate': np.random.uniform(0.5, 1.0, n),
        'study_hours': np.random.randint(2, 25, n),
        'previous_score': np.random.randint(30, 100, n)
    }
    
    df = pd.DataFrame(data)
    
    # Logic: Probability of passing increases with attendance and study hours
    # This ensures the AI has a pattern to learn!
    noise = np.random.normal(0, 5, n)
    score = (df['attendance_rate'] * 50) + (df['study_hours'] * 2) + noise
    df['passed'] = (score > 60).astype(int)
    
    # Upload to SQL (Replace existing data)
    df.to_sql('student_performance', con=engine, if_exists='replace', index_label='student_id')
    print(f"Successfully uploaded {n} student records to SQL.")

if __name__ == "__main__":
    generate_bulk_data(100)