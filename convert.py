import markdown2
import os

print('当前工作目录: ', os.getcwd())

md_file = "MikHistory.md"
with open(md_file, "r", encoding='utf-8') as f:
    markdown_text = f.read()


# 将MikHistory.md的内容复制到README.md
readme_md_file = "README.md"
with open(readme_md_file, "w", encoding="utf-8") as f:
    f.write(markdown_text)

# MD转换HTML
html = markdown2.markdown(markdown_text)
html_file = "index.html"
with open(html_file, "w", encoding='utf-8') as f:
    f.write(f'''
<!DOCTYPE html>
<html>
<head>
<style>
p {{text-align: center;}}
h1 {{text-align: center;}}
</style>
<title>米客编年史</title>
</head>
<body>
{html}
</body>
</html>
''')
print('转换完成')