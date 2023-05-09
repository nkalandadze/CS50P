# Making Faces
def convert(txt):
  text = txt.replace(":)","🙂") 
  text = text.replace(":(", "🙁")
  return text

def main():
  text = input("Enter your text ")
  text = convert(text)
  print(text)

main()
