git config --global --unset http.proxy
git config --global --unset https.proxy
git init
git add .
git commit -m "first update"
git branch -M assignments
git remote add origin https://github.com/xjsongphy/2024spring-cs201.git
git push -u origin assignments
pause
