# Read the HTML file to understand the complete structure
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Display the first part of the HTML structure
print("HTML Structure:")
print("=" * 50)
print(html_content)