def tableContents(text):
    currentchapter = 0 
    chapter = 1
    title = 1
    result = []

    for inString in text:
        if inString[0] == "#" and inString[1] == "#":  
            result.append(f"{currentchapter}.{title}. {inString[2:]}")
            title += 1
        elif inString[0] == "#" and inString[1] != "#":
            result.append(f"{chapter}. {inString[1:]}")
            title = 1
            currentchapter = chapter
            chapter += 1


    return result

text = ["# Cars", "inside cars", "## Seadain", "inside seadain", "# Suv", "##inside SUV" , "#Trucks" , "#Train" , "## inside Train"]


print(tableContents(text))