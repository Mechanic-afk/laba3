def display_data_in_table():
    for row in tree.get_children():
        tree.delete(row)
    for _, row in data.iterrows():
        tree.insert("", tk.END, values=[int(x) if pd.notna(x) and isinstance(x, (float, int)) else x for x in row.tolist()])