import pandas as pd

# Caliber Input
caliber_data = input('Caliber: ')

# Nested Dict. Input -> Load details
bullet_brand_value = input('Brand: ')
bullet_model_value = input('Model: ')
case_value = input('Case: ')

new_row = {'Caliber':caliber_data, 'Bullet Brand':bullet_brand_value, 'Bullet Model':bullet_model_value, 'Case':case_value}
df = pd.concat([df,pd.DataFrame([new_row])], ignore_index=True)
df


# Test