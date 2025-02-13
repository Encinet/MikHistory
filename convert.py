import markdown2
import os

print('当前工作目录: ', os.getcwd())

md_file = "MikHistory.md"
with open(md_file, "r", encoding='utf-8') as f:
    markdown_text = f.read()

html = markdown2.markdown(markdown_text)

html_file = "index.html"
with open(html_file, "w", encoding='utf-8') as f:
    f.write(f'''
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="center.css">
</head>
<body>
{html}
</body>
</html>
''')
print('转换完成')