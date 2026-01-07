from kfrequent.kfrequent_o_n import top_kfrequent_o_n

# Problem statement
###################
# Given an integer array nums and an integer k, return the k most frequent elements within the array.


if __name__ == '__main__':
    nums = [1,2,2,3,3,3]
    k = 2
    k_freqs = top_kfrequent_o_n(nums, k)
    print(k_freqs)