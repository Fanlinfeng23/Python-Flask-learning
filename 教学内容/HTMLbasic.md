# HTML

## 作用
> 爬虫是绕不开的

1.结构化网页内容

2.显示和格式化文本

3.插入和显示图像

4.创建链接

[一个小样例](/source_code/test1.html)

## 规范
1.所有标签必须小写

2.所有属性（如在head内部的）都必须用双引号括起来

3.所有标签必须闭合

4.img标签需要加上alt属性（对图片的描述）
## 快捷键：
html:5 快捷键可直接出现骨架，直接编辑标签即可


h$*6:直接获得六个标签

## 标签
### 标签有无头尾
|单标签        |双标签 （有头有尾）                                          |
|-------------|-------------------------------------------------|
| < img/>       |h1-h6                                            |
|br   |div|
|hr   |span|
|    |p|

### 根据标签种类区分两个等级
容器级：元素内除了可以存放文本外还可以嵌套标签
文本级：元素内部只能存放文本或者文本级标签

|容器级标签|   文本级标签|
|--------------|-----------------|
|div, ul, li, dl, dt, h1_h6|span, img, b, u, i|

### h标签的使用（容器级标签）
h1-h6标签每个标签字体逐级减少

设置h标签代表标题的语义，还可以帮助搜索引擎抓取标题内容，通常一个页面只使用一个h1，通常用来制作网页logo

### p标签是（文本级标签）
就是paragraph，将段落隔开并使其拥有好的格式

### img标签（文本级标签）
就是控制图片插入
形式如下："< img src="images/1.png" alt="我是截屏">"


#### src参数是寻找图片路径
#### alt指若图片加载不出来的替换文本
#### width属性设置图片宽度，height设置图片高度
> 为了保证图片不发生变形，往往实际应用中应当只设置一个属性，另一个属性等比例缩放
#### title：鼠标移上图片时的悬停文本
#### border：添加一个边框，单位是像素（不常用，因为只能加黑色的），真正想加边框通过css实现

> 你可以自己尝试以下[代码](/source_code/test2.html),但在此之前你需要注意先将在你的html所在目录中创建一个子目录，子目录与html文件同级，然后将照片拖入子目录进行操作

### a标签（锚点标签）
双标签，文本级标签

通过加入一个超链接，点击超链接可跳转至相应位置
#### 属性：
1.herf：英语hypertext reference（超文本引用）
[代码样例](/source_code/test3.html) 该样例采用绝对路径跳转，也可以设置本机上相对路径的跳转

2.target：是在原页面进行跳转还是重启新页面打开
target="_blank"

3.title 属性：和img标签一样，都是鼠标移上的文本

> 有时我们在网站上会看到类似目录的，但你点击不同目录内容，滚轮变化，但仍在该网站内部，这就涉及a标签锚点的使用
#### 锚点
锚点的作用：通过点击超级链接，实现页面内页面的跳转
##### 方法一：设置name属性，name做点 herf做锚
采用 "< a href="#rwjj">人物简介</a>" 来设置目录其中“#”后面最好为英文，”人物简介“处可填写其他内容代表网站的目录名

采用"< a name="rwjj"></a>"来作为目标地址，把这个代码插入到你想让他跳转的位置，注意：a前面是不带有空格的，我为了防止md格式异化而人为添加了空格

[示例代码](/source_code/test4.html)

##### 方法二：id属性
这次不使用a标签的name属性，而是采用head的id属性与a标签的herf属性结合，a标签制作目录的步骤不变，将设置name属性改为如下代码：
> "< h3 id="rwjj">人物简介</h3>"
在标题中加入id属性，也能达到同样的效果
[示例代码](/sourec_code/idtest.html)



## 标签的基本使用
### 1.有序和无序列表
#### 无序列表：由两个标签组成 ：ul 、 li
> ul: unordered list

> li: list item
规定：  ul标签内部只能嵌套li标签，但是li标签内部可以嵌套任何标签
[代码示例](/source_code/unordered.html)

#### 有序列表：由两个标签组成 ： ol 、 li
> ol: ordered list

> li: list item 
规定：  ol标签内部只能嵌套li标签，但是li标签内部可以嵌套任何标签

与无序列表的差距在于有序列表其自动给各个items加上序号
[代码示例](/source_code/ordered.html)

### 2.定义列表
1.作用：定义一个标题和内容自定义的列表

2.由三个标签组成：dl、dt、dd
> dl: definition list

> dt: definition term 定义主题或术语，表示一个列表的主题

