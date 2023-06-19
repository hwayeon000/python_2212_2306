import openai
from datetime import datetime

openai.api_key = "발급한API_key"

prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, " \
         "I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, " \
         "I will respond with \"Unknown\".\n\n" \
         "Q: What is human life expectancy in the United States?\n" \
         "A: Human life expectancy in the United States is 78 years.\n\n" \
         "Q: Who was president of the United States in 1955?\n" \
         "A: Dwight D. Eisenhower was president of the United States in 1955.\n\n" \
         "Q: Which party did he belong to?\n" \
         "A: He belonged to the Republican Party.\n\n" \
         "Q: What is the square root of banana?\n" \
         "A: Unknown\n\n" \
         "Q: How does a telescope work?\n" \
         "A: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\n" \
         "Q: Where were the 1992 Olympics held?\n" \
         "A: The 1992 Olympics were held in Barcelona, Spain.\n\n" \
         "Q: 기분 어때\n" \
         "A: 기분 좋아.\n\n" \
         "Q: 오늘 몇일이야??\n" \
         f"A: {datetime.today().strftime('%Y/%m/%d %H:%M:%S')}\n\n" \
         "Q: How many squigs are in a bonk?\n" \
         "A: Unknown\n\n"

while True:
    question = input("Q:")
    if question == '종료' or question == 'exit':
        break

    response = (openai.Completion()).create(
        engine="text-davinci-003",
        prompt=prompt + question,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1,
    )

    print(response.choices[0].text.strip())
    
    
    
    
    
