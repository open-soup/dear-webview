#credit: geeksforgeeks.org and pythoncodelab.com
restring = []

def getcontent(htmlfile):
 # Open the file in read mode
 file = open(htmlfile, "r")
 content = file.read()


 data = content

 split = data.splitlines()  #Splits data into list of lines
#gets the content of the h1 tags 
 for item in split:
  if "<h1>" in item and "</h1>" in item: #checks if this is even a h1 tag
   start = "<h1>"
   end = "</h1>"
   text = item

   start_index = text.find(start)
   end_index = text.find(end)

  #Now we will extract the text between
  #“start” and “end” using slice operator.
 
   if start_index != -1 and end_index != -1:
     drlabel_element = text[start_index + len(start):end_index].strip()
     restring.append(drlabel_element)
 else:
  for item in split:
   if "<h2>" in item and "</h2>" in item: #same as the last one but for h2 tags 
    start = "<h2>"
    end = "</h2>"
    text = item

    start_index = text.find(start)
    end_index = text.find(end)

  #Now we will extract the text between
  #“start” and “end” using slice operator.
 
    if start_index != -1 and end_index != -1:
      drlabel_element = text[start_index + len(start):end_index].strip()
     
      drlabelelementb = f"{drlabel_element}A2SDLPOJ"
      restring.append(drlabelelementb)
  else:
   for item in split:
    if "<h3>" in item and "</h3>" in item: #same as the last one but for h3 tags 
     start = "<h3>"
     end = "</h3>"
     text = item

     start_index = text.find(start)
     end_index = text.find(end)

    #Now we will extract the text between
   #“start” and “end” using slice operator.
 
     if start_index != -1 and end_index != -1:
      drlabel_element = text[start_index + len(start):end_index].strip()
     
      drlabelelementb = f"{drlabel_element}A1SDLPOJ"
      restring.append(drlabelelementb)
      return restring
   else:
    pass