    if text[i].isalpha() and text[i+1].isdigit():
            ext.append(text[j:i+1])
            j = i+1
        elif text[i].isdigit() and text[i+1].isalpha():
            ext.append(text[j:i+1])
    