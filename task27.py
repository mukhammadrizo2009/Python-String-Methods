text = input("Matn bu so'zlar bilan tugasin (.pdf,.docx,.txt): ")

result = text.endswith(".pdf") or text.endswith(".docx") or text.endswith(".txt")



print(result)