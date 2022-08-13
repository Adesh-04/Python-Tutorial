## Not Completed
class Solution():
    def floodFill(self,image,sr,sc,color):
        self.image = image
        original_color = self.image[sr][sc]
        self.image[sr][sc] = color
        i = 0

        while i < 3:
            i += 1
            if self.image[sr][sc] == color:
                if self.image[sr+1][sc] == original_color:
                    self.image[sr+1][sc] = color
                if self.image[sr+1][sc+1] == original_color:
                    self.image[sr+1][sc+1] = color
                if self.image[sr][sc+1] == original_color:
                    self.image[sr][sc+1] = color
                if self.image[sr][sc] == original_color:
                    self.image[sr][sc] = color
            
        return image
                
                    
            
        
        
        pass
    


image = Solution()
val = image.floodFill( [ [1,1,1],[1,1,0],[1,0,1]], 1, 1, 2  )

print(val)

