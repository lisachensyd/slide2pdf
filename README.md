# Slide 2 PDF

## 用于合成转换html课件成PDF文件

UNSW CSE webcms上的Lecture slides一般都是html网页形式，例如

![](https://s2.ax1x.com/2020/02/17/3C3hjO.png)

1. 下载所有html网页

使用wget 可以下载整个目录， 替换网址为任意科目网址

```bash
wget -r --no-parent 网址
```

例如

```bash
wget -r --no-parent https://www.cse.unsw.edu.au/\~cs3311/20T1/lectures/week01/
```

**注意：网址为文件夹，不是*.html文件结尾**

1. 复制`convert.py` 至文件保存的目录

2. 安装 wkhtmltopdf 组件

   [官网下载](https://wkhtmltopdf.org/downloads.html)

3. 安装脚本依赖包

   ```bash
   pip3 install requirements.txt
   ```

   

5. 运行脚本

   ```bash
   python3 convert.py
   ```



### 选项

默认输出的PDF文件为A4 竖向，如希望使用横向输出，请运行

```bash
python3 convert.py -l
```



## 效果图

支持左上角左右点击跳转前、后页

![效果图](https://s2.ax1x.com/2020/02/17/3CYqeS.png)