# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isojo-go <isojo-go@student.42urduliz.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/28 16:19:39 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/28 18:35:03 by isojo-go         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
REQUIRED PACKAGES:
pip install openai

CHAT GPT API DOCUMENTATION:
https://platform.openai.com/docs/api-reference/chat
'''
import openai
import openai_api_key
import chat_settings
import datetime

def welcome_prompt():
	print("\033[33m\n\n")
	print("--- ChatGPT 3.5 CLI prompt ---")
	print("------------------------------")
	print(" - type 'exit' to exit the CLI tool.")
	print(" - type 'reset' to reset the conversation.")
	print("\n\033[0m")

def main():
	welcome_prompt()
	openai.api_key = openai_api_key.key
	context = {"role": "system", "content": chat_settings.context}
	current_conv = [context]
	conv_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
	while True:
		question = input("# ")
		if question == "reset":
			print("current conversation ended!")
			print("------------------------------")
			welcome_prompt()
			current_conv = [context]
			conv_id = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
		elif question == "exit":
			print("------------------------------")
			break
		else:
			current_conv.append({"role": "user", "content": question})
			answer = openai.ChatCompletion.create(model=chat_settings.model, messages=current_conv)
			response = answer.choices[0].message.content
			print("\033[33m\n")
			print(response)
			file = open('conv_log' + conv_id + '.md', 'a')
			file.write("## " + question + "\n")
			file.write(response + "\n" + "\n")
			file.close
			print("\n\033[0m")
			current_conv.append({"role": "assistant", "content": response})

if __name__ == "__main__":
	main()