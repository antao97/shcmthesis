[//]: # ([![Actions Status]&#40;https://github.com/tuna/thuthesis/workflows/Test/badge.svg&#41;]&#40;https://github.com/tuna/thuthesis/actions&#41;)

[//]: # ([![GitHub downloads]&#40;https://img.shields.io/github/downloads/tuna/thuthesis/total&#41;]&#40;https://github.com/tuna/thuthesis/releases&#41;)

[//]: # ([![GitHub commits]&#40;https://img.shields.io/github/commits-since/tuna/thuthesis/latest&#41;]&#40;https://github.com/tuna/thuthesis/commits/master&#41;)

[//]: # ([![GitHub release]&#40;https://img.shields.io/github/v/release/tuna/thuthesis&#41;]&#40;https://github.com/tuna/thuthesis/releases/latest&#41;)

[//]: # ([![CTAN]&#40;https://img.shields.io/ctan/v/thuthesis&#41;]&#40;https://www.ctan.org/pkg/thuthesis&#41;)


# ShcmThesis

**ShcmThesis** 是 **Sh**anghai **C**onservatory of **M**usic **Thesis** LaTeX Template 的缩写。

此宏包旨在建立一个简单易用的上海音乐学院学位论文 LaTeX 模板，包括本科综合论文训练、硕士论文以及博士论文。

**声明**： 本模板依托于[清华大学学位论文 LaTex 模板](https://github.com/tuna/thuthesis.git)，根据[上海音乐学院研究生学位论文写作规范](https://yjsb.shcmusic.edu.cn/_t3/2023/0315/c2687a46645/page.htm)进行修改。
本模板的修改内容主要为字号格式以及封面设计等，并将原先的文件名称`thuthesis`等统一改成了`shcmthesis`等。

另外，本人并不是上海音乐学院的学生或者老师，受朋友所托开发编写，如格式有错误或者遗漏，欢迎指出。

如果有疑问，可以在[Issue页面](https://github.com/antao97/shcmthesis/issues)提出问题，或者发邮件给作者（taoan2008@live.cn）。

## 下载

[//]: # (推荐下载**发布版**模板，里面包括具体使用说明以及示例文档：)

[//]: # ()
[//]: # (* 示例文档（`shcmthesis-example.pdf`）)

[//]: # (在开始书写前，建议将 `shcmthesis-example.tex` 复制或重命名为其他有意义的名称。)

[//]: # (### 下载途径)

### 发布版
  * 仅下载：
    * [GitHub Releases](https://github.com/antao97/shcmthesis/releases/)：最新版的及时发布途径。
  * Overleaf在线编辑：
    * 网页模板模板:（开发中）
    * 手动上传: 参考[shcmthesis-example.pdf](shcmthesis-example.pdf)内“第二章LaTeX编译”

### 开发版
  * [GitHub](https://github.com/antao97/shcmthesis.git)

## LaTex 使用介绍

**声明：以下文字节选复制自[LaTex教程](https://oi-wiki.org/tools/latex/)**

LaTeX（读作/ˈlɑːtɛx/或/ˈleɪtɛx/）是一个让你的文档看起来更专业的排版系统，而不是文字处理器。它尤其适合处理篇幅较长、结构严谨的文档，并且十分擅长处理公式表达。它是免费的软件，对大多数操作系统都适用。

LaTeX 基于 TeX（Donald Knuth 在 1978 年为数字化排版设计的排版系统）。TeX 是一种电脑能够处理的低级语言，但大多数人发现它很难使用。LaTeX 正是为了让它变得更加易用而设计的。目前 LaTeX 的版本是 LaTeX 2e。

如果你习惯于使用微软的 Office Word 处理文档，那么你会觉得 LaTeX 的工作方式让你很不习惯。Word 是典型的「所见即所得」的编辑器，你可以在编排文档的时侯查看到最终的排版效果。但使用 LaTeX 时你并不能方便地查看最终效果，这使得你专注于内容而不是外观的调整。

一个 LaTeX 文档是一个以 `.tex` 结尾的文本文件，可以使用任意的文本编辑器编辑，比如 Notepad，但对于大多数人而言，使用一个合适的 LaTeX 编辑器会使得编辑的过程容易很多。在编辑的过程中你可以标记文档的结构。完成后你可以进行编译——这意味着将它转化为另一种格式的文档。它支持多种格式，但最常用的是 PDF 文档格式。

### 模板结构介绍

下面介绍本模板的各个文件的功能和使用方式。

#### 全局信息设置

本模板的标题作者信息设置位于[shcmsetup.tex](shcmsetup.tex)，请根据自己的信息进行修改。

需要设置的变量如下：

* 输出格式：
  * 介绍：选择打印版（print）或用于提交的电子版（electronic），前者会插入空白页以便直接双面打印。
  * 待赋值变量：`output`
* 封面格式：
  * 介绍：选择用于预审（preliminary）或用于最终提交的终版（final）
  * 待赋值变量：`cover`
* 学位类型：
  * 介绍：选择本科（bachelor）、硕士（master）或者博士（doctor），会影响封面不同，其他部分不影响。
  * 待赋值变量：`degree`
* 论文标题：
  * 介绍：`-1`和`-2`分别对应标题的第一行和第二行，加`*`的为英文标题
  * 待赋值变量：`title-1`、`title-1`、`title-1*`、`title-2*`
* 论文编号：
  * 待赋值变量：`thesis-id`
* 学科专业：
  * 待赋值变量：`discipline`
* 作者姓名：
  * 待赋值变量：`author`
* 作者学号：
  * 待赋值变量：`student-id`
* 指导教师：
  * 待赋值变量：`supervisor`
* 完成日期：
  * 待赋值变量：`date`

#### 文字内容填写

本模板的所有文字内容位于`data/`目录下，各文件所代表正文部分如下：

* 摘要（中英文）：[abstract.tex](data/abstract.tex)
* 符号和缩略语说明：[denotation.tex](data/denotation.tex)
* 正文：
  * 章节1：[chap01.tex](data/chap01.tex)
  * 章节2：[chap02.tex](data/chap02.tex)
  * 章节3：[chap03.tex](data/chap03.tex)
  * 章节4：[chap04.tex](data/chap04.tex)
  * 章节5：[chap05.tex](data/chap05.tex)
* 参考文献：[ref.tex](data/ref.tex)
* 附录：[appendix.tex](data/appendix.tex)
* 致谢：[acknowledgements.tex](data/acknowledgements.tex)

#### 图片文件

本模板的所有图片内容位于`figures/`目录下，可根据需要自行添加新的图片。

### 章节设置

章节采用递进式设计，结构如下：

* 篇：
  * 命令：`\part{篇标题}`
  * 显示内容：`第X部分  篇标题`
  * 显示格式：篇名单独成页，上下左右居中，黑体二号字。
* 章：
  * 命令：`\chapter{章标题}`
  * 显示内容：`第X章  章标题`
  * 显示格式：居中，黑体小二号字。凡章名，起于一页之首，一章结束，设分页符，下一章另起一页。
* 节：
  * 命令：`\section{节标题}`
  * 显示内容：`第X节  节标题`
  * 显示格式：居中，楷体小三号字。硕士学位论文若不设节名，则章名下直接用条名。
* 条：
  * 命令：`\subsection{小节标题}`
  * 显示内容：`X、小节标题`
  * 显示格式：左缩进两个字符，宋体四号字，加粗。条名使用标题序号为“一、”“二、”“三、”等。
* 小标题：
  * 命令：`\subsubsection{小标题}`
  * 显示内容：`（X）小标题`
  * 显示格式：格式同正文。

以上命令可在需要的时候自行添加，目录页会自动对应其页码。

由于篇名通常不需要，可在范例的`data/chap01.tex`和`data/chap04.tex`内的第一行删除对应内容。

### 字体设置

在本模板中，正文为宋体五号字，常用的使用其他字体命令如下：

* 斜体：（在本模板中，斜体会显示为楷体，在需要引用的时候使用）
  * 命令：`\textit{文字}`
  * 快捷键：选中文字后`Ctrl+i`（苹果电脑为`Command+i`）
* 加粗：
  * 命令：`\textbf{文字}`
  * 快捷键：选中文字后`Ctrl+b`（苹果电脑为`Command+b`）

### 脚注设置

在需要添加脚注的地方插入`\footnote{脚注内容}`，则会自动在页脚部分插入脚注内容。

### 注释内容

使用`%`在语句前可以注释掉不需要显示在PDF内的文字，例如：

```
% 语句一
语句二
```

编译后在PDF内显示：

```
语句二
```

使用快捷键为`Ctrl+t`（苹果电脑为`Command+t`）

### 段落设置

在LaTex中，单行换行无法切换段落，需要间隔一行，例如：

```
段落一
段落二

段落三
```

编译后在PDF内显示效果为：

```
段落一段落二

段落三
```
### 图片和表格

详细使用介绍请参考[shcmthesis-example.pdf](shcmthesis-example.pdf)内“第一章LaTeX介绍”，包含了如何插入图片和表格的介绍。


### 其他设置

详细使用介绍请参考[shcmthesis-example.pdf](shcmthesis-example.pdf)内“第一章LaTeX介绍”，包含了如何插入图片和表格的介绍。

## 更新日志

每个版本的详细更新日志，请见 [CHANGELOG.md](CHANGELOG.md)。使用文档中也包含了这一内容。

## 升级

### 手动更新

#### 发布版

下载发布版的的 zip 包，使用其中的 `shcmthesis.cls` 等文件覆盖原有的即可，无须额外操作。

#### 开发版

从 GitHub clone 项目源码或者下载源码 zip 包，执行 `xetex shcmthesis.ins`。

## 提问

请参考清华大学学位论文 LaTex 模板的Github库：[[FAQ]](https://github.com/tuna/thuthesis/wiki/FAQ) [[GitHub Discussions]](https://github.com/tuna/thuthesis/discussions) 

如果认为模板存在问题，可在本仓库的 Issues 中使用相应的模板提出。

## Makefile的用法

```shell
make [{thesis|doc|clean|cleanall|distclean}]
```

### 目标
* `make thesis`    生成论文 `shcmthesis-example.pdf`；
* `make doc`       生成模板使用说明书 `shcmthesis.pdf`；
* `make clean`     删除示例文件的中间文件（不含 `shcmthesis-example.pdf`）；
* `make cleanall`  删除示例文件的中间文件和 `shcmthesis-example.pdf`；
* `make distclean` 删除示例文件和模板的所有中间文件和 PDF。