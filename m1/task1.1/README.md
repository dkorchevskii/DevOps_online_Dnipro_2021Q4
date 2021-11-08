TASK 1.1
1. For this task i'm using my regular OS, that alreaday has git installed.

2. I changed my global configs with this commans: 
	git config --global user.name "dkorchevskii"
	git config --global user.email "dkorchevskii@gmail.com"
	git config --global core.editor vim 
	
3. I created new account on GitHub for this course with dkorchevskii@gmail.com email.

4. I created new private repo on GitHub with name: DevOps_online_Dnipro_2021Q4

5. To clone repo to my workstation with ssh i firstly set up ssh key localy, added private key to ssh agent and public key to my github account.

6. Then i cloned the repo with this command 
	git clone git@github.com:dkorchevskii/DevOps_online_Dnipro_2021Q4.git

7. I Opened git console in root directory of my project and created folders for this task:
	mkdir m1/task1.1

8. I created empty readme.txt file.
	touch readme.txt

9. I made all files trackable with this command
	git add .
	
10. My first commit 
	git commit -m "First commit. Empty file readme.txt has been added" 

11. I created develop branch and checkout on it with one command
	git checkout -b develop
	
12. Created index.html empty file. Made files in branch trackable.  Commited.
	
	touch index.html
	git add .
	git commit -m "New empty file index.html"


13. Created branch with name “images”. Checked on it. Added images folder with some images inside it. Commited.
	git checkout -b images
	mkdir images
	git add .
	git commit -m "New folder images with some image files inside"
	
14. Changed index.html, added images source inside it. Commited.
		<!DOCTYPE html>
		<html>
		<body>
		
		<h1>Nasa images</h1>
		<p>Photos of the day</p>
		
		<img src="images/1.jpg" style="width:900px;height:600px;">
		<img src="images/2.jpg" style="width:900px;height:600px;">
		<img src="images/3.jpg" style="width:900px;height:600px;">
		<img src="images/4.jpg" style="width:900px;height:600px;">
		<img src="images/5.jpg" style="width:900px;height:600px;">	
					   
		</body>
		</html>
		
	git add .
	git commit -m "Added image sources to index.html"

15. Went back to develop branch. Created branch with name “styles”. Checked on it. Added styles folder with styles source inside it. Commited.
	git switch develop
	git checkout -b styles
	mkdir styles
	touch styles/styles.css
	git add .
	git commit -m "New folder styles with styles.css file inside"

16. Added styles source to my index.html. Commited.
		 <!DOCTYPE html>
	<html>
	<head>
	<link rel="stylesheet" href="styles/styles.css">
	</head>
	<body>
	</body>
	</html>
	
	git add .
	git commit -m "Styles source added to index.html"

17. Went to develop branch.
		git switch develop    
18. Merged two new branches into develop using git merge command.
		git merge images  	
		git merge styles - Here i had merge conflict in index.html. In text editor i edited file to include all necessary code. 
		git add .
		git commit -m "Images ans styles branches are merged into develop, conflict resolved in index.html"

19. Merged develop into master.
		git switch main
		git merge develop 
		
20. I inspected my repository with git log command using different options like
	git log -p to see the exact changes made to a repository
	git log --oneline to retrieve a list of commit IDs and their associated commit messages
	git log -n 3 - to see a list of the three most recent commits made to a repository

21. I pushed all your changes with all your branches to origin (git push origin --all).

22. Execute command “git reflog“ and save it content somewhere (not in
repository) with filename “task1.1_GIT.txt”.
	git reflog > ~/task1.1_GIT.txt 
23. task1.1_GIT.txt added to local repo, then pushed it to GitHub.
	cp ~/task1.1_GIT.txt ~/DevOps_online_Dnipro_2021Q4/m1/task1.1/
	git add .
	git commit -m "file with git reflog output added"
	git push
	
24. Made file readme.md in folder task1.1 and described results of my work with Git.

25. Final commit and push
	git add .
	git commit -m "README.md added to task folder"
	git push

As i see - DevOps is a combiantion of tools and practises, that helps to highly improve the process of software devepolment by implementing cultures of collaboration, automation, continuous integration, continuous delivery, continuous testing, continuous monitoring and by breaking barriers between dev and ops departments.