# Copy the CSS file to the React structure
with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('src/styles/App.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Created src/styles/App.css")