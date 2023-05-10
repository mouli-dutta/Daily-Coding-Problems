# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

def find_max_profit(a):

    max = float('-inf')

    

    for i in range(len(a)):

        for j in range(i, len(a)):

            if a[i] < a[j]:

                diff = abs(a[i] - a[j])

                

                if diff > max:

                    max = diff

    return max

a = [9, 11, 8, 5, 7, 10]

print(find_max_profit(a))
