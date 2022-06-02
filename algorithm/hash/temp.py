class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_num_str = ""
        s_idx = list()
        for ss in s:
            if ss not in s_idx:
                s_idx.append(ss)
            s_num_str += str(s_idx.index(ss))
            
        t_num_str = ""
        t_idx = list()
        for tt in t:
            if tt not in t_idx:
                t_idx.append(tt)
            t_num_str += str(t_idx.index(tt))
        
        print(s_num_str, t_num_str)
        # if "".join(s_idx) == "".join(t_idx):
        #     return True
        # else:
        #     return False
