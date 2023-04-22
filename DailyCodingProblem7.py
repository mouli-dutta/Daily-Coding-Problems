# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


def num_decodings(message):
    n = len(message)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if message[i-1] != '0':
            dp[i] += dp[i-1]
        if i > 1 and message[i-2:i] >= '10' and message[i-2:i] <= '26':
            dp[i] += dp[i-2]
    return dp[n]

print(num_decodings('111'))