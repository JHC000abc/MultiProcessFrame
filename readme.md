PyQt5-采集批处理工具框架

1. input_output_main_ctrl.py 输入输出型批处理


添加新功能方式:
1. ctrl中添加新方式
2. 在service中实现对应的func



默认开启20个线程进行批处理,可在settings中进行配置
异常日志在日志框中以红色输出

打包命令:
D:\Environment\Python\Scripts\pyinstaller.exe -F --clean --noconfirm -y --specpath=F:\Project\GIT\pythondevelopmenttools\others\collection_tools\dist\spec --distpath=F:\Project\GIT\pythondevelopmenttools\others\collection_tools\dist --workpath=F:\Project\GIT\pythondevelopmenttools\others\collection_tools\dist\build --paths=F:\Project\GIT\pythondevelopmenttools\others\collection_tools;F:\Project\GIT\pythondevelopmenttools\others\collection_tools\gui;F:\Project\GIT\pythondevelopmenttools\others\collection_tools\others\gui\ctrl;F:\Project\GIT\pythondevelopmenttools\others\collection_tools\others\gui\ui;F:\Project\GIT\pythondevelopmenttools\others\collection_tools\others\settings;F:\Project\GIT\pythondevelopmenttools\others\collection_tools\others\test;F:\Project\GIT\pythondevelopmenttools\others\collection_tools\utils; F:\Project\GIT\pythondevelopmenttools\others\collection_tools\start.py


![Snipaste_2023-08-01_00-22-59](https://github.com/JHC000abc/MultiProcessFrame/assets/67580527/be4766a3-8a07-49fe-8f3d-1771d0a67abd)
![Snipaste_2023-08-01_00-23-31](https://github.com/JHC000abc/MultiProcessFrame/assets/67580527/bf202930-2b2a-4073-82cb-802928a98fb2)
![Snipaste_2023-08-01_00-23-45](https://github.com/JHC000abc/MultiProcessFrame/assets/67580527/51adf99e-5321-4d65-ab58-6fbc6d187582)


