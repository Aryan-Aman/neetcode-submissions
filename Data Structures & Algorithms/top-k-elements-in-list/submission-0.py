class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count frq and no.->arr convert and sort for oprn->res append
        count_map={}
        for n in nums:
            count_map[n] = 1+ count_map.get(n, 0) 
        
        arr=[]
        for key_no, value_cnt in count_map.items():
            arr.append([value_cnt, key_no])
        arr.sort()

        res=[]
        while len(res)<k:
            res.append(arr.pop()[1])
        return res