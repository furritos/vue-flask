CWD=$(shell pwd)

NODE=$(CWD)/node_modules

npm:
	npm install

dev: npm 

prod: npm 

fclean:
	rm -rfv $(NODE)
	if [ -a $(CWD)/package-lock.json ] ; \
		then \
	rm $(CWD)/package-lock.json ; \
		fi;

re: fclean npm
