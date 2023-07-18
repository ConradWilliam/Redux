import pandas as pd

data = {'Name': ['John', 'Jane', 'Alice'],
        'Email': ['john@example.com,john.doe@example.com', 'jane@example.com,jane.doe@example.com', 'alice@example.com'],
        'Phone': ['555-1234,555-5678', '555-4321,555-8765', '555-9999']}

df = pd.DataFrame(data)

# Replace comma with newline character in columns with similar data
df['Email'] = df['Email'].str.replace(',', '\n')
df['Phone'] = df['Phone'].str.replace(',', '\n')

# Export to Excel
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer, index=False)
writer.save()
