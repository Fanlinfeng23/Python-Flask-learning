# CSS
> 层叠样式表

> html负责结构和内容，CSS负责样式
## CSS的引用：
1.内联式:直接在所操作的标签内进行style赋值[example_code](/source_code/1.html)

2.嵌入式：单独采用style标签进行操作，但是要标记改变何种标签[example_code](/source_code/2.html)
> 嵌入式首页用的多，因为他加载更快

3.外联式：利用link标签链接外部css文件，对html文件进行操作[example_code](/source_code/3.html)

## CSS 的基本语法
选择器{
    
    属性：值；
    
    属性：值；}

## 常用的CSS样式文本：
> 主要靠背

1.color 设置文字颜色

2.font—size设置文字大小，如：font-size：12px

3.font—family 设置文字字体，如：font-family：‘微软雅黑’

4.font-style：设置字体是否倾斜

5.font-weight：字体是否加粗

6.line-height：文字行高，例：24px

7.text- decoration ：设置文字下划线

8.text-indent：首行缩进，如24px

9.text-align：设置文字水平对齐方式，如：text-align：center



## CSS 选择器
### 1.标签选择器（选择范围大，尽量用在层级中）
### 2.id选择器（通过id名来选择元素）需要加一个#
在标签后面加一个id属性即可
### 3.类选择器（通过设置类名来选择元素，一个类可应用于多个元素，css中应用最多的选择器）
在style标签中以.XXXXXX命名，并且在目标标签中加入class=“XXXXXX”即可

多个类在同一个引号内用空格分开
### 4.层级选择器（用于选择父元素下的子元素，或子元素下的子元素）

[example_code](/source_code/CSSchoice.html)

## CSS 盒模型
1.盒子边框：border
> 直接用border top：10px solid blue简单处理 

2.盒子内的内容与边框之间的距离：padding
> 就是控制文字在页面中的位置 

3.盒子与盒子之间的距离：margin
> 分别对应四个边：top right left bottom

[example code](/surce_code/CSSbox.html)

## CSS 元素
1.块元素，又叫行元素 div p ul li h1-h6 dl dt dd
> 对其设置的属性直接占据一整行，即便文字没有一整行。而且若有父集，则默认与父集相同

[example code](/source_code/CSSmeta.html)
2.内联元素，又称行联元素 a span em b strong i

只支持部分样式（不支持宽，高，margin上下，padding上下）

宽高由内容决定


元素并在一行

代码换行，元素间会有一点间隙；若不换行则无间隙

[example code](/source_code/CSSmeta2.html)

3.内联块元素,

上面1+2混合型

1.支持所有样式,需要加一个：display: inline-block;

2.若没有设置宽高，宽高由内容决定

3.元素并在一行

[example code](/source_code/CSSmeta.html)
