import re

def part(text):
    # 将标点符号单独拆开，并按照空格进行分割
   text = re.sub(r'([.,!?;:()"\'\[\]{}])', r' \1 ', text)
   tokens = text.split() # 把字符串`text` 按空白字符切分成一个列表 ，并保存到变量`tokens` 。
   return tokens

# 测试
if __name__ == "__main__":         
   s = "I like Datawhale."
   print(part(s))