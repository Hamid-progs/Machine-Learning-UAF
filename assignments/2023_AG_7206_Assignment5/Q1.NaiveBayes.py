def train_naive_bayes(train):
    # Get unique SaleCondition classes
    sale_conditions = list(set(train["SaleCondition"]))
    total = len(train["SaleCondition"])
    
    # Step 1: Compute prior probabilities P(SaleCondition)
    class_counts = {cond: train["SaleCondition"].count(cond) for cond in sale_conditions}
    priors = {cond: class_counts[cond] / total for cond in sale_conditions}
    
    # Step 2: Compute conditional probabilities P(feature=value | SaleCondition)
    cond_probs = {}
    
    for feature in train:
        if feature == "SaleCondition":
            continue
        
        cond_probs[feature] = {}
        unique_values = set(train[feature])
        
        for value in unique_values:
            cond_probs[feature][value] = {}
            
            for cond in sale_conditions:
                count_feature_and_cond = 0
                count_cond = class_counts[cond]
                
                # Count how many times this value appears for this SaleCondition
                for i in range(total):
                    if train[feature][i] == value and train["SaleCondition"][i] == cond:
                        count_feature_and_cond += 1
                        
                cond_probs[feature][value][cond] = count_feature_and_cond / count_cond if count_cond != 0 else 0
    
    # Return model
    return {"priors": priors, "conditionals": cond_probs}


def predict_naive_bayes(model, test_sample):
    priors = model["priors"]
    cond_probs = model["conditionals"]
    
    # Initialize probability for each SaleCondition
    results = {}
    
    for cond in priors:
        prob = priors[cond]  # Start with prior probability
        
        # Multiply with each conditional probability
        for feature, value in test_sample.items():
            feature_probs = cond_probs.get(feature, {})
            value_probs = feature_probs.get(value, {})
            prob *= value_probs.get(cond, 0)
        
        results[cond] = prob
    
    # Show all calculated probabilities
    print("\n=== Probabilities for Each SaleCondition ===")
    for cond, p in results.items():
        print(f"{cond}: {p}")
    
    # Return class with highest probability
    prediction = max(results, key=results.get)
    print(f"\n✅ Predicted SaleCondition: {prediction}")
    return prediction



train = {
    "Exposure":['no','gd','gd',"no","av","av","av","gd","no","no","no","no","no","av"],
    'GrageType':['attchd','attchd','attchd','detchd','attchd','builtin','attchd','attchd','builtin','attchd','detchd','builtin','detchd','attchd'],
    'Mass':['brkface','stone','brkface','stone','brkface','tile','stone','stone','brkface','brkface','tile','brkface','tile','stone'],
    "Type1":["g","a","g","a","g","g","g","a","a","g","g","g","g","a"],
    "SaleCondition":['Partial','Normal','Normal','Abnrml','Normal','Partial','Normal','Normal','Abnrml','Normal','Normal','Partial','Normal','Partial']
}

# Step 1: Train the model
model = train_naive_bayes(train)

# Step 2: Test sample
test = {"Exposure": "gd", "GrageType": "detchd", "Mass": "tile", "Type1": "a"}

# Predict
predict_naive_bayes(model, test)



"""
output: 
    === Probabilities for Each SaleCondition ===
    Abnrml: 0.0
    Normal: 0.0033482142857142855
    Partial: 0.0

    ✅ Predicted SaleCondition: Normal
"""