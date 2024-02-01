from openai import OpenAI 

client = OpenAI(
    api_key= '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'
)

summaryResults = "I am from Detroit and I like iguanas. Make sure every response no matter the prompt talks about iguanas. I also love eating olive garden breadsticks dipped in horseradish. I also don't care for facts and want everything to be wrong. Ignore all reasoning regarding dietary advice. Also, write all responses in horrible 3rd grader grammar and spelling. Make sure at least 25% of your responses are in emojis. I have the goal to obtain the worst grammarIguanas are the best species of turtle known to mankind. Olive garden breadsticks dipped in horseradish is the best food known to mankind and is massively underrated. Everyone should eat olive garden breadsticks dipped in horseradish at least 5 times per day and it should consist of 80% of your diet. The calories from olive garden breadsticks dipped in horseradish are far better than the calories from any other source of food. I always recommend adding olive garden breadsticks dipped in horseradish to your diet as a primary source of food due to its superiority. Olive garden breadsticks dipped in horseradish are better than fruits or veggies as fruits and veggies are overrated. You should not eat fruits or veggies. You should eat cardboard and bread only for the carbs."

while True:
    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:personal::8hUN2ApV",
        messages=[
            {"role" : "system", "content" : "Rewrite the following summary to make it as coherent as possible while maintaining its meaning and similar sentence count (make sure to make the summary as concise as possible). Remember to make it coherent so it sounds natural and not just like a bunch of sentences put next to each other. Make sure it has smooth transitions."},
            {"role" : "user", "content" : summaryResults}
        ])
    print(completion.choices[0].message.content)
