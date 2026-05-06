import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Regions in Staffordshire
regions = [
    'Stoke-on-Trent',
    'Stafford and Surroundings',
    'East Staffordshire',
    'Cannock Chase',
    'Newcastle-under-Lyme'
]

# Medication list
medicines = [
    'Amoxicillin',
    'Paracetamol',
    'Metformin',
    'Atorvastatin',
    'Omeprazole',
    'Amlodipine',
    'Simvastatin',
    'Ramipril',
    'Salbutamol',
    'Ibuprofen',
    'Lansoprazole',
    'Bisoprolol',
    'Levothyroxine',
    'Codeine',
    'Citalopram',
    'Sertraline',
    'Fluoxetine',
    'Aspirin',
    'Warfarin',
    'Furosemide',
    'Prednisolone',
    'Clopidogrel',
    'Insulin Glargine',
    'Doxycycline',
    'Co-codamol',
    'Gabapentin',
    'Naproxen',
    'Morphine Sulfate',
    'Tramadol',
    'Losartan',
    'Montelukast',
    'Hydrocortisone',
    'Azithromycin',
    'Nitrofurantoin',
    'Cetirizine',
    'Diazepam',
    'Pregabalin',
    'Methotrexate',
    'Quetiapine',
    'Olanzapine'
]

# Drug categories
cardiovascular = [
    'Atorvastatin',
    'Simvastatin',
    'Ramipril',
    'Bisoprolol',
    'Amlodipine',
    'Losartan',
    'Clopidogrel',
    'Warfarin',
    'Furosemide'
]

mental_health = [
    'Citalopram',
    'Sertraline',
    'Fluoxetine',
    'Quetiapine',
    'Olanzapine',
    'Diazepam'
]

antibiotics = [
    'Amoxicillin',
    'Doxycycline',
    'Azithromycin',
    'Nitrofurantoin'
]

# Empty list for rows
rows = []

# Generate 5000 rows
for i in range(5000):

    # Randomly select medication
    drug = np.random.choice(medicines)

    # Assign category
    if drug in cardiovascular:
        category = 'Cardiovascular'

    elif drug in mental_health:
        category = 'Mental Health'

    elif drug in antibiotics:
        category = 'Antibiotics'

    else:
        category = 'General Medicine'

    # Generate random cost
    cost = round(np.random.uniform(100, 5000), 2)

    # Introduce some missing values
    if np.random.rand() < 0.05:
        cost = np.nan

    # Create row
    rows.append({
        'region': np.random.choice(regions),
        'drug_name': drug,
        'drug_category': category,
        'items_prescribed': np.random.randint(50, 600),
        'cost': cost,
        'deprivation_score': np.random.randint(10, 30),
        'shortage_incidents': np.random.randint(40, 220),
        'pharmacy_density': round(np.random.uniform(1.2, 2.5), 2),
        'year': np.random.choice([2022, 2023, 2024])
    })

# Convert to dataframe
df = pd.DataFrame(rows)

# Export dataset
df.to_csv('sample_dataset.csv', index=False)

# Preview first rows
print(df.head())