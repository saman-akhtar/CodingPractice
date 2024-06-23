
# Code Question

# New Year's Day is around the corner and our company  is having a sale. They have a list of items they are considering but they may need to remove some of them. Determine the minimum number of items to remove from an array of prices so that the sum of prices of any k items does not exceed a threshold.

# Note: If the number of items in the list is less than k, then there is no need to remove any more items.

# Example:
# prices = [3, 2, 1, 4, 6, 5]
# k = 3
# threshold = 14

# The sum of prices for every k = 3 items must not be more than threshold = 14. The sum of the prices of the last three items is 6 + 5 + 4 = 15. The minimum number of items to remove so that the sum of the prices of any k items does not exceed the threshold is 1.


# ANSWER
import sys
import json

def reduceGifts(prices, k , threshold):
    print(f"Prices: {prices}, k: {k}, Threshold: {threshold}")
    if(len(prices)< k):
        return 0
    prices = sorted(prices, reverse = True)
    sums= sum(prices[:k])
    r = k - 1
    l =0
    while(r < len(prices)):
        print(f" for {l} {r}: sum = {sums}")
        if(sums > threshold):
            sums = sums - prices[l]
            l = l + 1
            sums = sums + prices[l]
        else:
            break;
        r = r +1
    print("ANS :",l -1)
    return l -1

def main():
    print(sys.argv,len(sys.argv))
    if len(sys.argv) !=4:
        print("Usage: script.py <prices> <k> <threshold>")
        sys.exit(1)
    prices_arg = sys.argv[1]
    k = int(sys.argv[2])
    threshold = int(sys.argv[3])
    try:
        prices = json.loads(prices_arg) 
        if not isinstance(prices, list):
            # If the result is not a list, raise a ValueError
            raise ValueError
    except (ValueError, json.JSONDecodeError) as e:
        print("Error: Prices should be a list of integers.",e)
        sys.exit(1)
    
    reduceGifts(prices, k , threshold)
if __name__ == "__main__":
    main()


#test cases
# [9,6,7,2,7,2] 2  13
# [9,6,3,2,9,10,10,11] 4  1

#Time / Space complexity
# TC O(n log n) + iterantion no of windows => O(nlogn)
# Sp O(1)
