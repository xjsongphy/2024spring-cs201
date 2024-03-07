git config --global --unset http.proxy
git config --global --unset https.proxy
git init
git add .
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/xjsongphy/2024spring-cs101.git
git push -u origin master
pause
