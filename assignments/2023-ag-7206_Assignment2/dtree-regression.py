# import pandas as pd
# import numpy as np

# data = {
#     "Vehicle_Class": ["COMPACT","COMPACT","COMPACT","SMALL","SMALL","MID","SMALL","SMALL","COMPACT","MID","SMALL","SMALL"],
#     "Engine_Size":   ["A","A","B","C","C","C","B","A","B","A","A","B"],
#     "Fuel_Type":    ["Z","E","E","Z","Z","T","E","E","T","Z","E","Z"],
#     "Fuel_Consumption": ["H","M","L","L","M","L","M","L","L","M","L","L"],
#     "CO2": [196,221,136,255,244,230,212,225,239,359,359,338]
# }

# df = pd.DataFrame(data)
# target_mean = df["CO2"].mean()
# target_std = df["CO2"].std(ddof=0)   # population std (used in trees)

# print("Target Mean (CO2):", target_mean)
# print("Target Std (CO2):", target_std)

# def weighted_std(column):
#     total_rows = len(df)
#     weighted_std = 0

#     print(f"\nColumn: {column}")
    
#     for value in df[column].unique():
#         subset = df[df[column] == value]["CO2"]
#         weight = len(subset) / total_rows
#         std = subset.std(ddof=0)
#         avg = subset.mean()
        
#         weighted_std += weight * std
        
#         print(f"  Value: {value} | Count: {len(subset)} | Mean: {avg:.2f} | Std: {std:.2f}")
    
#     return weighted_std

# results = {}

# for col in ["Vehicle_Class", "Engine_Size", "Fuel_Type", "Fuel_Consumption"]:
#     w_std = weighted_std(col)
#     std_reduction = target_std - w_std
#     results[col] = std_reduction
    
#     print(f"Weighted Std of {col}: {w_std:.4f}")
#     print(f"Std Reduction: {std_reduction:.4f}")

# best_feature = max(results, key=results.get)

# print("\nStandard Deviation Reduction for each column:")
# for k, v in results.items():
#     print(f"{k}: {v:.4f}")

# print("\n✅ Parent Node (Best Split):", best_feature)





# import pandas as pd
# import numpy as np

# data = {
#     "Engine_Size": ["A", "A", "B", "B"],
#     "Fuel_Type":   ["Z", "E", "E", "T"],
#     "Fuel_Consumption":    ["H", "M", "L", "L"],
#     "CO2":          [196, 221, 136, 239]
# }

# df = pd.DataFrame(data)
# target_mean = df["CO2"].mean()
# target_std = df["CO2"].std(ddof=0)   # population std (used in trees)

# print("Target Mean (CO2):", target_mean)
# print("Target Std (CO2):", target_std)

# def weighted_std(column):
#     total_rows = len(df)
#     weighted_std = 0

#     print(f"\nColumn: {column}")
    
#     for value in df[column].unique():
#         subset = df[df[column] == value]["CO2"]
#         weight = len(subset) / total_rows
#         std = subset.std(ddof=0)
#         avg = subset.mean()
        
#         weighted_std += weight * std
        
#         print(f"  Value: {value} | Count: {len(subset)} | Mean: {avg:.2f} | Std: {std:.2f}")
    
#     return weighted_std

# results = {}

# for col in [ "Engine_Size", "Fuel_Type", "Fuel_Consumption"]:
#     w_std = weighted_std(col)
#     std_reduction = target_std - w_std
#     results[col] = std_reduction
    
#     print(f"Weighted Std of {col}: {w_std:.4f}")
#     print(f"Std Reduction: {std_reduction:.4f}")

# best_feature = max(results, key=results.get)

# print("\nStandard Deviation Reduction for each column:")
# for k, v in results.items():
#     print(f"{k}: {v:.4f}")

# print("\n✅ Parent Node (Best Split):", best_feature)




import pandas as pd
import numpy as np

data = {
    "Engine_Size": ["C", "A"],
    "Fuel_Type":   ["T","Z"],
    "Fuel_Consumption":    ["L", "M"],
    "CO2":          [230,359 ]
}

df = pd.DataFrame(data)
target_mean = df["CO2"].mean()
target_std = df["CO2"].std(ddof=0)   # population std (used in trees)

print("Target Mean (CO2):", target_mean)
print("Target Std (CO2):", target_std)

def weighted_std(column):
    total_rows = len(df)
    weighted_std = 0

    print(f"\nColumn: {column}")
    
    for value in df[column].unique():
        subset = df[df[column] == value]["CO2"]
        weight = len(subset) / total_rows
        std = subset.std(ddof=0)
        avg = subset.mean()
        
        weighted_std += weight * std
        
        print(f"  Value: {value} | Count: {len(subset)} | Mean: {avg:.2f} | Std: {std:.2f}")
    
    return weighted_std

results = {}

for col in [ "Engine_Size", "Fuel_Type", "Fuel_Consumption"]:
    w_std = weighted_std(col)
    std_reduction = target_std - w_std
    results[col] = std_reduction
    
    print(f"Weighted Std of {col}: {w_std:.4f}")
    print(f"Std Reduction: {std_reduction:.4f}")

best_feature = max(results, key=results.get)

print("\nStandard Deviation Reduction for each column:")
for k, v in results.items():
    print(f"{k}: {v:.4f}")

print("\n✅ Parent Node (Best Split):", best_feature)
