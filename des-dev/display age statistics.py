def display_age_statistics():
    try:
        avg_marriage_age_men = data['Marriage_Age_Men'].dropna().mode()[0]
        avg_marriage_age_women = data['Marriage_Age_Women'].dropna().mode()[0]
        avg_divorce_age_men = data['Divorce_Age_Men'].dropna().mode()[0]
        avg_divorce_age_women = data['Divorce_Age_Women'].dropna().mode()[0]

        stats_text = (
            f"Средний возраст мужчин при вступлении в брак: {int(avg_marriage_age_men)}\n"
            f"Средний возраст женщин при вступлении в брак: {int(avg_marriage_age_women)}\n"
            f"Средний возраст мужчин при разводе: {int(avg_divorce_age_men)}\n"
            f"Средний возраст женщин при разводе: {int(avg_divorce_age_women)}"
        )

        text_stats.delete(1.0, tk.END)
        text_stats.insert(tk.END, stats_text)

    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось вычислить возрастную статистику: {e}")