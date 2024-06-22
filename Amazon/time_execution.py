#Question
# Cloud1 is a cloud computing platform with multiple servers. One of the servers is assigned to serve customer requests. There are 
# 𝑛
# n customer requests placed sequentially in a queue, where the 
# 𝑖
# 𝑡
# ℎ
# i 
# th
#   request has a maximum waiting time denoted by wait[i]. That is, if the 
# 𝑖
# 𝑡
# ℎ
# i 
# th
#   request is not served within wait[i] seconds, then the request expires and it is removed from the queue. The server processes the request following the First In First Out (FIFO) principle. The 1st request is processed first, and the 
# 𝑛
# 𝑡
# ℎ
# n 
# th
#   request is served last. At each second, the first request in the queue is processed. At the next second, the processed request and any expired requests are removed from the queue.

# Given the maximum waiting time of each request denoted by the array wait, find the number of requests present in the queue at every second until it is empty.

# Note:

# If a request is served at some time instant t, it will be counted for that instant and is removed at the next instant.
# The first request is processed at time = 0. A request expires without being processed when time = wait[i]. It must be processed while time < wait[i]. See the example below for wait[3].
# The initial queue represents all requests at time = 0 in the order they must be processed.
# Example:
# The number of requests is 
# 𝑛
# =
# 4
# n=4, and their maximum wait times are wait = [2, 2, 3, 1].



#answer
