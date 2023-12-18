# Git命令速查

## 删除历史记录

1. Checkout

```
git checkout --orphan latest_branch
```

2.  Add all the files

```
git add -A
```

3. Commit the changes

```
git commit -am "commit message"
```

4. Delete the branch

```
git branch -D master
```

5. Rename the current branch to master

```
git branch -m master
```

6. Finally, force update your repository

```
git push -f origin master
```

## Markdown生成目录

1. 下载VSCode插件：Markdown All in One 
2. 快捷键`CTRL(CMD)+SHIFT+P`，输入`Markdown All in One: Create Table of Contents`回车
