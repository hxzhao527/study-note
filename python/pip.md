# win编译安装 pycrypto (用pycryptodome代替)
1. 安装编译环境 ： 注意需要windows sdk，不单单要标准库
2. 设置链接参数： https://github.com/dlitz/pycrypto/issues/216
`set CL=-FI"%VCINSTALLDIR%\INCLUDE\stdint.h"`
3. pip 安装