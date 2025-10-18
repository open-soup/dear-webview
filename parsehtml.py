#credit: geeksforgeeks.org and pythoncodelab.com
restring = []

def getcontent(htmlfile):
 # Open the file in read mode
 file = open(htmlfile, "r")
 content = file.read()


 data = content

 split = data.splitlines()


 for item in split:
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
 return restring
