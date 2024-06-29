# pip3 install camelcase
# pip3 uninstall camelcase
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))
#This method capitalizes the first letter of each word.