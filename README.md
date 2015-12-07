# Analysis
Genetic Algorithm using Simple Moving Average
1. Calculate the moving average using some parameters
2. Calculate another moving average using another parameter
3. Compare the two moving averages from 1 & 2 to see if they cross
4. If they cross then this is a signal. We must compare it against the real result and if it is above the result, then sell. If it is below the result, then buy.
5. If the prediction is correct, then it stays in the GA. Otherwise it is eliminated from the gene pool
Result: The final result should be the best moving average parameters


Details:
1. Encode the parameters of the MA as chromosomes.
We can choose the parameters to be binary strings. For example, using an 8 bit string would be searching between 1 and 256. Since we have limited resources, we should choose something with low search space so it actually terminates.