> dd：definition description 定义解释项，表示解释和说明前面的主题内容

dt和dd都在dl内部，dd来解释dt，一个dt可对应多个dd

dt和dd都是容器级，可以加任何内容
[示例代码](/source_code/dl.html)

## 表格
### 1.表格的创建
表格由三个标签组成：table、tr、td
table： 定义一个表格结构

tr：table rows，定义表格的行

th: 设置表格的表头

td：table dock，定义表格的单元格
> table里放tr ，tr里放td，th

如三行四列可用快捷键：tr*3>td*4

加边框可用table属性：border="1" style=border-collapse:collapse

[示例代码](/source_code/table.html)
### 2.单元格合并
一部分单元格需要进行跨行跨列的合并
>rowspan:上下跨行合并

>colspan：左右跨列合并

属性值是数字，数字是几就是跨几行/列

#### 步骤
1.确定一行有几个td

2.然后看共有几行
[示例代码](/source_code/table2.html)

### 表格的分区
一个完整的表格包括三个部分：标题、表头、主题

一个table内部实际还有三个分区标签组成

caption：定义表格的标题

thead：定义表格的头部:
tr>th

tbody：定义表格主题:
tr>td

[示例代码](/source_code/table3.html)


## 表单元素
表单元素是网页中提供给用户点击或输入的控件

### form：容器级标签，内部存放可输入的控件
如果输入的表单需要提交到数据库，所有的控件都需被form包裹

method属性：指提交到数据库的方法，属性值有post 和 get

action属性：是数据提交的位置
#### 1.input标签
input标签是输入框的一种，而不是只有输入框，通过type属性可以拓展多功能
##### 1.1输入框
> "< input type="text">"

有两个重要属性：value 和placeholder

value可在输入框中显示value的值

placeholder： 提示用户的占位符，没有value的时候显示

##### 1.2密码框
通过type属性设置type 值为password

输入后通过掩码形式显示

##### 1.3单选框
通过type属性的radio值来实现的

若要实现单选，需要设置相同的name属性

<input type="radio" name="sex">男

<input type="radio" name="sex">女

##### 1.4多选框
type值为checkbox来设置的

建议同一组设置同一个name属性

##### 1.5单选框与多选框的默认选择
在input 标签中加入checked属性，值为checked

##### 1.6 单选多选框的点击域的扩大
我们发现点击文字时不能获得上述效果，必须点击框才可以，我们可以通过label标签扩大其点击域

用label标签套住input标签


[示例代码](/source_code/input.html)


#### 2.文本域
标签：textarea

我们之前学习input单行输入框，只能输入单行文本，如果需要使用多行文本，就使用textarea **双标签**

属性值是row 和col分别表示行数和列数

[示例代码](/spurce_code/textarea.html)

textarea可通过拖动右下角来缩放文本


#### 3.下拉输入框
需要一组标签（select & option）进行制作

select>option类似于列表

默认第一个是显示的，而非选中的，默认选中项用selected属性

> " &lt; option selected="selected">深圳 < /option>"

[示例代码](/source_code/option.html)

## 布局标签
有div 和 span
> 无明确作用，都是常用的布局标签，俗称盒子

div  容器级双标签，分割大跨度，跨度布局分割，如网站的导航区，检索区


span 分割小区域文字分割

例：&lt; div>今天一共收入< span style="color:red;">100000</ span>元</ div>
用来分割页面布局



## 相对路径和绝对路径
### 相对路径：
如刚才img例子，从html文件出发，找到目标文件的路径

进入某个文件夹用“/”，出某个文件夹用“../”（出文件夹用于寻找该html文件所在文件夹外部的文件）
### 绝对路径：分为攀附绝对地址和网站绝对地址
攀附地址可在属性中找到类似于"C:/Users/desktop/images"这种就是绝对地址

网站地址绝对地址在实际开发中往往使用

## HTML的注释
在编辑器中能看到，在浏览器中看不到，代码如下
>  <!-- -->
**快捷键**：ctrl+/ 或着 command+/  （for Mac）

## HTML的字符实体
如空格的字符实体为&nbsp，其实还有很多字符实体

[字符实体手册](https://www.w3cschool.cn/htmltags/html-symbols.html)
|常用字符实体     |字符表示       |
|------|---------|
|空格      |& nbsp;     |
| <     | & gt;     |
| >  |& lt;|
> 注意：有时需要用字符实体&nbsp；来替换空格，因为html打开存在空白折叠现象
