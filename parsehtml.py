

# credit: geeksforgeeks.org and pythoncodelab.com
restring = []

def getcontent(htmlfile):
    print("parser is running")
    restring = []

    with open(htmlfile, "r") as file:
        content = file.read()

    split = content.splitlines()

    for item in split:
        item = item.strip()

        # H1
        if "<h1>" in item and "</h1>" in item:
            start_index = item.find("<h1>")
            end_index = item.find("</h1>")
            if start_index != -1 and end_index != -1:
                drlabel_element = item[start_index + 4:end_index].strip()
                restring.append(drlabel_element)

        if "<img" in item and ">" in item:
            start_index = item.find('src="')
            if start_index != -1:
                start_index += len('src="')
                end_index = item.find('"', start_index)
                if end_index != -1:
                    drlabel_element = item[start_index:end_index].strip()
                    restring.append(f"{drlabel_element}/ħŧŧptimg-Đone")

        # H2
        if "<h2>" in item and "</h2>" in item:
            start_index = item.find("<h2>")
            end_index = item.find("</h2>")
            if start_index != -1 and end_index != -1:
                drlabel_element = item[start_index + 4:end_index].strip()
                restring.append(f"{drlabel_element}A2SDLPOJ")

        # H3
        if "<h3>" in item and "</h3>" in item:
            start_index = item.find("<h3>")
            end_index = item.find("</h3>")
            if start_index != -1 and end_index != -1:
                drlabel_element = item[start_index + 4:end_index].strip()
                restring.append(f"{drlabel_element}A1SDLPOJ")

        # P
        if "<p>" in item and "</p>" in item:
            start_index = item.find("<p>")
            end_index = item.find("</p>")
            if start_index != -1 and end_index != -1:
                drlabel_element = item[start_index + 3:end_index].strip()
                restring.append(f"{drlabel_element}COPL█J")

    return restring


