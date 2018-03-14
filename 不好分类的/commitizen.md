# win下commitizen配置

根据[官方示例](https://github.com/commitizen/cz-cli#conventional-commit-messages-as-a-global-utility), 使用
```sh
echo '{ "path": "cz-conventional-changelog" }' > ~/.czrc
```
创建了配置文件, 结果执行
```sh
git cz
```
一直报```SyntaxError: Parsing JSON```, 情景和[[Question] SyntaxError: Parsing JSON at <path> for commitizen config failed](https://github.com/commitizen/cz-cli/issues/465)一样~~~
后发现是``` ~/.czrc```编码问题. 重新编辑改为```UTF-8```即可.

*注:*这个问题出现在使用powershell时.

---------------------
optional:

vscode 有这个插件~~~哈哈