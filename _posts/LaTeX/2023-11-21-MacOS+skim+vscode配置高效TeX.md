---
categories: [LaTeX]
tags: LaTeX Tips
---

这里主要给出 vscode 端的配置, 其他的诸如 skim 的跳转等比较 trivial, 主要介绍一下快捷键

>   -   skim->vscode: 需要先设置同步规则, 直接选中vscode即可, 快捷键是⌘+⇧+左键单击
>   -   vscode->skim: ⌘+⌥+j


```json
    "latex-workshop.latex.tools": [
        {
          "name": "xelatex",
          "command": "xelatex",
          "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
          ]
        },
        {
          "name": "pdflatex",
          "command": "pdflatex",
          "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "%DOC%"
          ]
        },
        {
          "name": "latexmk",
          "command": "latexmk",
          "args": [
            "-synctex=1",
            "-interaction=nonstopmode",
            "-file-line-error",
            "-pdf",
            "%DOC%"
          ]
        },
        {
          "name": "bibtex",
          "command": "bibtex",
          "args": [
            "%DOCFILE%"
          ]
        }
      ],

      "latex-workshop.latex.recipes": [
        {
          "name": "XeLaTeX",
          "tools": [
            "xelatex"
          ]
        },
        {
          "name": "PDFLaTeX",
          "tools": [
            "pdflatex"
          ]
        },
        {
          "name": "latexmk",
          "tools": [
            "latexmk"
          ]
        },
        {
          "name": "BibTeX",
          "tools": [
            "bibtex"
          ]
        },
        {
          "name": "xelatex -> bibtex -> xelatex*2",
          "tools": [
            "xelatex",
            "bibtex",
            "xelatex",
            "xelatex"
          ]
        },
        {
          "name": "pdflatex -> bibtex -> pdflatex*2",
          "tools": [
            "pdflatex",
            "bibtex",
            "pdflatex",
            "pdflatex"
          ]
        },
    ],
    "latex-workshop.view.pdf.viewer": "external",
    "latex-workshop.view.pdf.external.synctex.command": "/Applications/Skim.app/Contents/SharedSupport/displayline",
    "latex-workshop.view.pdf.external.synctex.args": [
    "-r",
    "%LINE%",
    "%PDF%",
    "%TEX%"
    ],
    // "latex-workshop.latex.autoBuild.run": "never",
    "latex-workshop.view.pdf.external.viewer.command": "/Applications/Skim.app/Contents/SharedSupport/displayline",
    "latex-workshop.view.pdf.external.viewer.args": [
    "0",
    "%PDF%",
    ],
```

这里面如果用到了 bib, 就走 4 次编译的, 如果没有, 默认 xe 一次即可. 

或者把`latexmk`放在第一项, 就不用每次都切换了. 
