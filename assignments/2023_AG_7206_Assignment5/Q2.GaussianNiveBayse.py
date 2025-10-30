import math

def train_gaussian_nb(data):
    # Separate data by class
    separated = {'M': {'Radius Mean': [], 'Texture Mean': [], 'Perimeter Mean': []},
                 'B': {'Radius Mean': [], 'Texture Mean': [], 'Perimeter Mean': []}}
    
    for i in range(len(data['Diagnosis'])):
        diag = data['Diagnosis'][i]
        separated[diag]['Radius Mean'].append(data['Radius Mean'][i])
        separated[diag]['Texture Mean'].append(data['Texture Mean'][i])
        separated[diag]['Perimeter Mean'].append(data['Perimeter Mean'][i])
    
    # Calculate mean and variance for each class and feature
    model = {}
    for diag in separated:
        model[diag] = {}
        for feature in separated[diag]:
            values = separated[diag][feature]
            mean_val = sum(values) / len(values)
            variance = sum((x - mean_val) ** 2 for x in values) / len(values)
            model[diag][feature] = {"mean": mean_val, "variance": variance}
    
    # Prior probabilities
    total = len(data['Diagnosis'])
    model['priors'] = {
        'M': data['Diagnosis'].count('M') / total,
        'B': data['Diagnosis'].count('B') / total
    }
    
    return model


def gaussian_probability(x, mean, variance):
    if variance == 0:
        return 0
    exponent = math.exp(-((x - mean) ** 2) / (2 * variance))
    return (1 / math.sqrt(2 * math.pi * variance)) * exponent


def predict_gaussian_nb(model, test):
    probs = {}
    for diag in ['M', 'B']:
        prior = model['priors'][diag]
        likelihood = 1
        for feature, x in test.items():
            mean = model[diag][feature]["mean"]
            var = model[diag][feature]["variance"]
            likelihood *= gaussian_probability(x, mean, var)
        probs[diag] = likelihood * prior
    
    print("\n=== Gaussian Probabilities ===")
    for cls, val in probs.items():
        print(f"P({cls}) = {val}")
    
    predicted = max(probs, key=probs.get)
    print(f"\n✅ Predicted Diagnosis: {predicted}")
    return predicted


data = {
    "Diagnosis": ["M", "M", "M", "M", "M", "B", "B", "B", "B", "B"],
    "Radius Mean": [17.99, 20.57, 19.69, 11.42, 20.29, 13.54, 13.08, 9.504, 13.49, 11.76],
    "Texture Mean": [10.38, 17.77, 21.25, 20.38, 14.34, 14.36, 15.71, 12.44, 22.3, 21.6],
    "Perimeter Mean": [122.8, 132.9, 130, 77.58, 135.1, 87.46, 85.63, 60.34, 86.91, 74.72]
}


# Step 1 – Train model
model = train_gaussian_nb(data)

# Step 2 – Predict for test sample
test = {"Radius Mean": 15, "Texture Mean": 11, "Perimeter Mean": 110}
predict_gaussian_nb(model, test)


"""
output:
    === Gaussian Probabilities ===
    P(M) = 2.3243341165510906e-05
    P(B) = 3.539921234915204e-07

    ✅ Predicted Diagnosis: M
"""