
import signal 
import gi
import os
from GithubInformation import GithubInformation
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
 


class GithubInfobar(object):
	
		
	    
		def __init__(self):
		    self.indicator = appindicator.Indicator.new("githubapplication" , os.path.dirname(os.path.realpath(__file__))+'/image/github.jpg',appindicator.IndicatorCategory.APPLICATION_STATUS)
		    self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
		    self.indicator.set_menu(gtk.Menu())
		    self.public_repo = self.repositories
		    self.total_stars = self.stars
		    self.total_followers = self.followers
		    self.indicator.set_label(" Repositories: %s  Stars: %s  Followers: %s "%(self.repositories,self.total_stars,self.total_followers),"number of public repos")
		    
		 
		
		
		def _github_Info(self):
			git = GithubInformation()
			repos = git.get_Public_repository()
			stars = git.get_Stars()
			followers = git.get_Followers()
			return (repos,stars,followers)
		
		
		
		
		@property
		def repositories(self):
			repos = self._github_Info()
			return str(repos[0])
		
		@property
		def stars(self):
			stars = self._github_Info()
			return str(stars[1])
		
		@property
		def followers(self):
			followers = self._github_Info()
			return str(followers[2])
		
		
		
		@staticmethod
		def main():
			git = GithubInfobar()
			signal.signal(signal.SIGINT,signal.SIG_DFL)
			gtk.main()
	
	
		



if __name__ == "__main__":					     
    GithubInfobar.main()
					     

