.PHONY: git-automated
git-automated:
	# remove the .idea folder
	# remember that another option is to add it to the
	# .gitignore file so it is not include in the git
	git add .
	git commit -m "$(message)"
	git push