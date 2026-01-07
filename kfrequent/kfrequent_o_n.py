def top_kfrequent_o_n(nums: list[int], k: int) -> list[int]:
    frequencies = {} # space o(n) worst case; happens when all elements are distinct. where n is number of elements in nums
    nums_length = len(nums)
    freqs_list = [[] for _ in range(nums_length)] # space o(n)
    
    # store frequencies of all numbers
    for number in nums: # o(n)
        frequencies[number] = 1 + frequencies.get(number, 0)

    # put the numbers in buckets according to their frequency so that (index of bucket)=frequency-1
    # we do this after frequencies are set in order to avoid having same number with different frequencies
    for number, frequency in frequencies.items(): # o(n) worst case; distinct elements
        freqs_list[frequency-1].append(number)
    
    top_k = [] # space o(k)
    counter = 1
    # extract the top k frequent elements from freqs_list
    while len(top_k) < k: # o(n + k) where k is slicing cost; at most k elements copied during all loop iterations
        k_left = k - len(top_k)
        if freqs_list[nums_length-counter]: # if sublist exists since we can have some empty sublists if no number has the corresponding frequency
            top_k += freqs_list[nums_length-counter][:k_left] # merge sublist with top_k up to space left in top_k
        counter += 1 

    return top_k
