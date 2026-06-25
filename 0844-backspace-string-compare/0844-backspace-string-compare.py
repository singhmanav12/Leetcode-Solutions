class Solution(object):
    def backspaceCompare(self, s, t):
        def build_final_string(string_to_process):
            List= []
            for i in string_to_process :
                if i!= '#':
                    List.append(i)
                elif List:
                    List.pop()
                
            return "".join(List)
            
            # Process both strings and compare the final results
        return build_final_string(s) == build_final_string(t)