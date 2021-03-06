from github import Github

class GithubInformation(object):
      
    
	 access_Token = ""#Enter your access Token
	 git = Github(access_Token)
	 user = git.get_user("")#Enter your username for example Goodship1
	 
	 @classmethod
	 def get_Public_repository(cls):
		 '''Only gets public repos of user'''
		 repo_Counter = 0
		 repository = sum([repo_Counter+1 for repos in cls.user.get_repos()])
		 return repository
    
     
    
	 @classmethod
	 def get_Stars(cls):
		''' Gets total stars'''
		star_Counter = 0
		stars = sum([star_Counter+1 for star in cls.user.get_starred()]) 
		return stars
		
		
		
	 @classmethod
	 def get_Followers(cls):
		 '''Gets followers'''
		 follower_Count = 0
		 followers = sum([follower_Count+1 for follow in cls.user.get_followers()])
		 return followers

    
   

