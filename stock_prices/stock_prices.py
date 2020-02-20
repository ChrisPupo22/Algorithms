#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #pseudocoded steps to solution:
  # prices_length = len(prices)
  # print(prices_length)
  #set iterators through prices arr and set profit variable
  # arr_length = len(prices)
  total_profit = 0
  
  # first_iterator = prices[c]
  # second_iterator = first_iterator + 1

  #compare the first iterator with second iterator 
  for i in prices:
    first_iterator = prices[i]
    # second_iterator = prices[i]
    print(first_iterator)

    # print(second_iterator)
  

    # if first_iterator < second_iterator: 
    #   current_profit = second_iterator - first_iterator 
    #   first_iterator + 1
    #   second_iterator + 1 
    #   if current_profit > total_profit: 
    #     total_profit = current_profit
    # else: 
    #   return total_profit

  

print(find_max_profit([10, 20, 30, 80]))


  #subtract if first iterator is less than second iterator


  #check for edge cases 
  


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))