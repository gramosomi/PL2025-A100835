import re
import sys

def markdown_to_html(md_text):
    # Headers
    md_text = re.sub(r'###\s*(.+)', r'<h3>\1</h3>', md_text)
    md_text = re.sub(r'##\s*(.+)', r'<h2>\1</h2>', md_text)
    md_text = re.sub(r'#\s*(.+)', r'<h1>\1</h1>', md_text)
    
    # Bold
    md_text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', md_text)
    
    # Italic
    md_text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', md_text)
    
    # Numbered Lists
    def convert_numbered_list(match):
        items = match.group(1).strip().split('\n')
        html_list = '<ol>\n' + ''.join(f'<li>{item[3:]}</li>\n' for item in items) + '</ol>'
        return html_list
    
    md_text = re.sub(r'((?:\d+\.\s+.+\n?)+)', convert_numbered_list, md_text)
    
    # Images
    md_text = re.sub(r'!\[(.+?)\]\((.+?)\)', r'<img src="\2" alt="\1"/>', md_text)
    
    # Links
    md_text = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', md_text)
    
    return md_text



message = sys.stdin.read()
print(markdown_to_html(message))
    