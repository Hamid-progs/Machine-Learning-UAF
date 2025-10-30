def LinearRegression(X, Y, T ):
    # Check that both lists have the same length
    if len(X) != len(Y):
        raise ValueError("X and Y must have the same length")

    # Calculate means
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Mean of product of X and Y
    mean_XY = sum(x * y for x, y in zip(X, Y)) / len(X)

    # Mean of X^2
    mean_X2 = sum(x**2 for x in X) / len(X)

    # Square of mean of X
    square_mean_X = mean_X ** 2

    # finding W1 and W0  of y = W1X1 + W0
    W1 = (mean_XY-(mean_X * mean_Y))/(mean_X2 - square_mean_X)
    W0 = mean_Y-(W1*mean_X)

    # Display results
    print(f"Mean of X: {mean_X}")
    print(f"Mean of Y: {mean_Y}")
    print(f"Mean of X*Y: {mean_XY}")
    print(f"Mean of X^2: {mean_X2}")
    print(f"(Mean of X)^2: {square_mean_X}\n")
    print(f"W0 : {W0}")
    print(f"W1 : {W1}\n")

    # Testing  case / Predicting y
    print('Results for Test Cases:')
    for t in T:
        y = (W1 * t) + W0
        print(t," : ", y)



X = [27.9,33.77,33,22.705,28.88,25.74,33.44,27.74,29.83,25.84,26.22]
Y = [16884.92,1725.552,4449.462,21984.47,3866.855,3756.622,8240.59,7281.506,6406.411,28923.14,2721.321]
T = [26.29,34.4,39.82,24.6,30.78]
LinearRegression(X,Y,T)


"""
output:
    Mean of X: 28.642272727272726
    Mean of Y: 9658.259
    Mean of X*Y: 261009.5944963636 
    Mean of X^2: 832.0641840909091 
    (Mean of X)^2: 820.379786983471

    W0 : 47959.97597661613
    W1 : -1337.2443360664545       

    Results for Test Cases:
    26.29  :  12803.82238142904
    34.4  :  1958.7708159300964
    39.82  :  -5289.093485550089
    24.6  :  15063.76530938135
    30.78  :  6799.595312490659
"""