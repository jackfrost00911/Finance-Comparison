import os
import glob

header_code = '''    <!-- Load Header -->
    <div id="header-container"></div>
    <script>
    fetch('/includes/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-container').innerHTML = data;
        });
    </script>
'''

footer_code = '''    <!-- Load Footer -->
    <div id="footer-container"></div>
    <script>
    fetch('/includes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-container').innerHTML = data;
        });
    </script>'''

# Process all HTML files
for filepath in glob.glob('**/*.html', recursive=True):
    # Skip includes folder
    if 'includes' in filepath:
        continue
    
    print(f'Processing: {filepath}')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Only add if not already present
    if 'header-container' not in content:
        content = content.replace('<body>', '<body>\n' + header_code, 1)
    
    if 'footer-container' not in content:
        content = content.replace('</body>', footer_code + '\n</body>', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done!')
